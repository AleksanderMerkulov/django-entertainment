from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.events_all, name="events_all"),
    path('<int:pk>/', views.EventDetail.as_view(), name="event_detail"),
    # path('category/', views.events_all, name="events_by_all_category"),
    path('<str:pk>/', views.events_all_by_category, name="event_by_category"),
    path('add/event/', views.addEvent, name="add_event"),
]
