from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import HttpResponse

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def register(request):
    if request.method == "GET":
        form = CustomUserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            print("Form is not valid")
            return HttpResponse('Проверьте введенную информацию и попробуйте еще раз ')

    return render(request, "registration/signup.html", {})
