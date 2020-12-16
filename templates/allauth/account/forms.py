from django import forms
from django.utils.translation import gettext as _

class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        login_widget = forms.TextInput(
                attrs={"placeholder": _("Username"), "autocomplete": "username"}
            )
        self.fields['login'].widget = self.fields['Anmelden']

    
