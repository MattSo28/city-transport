from django.urls import path
from . import views

urlpatterns = [
    path('mapview/', views.view_map,name='viewmap'),
]