from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.events_all, name="events_all"),
]