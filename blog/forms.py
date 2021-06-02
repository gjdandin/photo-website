from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django_resized import ResizedImageField

# class ProfileForm(ModelForm):
#     class Meta:
#         model = Profile
#         fields = '__all__'
#         exclude = ['user']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(ImageForm, self).__init__(*args, **kwargs)



    def save(self, commit=True):
        inst = super(ImageForm, self).save(commit=False)
        inst.user = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst

class EditImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'body', 'image', 'id', 'album')

class ContactForm(forms.Form):
    name = forms.CharField(max_length = 50)
    email = forms.EmailField(max_length = 150)
    message = forms.CharField(widget = forms.Textarea, max_length = 2000)
