from django import forms
from .widgets import CustomClearableFileInput
from .models import firstGalleryPageTitle, firstGalleryPictures, secondGalleryPictures, thirdGalleryPictures

class firstGalleryImgForm(forms.ModelForm):

    class Meta:
        model = firstGalleryPictures
        fields = '__all__'

    image_column_1 = forms.ImageField(label="Erstest Bild in der Reihe:", required=False, widget=CustomClearableFileInput)
    image_column_2 = forms.ImageField(label="Zweites Bild in der Reihe:", required=False, widget=CustomClearableFileInput)
    image_column_3 = forms.ImageField(label="Drittes Bild in der Reihe:", required=False, widget=CustomClearableFileInput)
    image_column_4 = forms.ImageField(label="Viertes Bild in der Reihe:", required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        first_gallery_img = firstGalleryPictures.objects.all()

class firstGalleryTitleForm(forms.ModelForm):
    class Meta:
        model = firstGalleryPageTitle
        fields = '__all__'

    page_image = forms.ImageField(label="Bild", required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        first_gallery_title = firstGalleryPageTitle.objects.all()


class secondGalleryImgForm(forms.ModelForm):

    class Meta:
        model = secondGalleryPictures
        fields = '__all__'

    image_column_1 = forms.ImageField(label="Erstest Bild in der Reihe:", required=False, widget=CustomClearableFileInput)
    image_column_2 = forms.ImageField(label="Zweites Bild in der Reihe:", required=False, widget=CustomClearableFileInput)
    image_column_3 = forms.ImageField(label="Drittes Bild in der Reihe:", required=False, widget=CustomClearableFileInput)
    image_column_4 = forms.ImageField(label="Viertes Bild in der Reihe:", required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        second_gallery_img = secondGalleryPictures.objects.all()


class thirdGalleryImgForm(forms.ModelForm):

    class Meta:
        model = thirdGalleryPictures
        fields = '__all__'

    image_column_1 = forms.ImageField(label="Erstest Bild in der Reihe:", required=False, widget=CustomClearableFileInput)
    image_column_2 = forms.ImageField(label="Zweites Bild in der Reihe:", required=False, widget=CustomClearableFileInput)
    image_column_3 = forms.ImageField(label="Drittes Bild in der Reihe:", required=False, widget=CustomClearableFileInput)
    image_column_4 = forms.ImageField(label="Viertes Bild in der Reihe:", required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        third_gallery_img = thirdGalleryPictures.objects.all()