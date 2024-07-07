from django.urls import path
from . import views

urlpatterns = [
    path('map/<str:geocoded_city_name>/', views.view_map, name='view_map'),
]