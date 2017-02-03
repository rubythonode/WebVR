from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse

from inventory.models import *

# Mobile Web UI
def index(request):
    houses = House.objects.all()
    return render(request, 'mobile_web/login/login.html', {
        'houses': houses,
    })

def map(request):
    return render(request, 'mobile_web/map/map.html')

def list(request):
    return render(request, 'mobile_web/list/list.html')

def house(request):
    return render(request, 'mobile_web/house/house.html')

# VR
def panorama(request):
    return render(request, 'inventory/panorama.html')

def hackingroom1(request):
    return render(request, 'inventory/hackingroom1.html')

def hackingroom2(request):
    return render(request, 'inventory/hackingroom2.html')

def hallway(request):
    return render(request, 'inventory/hallway.html')

def lobby(request):
    return render(request, 'inventory/lobby.html')

def office(request):
    return render(request, 'inventory/office.html')

def toilet4man(request):
    return render(request, 'inventory/toilet4man.html')

def customer_center(request):
    return render(request, 'inventory/customer_center.html')
