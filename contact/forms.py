from django import forms
from .widgets import CustomClearableFileInput
from .models import ContactInfo


class ContactInfoForm(forms.ModelForm):

    class Meta:
        model = ContactInfo
        fields = '__all__'

    image = forms.ImageField(label='Bild', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        product = ContactInfo.objects.all()