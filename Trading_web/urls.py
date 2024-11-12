"""
URL configuration for Trading_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from bot.views import money_management,contact,Generate_key,entery,Check_key,Check_utr,check_admin 

urlpatterns = [
    path('', entery),
    path('Moneymanegment', money_management, name='money_management'),
    path('admin', admin.site.urls),
    path('contact/', contact),
    path('Generatekey', Generate_key),
    path('checkingkey', Check_key),
    path('Checkutr',Check_utr),
    path('checkadmin',check_admin)
]