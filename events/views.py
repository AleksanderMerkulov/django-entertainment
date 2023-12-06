from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from .forms import AddEvent
from .models import *
from django.views.generic import DetailView


# Create your views here.
def events_all(request):
    events = Event.objects.all()
    return render(request, 'events/events_all.html', {"events": events})


class EventDetail(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'


def events_all_by_category(request, pk="all"):
    id_cat = Category.objects.filter(title=pk).first()
    if id_cat is None:
        return redirect('events_all')
    events = Event.objects.filter(id=id_cat.id)
    return render(request, "events/events_all.html", {"events": events})


def addEvent(request):
    if request.method == "POST":
        form = AddEvent(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
    else:
        form = AddEvent()
    return render(request, 'events/addEvent.html', {"form": form})
