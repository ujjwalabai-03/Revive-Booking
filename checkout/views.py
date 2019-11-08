from django.shortcuts import render
from hotel.models import *
from checkout.models import *

total_price=""

def checkout(request):
	if request.method == "POST":
		room_value = request.POST.get('select_room')
		option_value = request.POST.get('select_option')
		selected_room = Room.objects.get(id=room_value)
		selected_option = Option.objects.get(id=option_value)
	hotel_id = request.GET.get("hotel")
	hotel_name = Hotel.objects.get(id=hotel_id)
	global total_price
	total_price = int(selected_room.price) + int(selected_option.price) + int(hotel_name.price)
	return render(request, "checkout.html",{"room":selected_room,"option":selected_option,"hotel_name":hotel_name, "total_price":total_price})


def card_payment(request):
	user_name = request.POST.get("customer_name")
	phone = request.POST.get("customer_phone")
	email = request.POST.get("customer_email")
	User_detail.objects.create(user_name=user_name,phone=phone,email=email)
	total = total_price
	return render(request, "card.html",{"total":total})


def card_success_page(request):
	total =total_price
	return render(request, "card.html" ,{"total":total})


def net_success_page(request):
	total =total_price
	return render(request, "net_success.html",{"total":total})


def net_banking(request):
	total =total_price
	return render(request, "net_banking.html",{"total":total})	

