from django import forms

from events.models import Event


class AddEvent(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
