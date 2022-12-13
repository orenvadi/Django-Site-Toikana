from django import forms
from .models import *
from . import models

class AddReview(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('name','description','email')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),       
            'description': forms.TextInput(attrs={'class': 'form-control'}),           
            'email': forms.TextInput(attrs={'class': 'form-control'}),        
        }
