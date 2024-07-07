from django.shortcuts import render, redirect
import osmnx as ox
import os
import re

# Create your views here.

#rename filename
def generate_filename(geocode_result):
    # Sanitize the geocode result to create a valid filename
    sanitized_name = re.sub(r'[^a-zA-Z0-9]+', '_', geocode_result).lower()
    return f"{sanitized_name}_street_network"

def get_geocode_city_name(input_city_text):

    city_name = None

    geocoded_city_data = ox.geocoder.geocode_to_gdf(input_city_text)

    if not geocoded_city_data.empty:
        city_name = geocoded_city_data.iloc[0]['display_name']
        return city_name
    else:
        return None
    
def generate_map(city_name):
    """
    Given a geocoded city name, generate a map of the roads within the city boundaries
    """
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
    svg_file_path = os.path.join(output_folder, generate_filename(city_name) + ".svg")

    # Save the plot as an SVG file
    fig.savefig(svg_file_path, format='svg')

    return render(request, 'mapview.html', {'city_name': city_name})


