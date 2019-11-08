from django.db import models

# Create your models here.
class User_detail(models.Model):
	user_name = models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	email = models.CharField(max_length=100)