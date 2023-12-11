from django import forms

from events.models import Event


class AddEvent(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['creator_id'].initial = 1

    class Meta:
        model = Event
        fields = ['date', 'anons', 'title', 'source', 'typeOfEvent', 'image', 'category']
        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'date-input'}),
            'anons': forms.Textarea(attrs={'class': 'textarea-input', 'cols': 50, 'rows': 10}),
            'title': forms.TextInput(attrs={'class': 'text-input'}),
            'source': forms.TextInput(attrs={'class': 'text-input'}),
            'typeOfEvent': forms.Select(),
            'image': forms.FileInput(),
            # 'creator_id': forms.Select()
        }
