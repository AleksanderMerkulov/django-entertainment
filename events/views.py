from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Event
from django.views.generic import DetailView


# Create your views here.
def events_all(request):
    events = Event.objects.all()
    if request.user.is_authenticated:
        return render(request, 'events/events_all.html', {"events": events})
    else:
        return redirect('home')


class EventDetail(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'
