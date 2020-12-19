from django import forms
from .models import EventInfo
from .widgets import CustomClearableFileInput

class EventsForm(forms.ModelForm):

    class Meta:
        model = EventInfo
        fields = '__all__'

    image = forms.ImageField(label="Ereignisbild", required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        event = EventInfo.objects.all()