from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


def main_page(request):
    return render(request, 'main/main.html')
    pass


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
