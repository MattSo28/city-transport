from django.shortcuts import render, redirect
import osmnx as ox
import os
import re
import matplotlib
from django.conf import settings

# Create your views here.

def get_geocode_city_name(input_city_text):
    """
    Take in an input text and return the geocoded result
    """
    city_name = None

    geocoded_city_data = ox.geocoder.geocode_to_gdf(input_city_text)

    if not geocoded_city_data.empty:
        city_name = geocoded_city_data.iloc[0]['display_name']
        return city_name
    else:
        return None

def generate_filename(geocode_result):
    # Sanitize the geocode result to create a valid filename
    sanitized_name = re.sub(r'[^a-zA-Z0-9]+', '_', geocode_result).lower()
    return f"{sanitized_name}_street_network"
    
def generate_map(city_name):
    """
    Given a geocoded city name, generate a map of the roads within the city boundaries
    """
    # Use the 'Agg' backend for non-interactive plot generation
    matplotlib.use('Agg')

    graph = ox.graph_from_place(city_name, network_type='all', simplify=True)

    #Plot the street network
    fig, ax = ox.plot_graph(
        graph, 
        node_size=0, 
        bgcolor='white', 
        edge_color='black', 
        edge_linewidth=0.1,  # Set thin line width
        figsize=(10, 10),  # Set a larger figure size
        show=False, 
        close=False
    )

    # Get the absolute path to the 'poc/static/maps' directory
    current_script_path = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.join(current_script_path, 'static')
    os.makedirs(output_folder, exist_ok=True)

    #Define the filepath
    svg_file_name = generate_filename(city_name) + ".svg"

    # Define the filepath inside maps/static directory
    static_dir = os.path.join(settings.BASE_DIR, 'maps', 'static')
    os.makedirs(static_dir, exist_ok=True)
    svg_file_path = os.path.join(static_dir, svg_file_name)

    # Save the plot as an SVG file
    fig.savefig(svg_file_path, format='svg')

    return svg_file_path

def view_map(request, geocoded_city_name):
    svg_file_path = generate_map(geocoded_city_name)
    static_svg_url = os.path.join(settings.STATIC_URL, os.path.basename(svg_file_path))
    city_name = geocoded_city_name  # Pass the city_name to the template if needed
    return render(request, 'mapview.html', {'city_name': city_name, 'svg_url': static_svg_url})