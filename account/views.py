import django.utils.timezone
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView

from events.models import Event


# Create your views here.
@login_required
def account(request):
    future_event = Event.objects.filter(creator_id=request.user.id) & Event.objects.filter(
        date__gt=django.utils.timezone.now())

    today_event = Event.objects.filter(creator_id=request.user.id) & Event.objects.filter(
        date__day=django.utils.timezone.now().day)

    context = {
        'future_event': future_event,
        'today_event': today_event
    }

    return render(request, 'account/account_main.html', context)
    pass


class UserUpdateView(UpdateView):
    model = User
    template_name = 'events/changeEvent.html'
    fields = ['first_name', 'email']

    def get(self, request, **kwargs):
        self.object = User.objects.get(username=self.request.user)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(redirect_to='/account')

    def get_object(self, queryset=None):
        return self.request.user
