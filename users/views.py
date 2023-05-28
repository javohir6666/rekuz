from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from django.shortcuts import get_object_or_404
from .models import CustomUser, USER_TYPE
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here..
def loginPage(request):
    user_type = USER_TYPE
    context = {
        'user_type':user_type
    }
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
                
        else:
            return messages.error("Username or password is incorrect")

    return render(request, 'users/login.html', context)


def logOut(request):
    logout(request)
    return redirect('users:login')


def signup_save(request):
    if request.method != "POST": 
        return HttpResponse("Method not allowed")
    else:
        user_type = request.POST.get("user_type")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        telegram = request.POST.get("telegram")
        if password != password2:
            return messages.error("the password is not match!")
        else:
            try:
                user = CustomUser.objects.create_user(
                username=username,
                password=password,
                email=email,
                user_type = user_type,
                telegram = telegram
            )
                user.save()
                messages.success(request, "Registration successfully. You can login now!")
                return redirect(request.META.get("HTTP_REFERER"))
            except:
                messages.error(request, "Failed to Register")
                return redirect(request.META.get("HTTP_REFERER"))
        