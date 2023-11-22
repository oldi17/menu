from django.urls import path

from .views import Home

app_name = 'menu'

urlpatterns = [
    path('menu/', Home.as_view(), name='index')
]