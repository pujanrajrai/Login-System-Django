"""loginSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from logout import views as logout_views
from login import views as login_views
from info import views as info_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',include('register.urls')),
    path('logout/',logout_views.index,name='logoutPage'),
    path('login/',login_views.index,name='loginPage'),
    path('profile/',info_views.index,name='profilePage'),
]