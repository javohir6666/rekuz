from django.urls import path
from . import views
app_name = 'users'
urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logOut, name="logout"),
    path('signup_save/', views.signup_save, name='signup_save')
]
