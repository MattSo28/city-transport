from django.urls import path
from . import views

app_name = 'core'  # Namespace for the core app

urlpatterns = [
    path('', views.home, name='home'),
]