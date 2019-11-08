from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from hotel.views import *
from checkout.views import *


urlpatterns = [
	path('admin/', admin.site.urls),
	
	path('', home, name='home'),
	path('api/city/', get_city),
	path('api/hotel/', get_hotel),
	path('api/detail/', get_detail),
	path('api/room/', get_room),

	path('hotel_list/', hotel_list),
	path('hotel_detail/', hotel_detail),

	path('api/checkout/', checkout),

	path('checkout/', checkout),
	path('card_payment/', card_payment),
	path('net_banking/', net_banking),
	path('card_success_page/', card_success_page),
	path('net_success_page/', net_success_page)
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)