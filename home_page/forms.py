from django import forms

# from . import models
from .models import Booking, Review


class AddReview(forms.ModelForm):
    class Meta(forms.ModelForm):
        model = Review
        fields = ("name", "description", "email")

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
        }


class AddBooking(forms.ModelForm):
    class Meta(forms.ModelForm):
        BRANCHES_CHOICES = [
            ("Асанбай", "Асанбай"),
            ("Белый Аист", "Белый Аист"),
            ("Токтогула", "Токтогула"),
            ("Шопокова", "Шопокова"),
        ]
        model = Booking
        fields = ("name", "phone", "date", "guests", "branch")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "date": forms.DateInput(format="%m.%d.%Y", attrs={"type": "date"}),
            "guests": forms.NumberInput(),
            # "branch": forms.ChoiceField(
            #     choices=BRANCHES_CHOICES,
            # ),
        }
