from django import forms
from .models import Twit, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 


class TwitForm(forms.ModelForm):
    class Meta:
        model = Twit    
        fields = ['content', 'image']
        

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Tell us about yourself...'}),
            'profile_picture': forms.ImageField( required=False),
        }


