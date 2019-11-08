from django.shortcuts import render
import json
from django.http import HttpResponse
# from models.py
from hotel.models import *
from pprint import pprint 

def home(request):
	selected = City.objects.all()
	return render(request,'home.html',{'city':selected})


def get_city(request):
	cities = City.objects.all()
	values = []
	for city in cities:
		values.append({"id": city.id, "name": city.city, "image": city.image.url})	
	values = json.dumps(values)
	return HttpResponse(values, content_type="application/json")


def get_hotel(request):
	values = []
	city = request.GET.get("city")
	hotels = Hotel.objects.filter(city=city)
	for hotel in hotels:
		images = Image.objects.filter(hotel=hotel)	
		image_list = []
		for image in images:
			image_list.append(image.image.url)
		values.append({"id":hotel.id, "name":hotel.name,"ratings":hotel.ratings,"price":hotel.price, "images":image_list})
	values = json.dumps(values)
	return HttpResponse(values, content_type="application/json")


def hotel_list(request):
	return render(request,"hotel_list.html")


def get_detail(request):
	values = []
	hotel_id = request.GET.get("hotel")
	hotel = Hotel.objects.get(pk=int(hotel_id))
	images = Image.objects.filter(hotel=hotel)	
	image_list = []
	for image in images:
		image_list.append(image.image.url)
	values.append({"name":hotel.name, "ratings":hotel.ratings, "address":hotel.address, "price":hotel.price, "images":image_list})
	values = json.dumps(values)
	return HttpResponse(values, content_type="application/json")


def get_room(request):
	values=[]
	city = request.GET.get("city")
	hotels = Hotel.objects.filter(city=city)
	rooms = Room.objects.all()
	options = Option.objects.all()
	rooms_json = list(rooms.values())
	options_json = list(options.values())
	final = {"rooms" : rooms_json, "options": options_json}
	values = json.dumps(final)
	return HttpResponse(values, content_type="application/json")


def hotel_detail(request):
	return render(request,"hotel_detail.html")

