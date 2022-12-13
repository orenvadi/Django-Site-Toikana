from django import forms


class MyForm(forms.Form):
    date = forms.DateField(input_formats=["%Y-%m-%d"])
