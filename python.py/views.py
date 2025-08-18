from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import path
from . import views

@api_view(['GET'])
def restaurant_menu(request):
    menu = [
        {"name": "Paneer Butter Masala", "description": "Rich and creamy panner curry", "price": 599.00},
        {"name": "Chicken Biryani", "description": "Aromatic basmati rice with tender chicken", "price": 649.00},
        {"name": "Margherita Pizza", "description": "Classic cheese pizza with tomato base", "price": 399.00},
        {"name": "Masala Dosa", "description": "Crispy dosa stuffed with spiced potato and tomato filling", "price": 249.00},
    ]

urlpatterns = [
    path('menu/', views.restaurant_menu, name='restaurant-menu'),
]