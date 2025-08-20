import requests
from django.shortcuts import render

def homepage(request):
    response = requests.get("http://127.0.0.1:8000/api/menu/")
    if response.status_code == 200:
        menu = response.json()
    else:
        menu = []

    return render(request, "dmohp.html", {"menu":menu})