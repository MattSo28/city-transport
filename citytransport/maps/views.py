from django.shortcuts import render, redirect
import osmnx as ox
import os

# Create your views here.
def get_geocode_city_name(input_city_text):

    city_name = None

    geocoded_city_data = ox.geocoder.geocode_to_gdf(input_city_text)

    if not geocoded_city_data.empty:
        city_name = geocoded_city_data.iloc[0]['display_name']
        
        return city_name

    else:
        return None
    
