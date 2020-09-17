from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
# Create your views here.
from register.models import Account

def index(request):
    user=request.user
    print(user)
    if user.is_authenticated:
        context={}
        accounts=Account.objects.all()
        context['accounts']=accounts
        return render(request,'information/information.html',context)
    return redirect('loginPage')
