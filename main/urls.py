from django.urls import path
from . import views
from .views import IndexView
app_name = 'main'
urlpatterns = [
    path('', IndexView.as_view(), name='home')
]
