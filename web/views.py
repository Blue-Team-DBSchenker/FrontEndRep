from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from web.models import *

import requests as r
# Create your views here.

def index(request):
  context = dict()
  context['details'] = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Et tamen tantis vectigalibus ad liberalitatem utens etiam sine hac Pyladea amicitia multorum te benivolentia praeclare .'
  context['image'] = 'https://www.metoffice.gov.uk/binaries/content/gallery/mohippo/images/migrated-image/c/cirrus_clouds.jpg'
  return render(request,'index.html', context=context)




def login(request):
  return render(request,'login.html')

def register(request):
  return render(request,'register.html')


def home(request):
  return render(request, 'home.html')

def userregister(request):
  return render(request, 'userregister.html')

def user(request):
  return render(request, 'user.html')

def user1(request):
  return render(request, 'user1.html')


def userlogin(request):
  return render(request, 'userlogin.html')

def usertable(request):
  return render(request, 'usertable.html')