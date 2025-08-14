from django import forms
from .models import Twit

class TwitForm(forms.ModelForm):
    class Meta:
        model = Twit    
        fields = ['content', 'image']
        