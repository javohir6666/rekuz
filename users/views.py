from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from django.shortcuts import get_object_or_404
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here..
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:home')
            # if not user.first_name:
            #     messages.info(request,"Please enter your information")
            #     return redirect("users:profile", username)
                
                
            return redirect("index")
        else:
            return messages.error("Username or password is incorrect")

    return render(request, 'users/login.html')


def logOut(request):
    logout(request)
    return redirect('users:login')