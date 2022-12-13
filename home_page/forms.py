from django import forms

# from . import models
from .models import Review


class AddReview(forms.ModelForm):
    class Meta(forms.ModelForm):
        model = Review
        fields = ("name", "description", "email")

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
        }
