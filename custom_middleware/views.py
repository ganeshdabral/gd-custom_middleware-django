from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm

def login_view(request):
    form = UserForm(request.POST or None)
    context = {
        "form": form
    }
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user_obj = authenticate(request, username=username, password=password)
            if user_obj:
                login(request, user_obj)
                return redirect("profile")
            else:
                messages.info(request, "Invalid credential")
        else:
            messages.error(request, form.errors)
    return render(request, "account/login.html", context)

def my_account(request):
    return render(request, "account/profile.html", {})
def logout_view(request):
    logout(request)
    return redirect("login")