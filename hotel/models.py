from django.db import models

class City(models.Model):
	city = models.CharField(max_length=100)
	image = models.FileField(default='default.png',blank=True)

	def __str__(self):
		return self.city+'-'+str(self.id)


class Hotel(models.Model):
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=500)
	city = models.CharField(max_length=100)
	ratings = models.FloatField(blank=True)
	price = models.CharField(max_length=100)
	total_rooms = models.IntegerField(blank=True)

	def __str__(self):
		return self.name +', '+ self.city


class Room(models.Model):
	room_type = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	price = models.CharField(max_length=100)
	
	def __str__(self):
		return self.room_type

class Option(models.Model):
	option = models.CharField(max_length=100)
	choice = models.CharField(max_length=500)
	price = models.CharField(max_length=100)

	def __str__(self):
		return self.choice 

class Image(models.Model):
	image = models.FileField(default='default.png',blank=True)
	hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.hotel.name


class Search(models.Model):
	city = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True)
	check_in = models.CharField(max_length=100)
	check_out = models.CharField(max_length=100)
	room = models.IntegerField(blank=True)

	def __str__(self):
		return self.check_in+'-'+self.check_out	