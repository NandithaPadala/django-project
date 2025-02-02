from django.shortcuts import render,redirect
from .models import Destination
from django.contrib.auth.models import User, auth

# Create your views here.
def index(request):
    dests = Destination.objects.all()
    return render(request,'index.html',{'dests' : dests})

def register(request):
    return redirect('signup.html')