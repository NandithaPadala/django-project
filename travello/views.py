from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):


    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'Bussiest Place in the world'
    dest1.img = 'package-1.jpg'
    dest1.price = 700
    dest1.offer = True

    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.desc = 'First Biryani ,Then sherwani'
    dest2.img = 'package-2.jpg'
    dest2.price = 650
    dest2.offer = False

    dest3 = Destination()
    dest3.name = 'Bangaluru'
    dest3.desc = 'This is my third place to visit'
    dest3.img = 'package-3.jpg'
    dest3.price = 705
    dest3.offer = False

    dests = [dest1,dest2,dest3]


    return render(request,'index.html',{'dests' : dests})