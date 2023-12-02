from django.contrib import admin
from django.urls import path, include
from account import views

urlpatterns = [
    path('', views.account, name="account"),
]