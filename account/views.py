import django.utils.timezone
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from events.models import Event


# Create your views here.
@login_required
def account(request):
    future_event = Event.objects.filter(creator_id=request.user.id) & Event.objects.filter(
        date__lt=django.utils.timezone.now())

    today_event = Event.objects.filter(creator_id=request.user.id) & Event.objects.filter(
        date__day=django.utils.timezone.now().day)

    context = {
        'future_event': future_event,
        'today_event': today_event
    }

    return render(request, 'account/account_main.html', context)
    pass
