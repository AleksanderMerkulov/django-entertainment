from django.shortcuts import render

# Create your views here.
def events_all(request):
    return render(request, 'events/events_all.html')
