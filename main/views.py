from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from events.models import *


def main_page(request):
    cinemas = Event.objects.filter(category_id=2) & Event.objects.filter(typeOfEvent__name='public')[0:5]
    actual = Event.objects.filter(category_id=4) & Event.objects.filter(typeOfEvent__name='public')[0:5]
    theaters = Event.objects.filter(category_id=3) & Event.objects.filter(typeOfEvent__name='public')[0:5]

    return render(request, 'main/main.html', {"cinemas": cinemas, "actual": actual, "theaters": theaters})
    pass


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
