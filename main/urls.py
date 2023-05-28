from django.urls import path
from .views import IndexView,AdSite
app_name = 'main'
urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('adsite/', AdSite.as_view(), name='adsite')
]
