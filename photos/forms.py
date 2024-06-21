from django.forms import ModelForm
from .models import Photo

class addPhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'
