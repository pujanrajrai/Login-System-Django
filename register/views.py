# from django.shortcuts import render
# from django.http import HttpResponse
# from register.models import Account
# # Create your views here.

# def index(request):
#     contex={}
#     accounts=Account.objects.all()
#     contex['accounts']=accounts
#     return render(request,'register/home.html',contex)


from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from register.form import RegistrationForm

def index(request):
    context={}
    user=request.user
    if user.is_authenticated:
        return redirect('profilePage')
    if request.POST:
        form = RegistrationForm(request.POST)
        print('post request')
        if form.is_valid():
            print('valid')
            form.save()
            email=form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account=authenticate(email=email,password=raw_password)
            login(request,account)
            return redirect('profilePage')
        else:
            context['registration_form']=form
    else:
        print('not post request')
        form=RegistrationForm()
        context['registration_form']=form
    return render(request,'register/register.html',context)