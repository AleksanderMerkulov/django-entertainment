from django.shortcuts import render
from .models import Event
from django.views.generic import DetailView


# Create your views here.
def events_all(request):
    events = Event.objects.all()

    return render(request, 'events/events_all.html', {"events": events})


class EventDetail(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'
