from django import forms
from .models import *

class Newtopicform(forms.ModelForm):
    message=forms.CharField(widget=forms.
    Textarea(attrs={'placeholder':'What is on your mind?'}))
    class Meta:
        model=Topic
        fields=['subject','message']

    