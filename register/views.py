

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegisterForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True  # Activate the user
            user.save()
            return redirect("home")  # Redirect to the home page after successful registration
    else:
        form = RegisterForm()
    return render(request, "register/register.html", {"form": form})

