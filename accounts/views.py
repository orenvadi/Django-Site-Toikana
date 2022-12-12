from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib import messages

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def register(request):
    if request.method == 'GET':
        form  = CustomUserCreationForm()
        context = {'form': form}
        return render(request, 'registration/signup.html', context)
    if request.method == 'POST':
        form  = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    else:
        print('Form is not valid')
        messages.error(request, 'Error Processing Your Request')
        context = {'form': form}
        return render(request, 'registration/signup.html', context)

    return render(request, 'registration/signup.html', {})