from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _

class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Entfernen')
    initial_text = _('Aktuelles Bild')
    input_text = _('')
    template_name = 'news/custom_widget_templates/custom_clearable_file_input.html'