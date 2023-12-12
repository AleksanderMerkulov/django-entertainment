from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from events.models import *


def main_page(request):
    cinemas = Event.objects.filter(category_id=2) & Event.objects.filter(typeOfEvent__name='public')[0:5]
    actual = Event.objects.filter(category_id=4) & Event.objects.filter(typeOfEvent__name='public')[0:5]
    theaters = Event.objects.filter(category_id=3) & Event.objects.filter(typeOfEvent__name='public')[0:5]
    jopa = None
    if True:
        jopa = Event.objects.all()

    return render(request, 'main/main.html', {"cinemas": cinemas, "actual": actual, "theaters": theaters, "jopa": jopa})
    pass


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
