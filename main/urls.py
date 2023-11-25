from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.main_page, name="home"),
    path('instructions/', views.main_page, name="instructions")
]
