from django.conf import settings
from django.shortcuts import render

def homepages(request):
    restaurant_name = "My Restaurant"
    phone_number = settings.RESTAURANT_PHONE
    return render(request, "home.html".{
        "restaurant_name": restaurant_name,
        "phone_number": phone_number
    })