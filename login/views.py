


from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from login.form import LoginForm
# Create your views here.
def index(request):
    context={}
    user=request.user
    if user.is_authenticated:
        return redirect('profilePage')
    if request.POST:
        form=LoginForm(request.POST)
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            user=authenticate(email=email,password=password)
            if user:
                login(request,user)
                return redirect('profilePage')
    else:
        form=LoginForm()    
    context['login_form']=form
    return render(request,'login/login.html',context)
