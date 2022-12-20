from django import forms
from .models import SpielTabelle

class GameTableForm(forms.ModelForm):

    class Meta:
        model = SpielTabelle
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        product = SpielTabelle.objects.all()