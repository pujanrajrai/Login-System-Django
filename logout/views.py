from django.shortcuts import render,redirect
from django.contrib.auth import logout

# Create your views here.
def index(request):
    logout(request)
    return redirect('loginPage')