from IPython.core.display import HTML
from IPython.display import IFrame
from folium import Map, CircleMarker, GeoJson
from folium import Marker
import folium
import random
from folium import Map, CircleMarker, TileLayer, Popup
import os
import glob
import pandas as pd
import requests
import numpy as np
import streamlit.components.v1 as components

def World_Map_LAT_LON(LoN, LaT, Disagre):
    latitudes = LoN
    longitudes = LaT
    Magnitudes = LaT
    Locations = LoN
    Date = Disagre

    maxMagn = max(Magnitudes)

    # Define the size and color of each circle, based on some variable
    sizes = []
    for i in range(len(Magnitudes)):
        sizes.append(Magnitudes[i]*15/maxMagn)
    colors = [f"#{random.randint(0, 0xFFFFFF):06x}" for _ in range(len(latitudes))]

    # Combine the latitude, longitude, size, and color into a list of tuples
    locations = list(zip(latitudes, longitudes))
    radii = sizes

    # Create the map
    # "OpenStreetMap"  # "Stamen Terrain"  # "Stamen Toner"  # "Stamen Watercolor"  # "CartoDB positron"  # "CartoDB dark_matter" **
    map = Map(location=[-0.201858 - 2, (-78.480166)], zoom_start=6, width='100%', height='100%', zoom_control=True)
    # TileLayer('CartoDB positron').add_to(map)
    TileLayer('CartoDB positron', opacity=1).add_to(map)

    # Add a circle for each point
    for i in range(len(locations)):
        Marker(location=locations[i], tooltip= f'LAT = {latitudes}, LON = {longitudes}').add_to(map)
        Popup(f"Magnitude: {Magnitudes[i]}").add_to(Marker(location=locations[i]))

    # Add tectonic plates GeoJSON layer
    tectonic_plates = GeoJson("https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json",
        name='Tectonic Plates',
        style_function=lambda x: {'color': 'blue', 'weight': 0.8, 'opacity': 0.5}
    ).add_to(map)
    

    # Create custom legend
    legend_html = """
    <div style="position: fixed; 
        bottom: -250px; rigth: 50px; width: 4000px; height: 300px; 
        border:0px solid grey; z-index:9999; font-size:14px;
        background-color: ;
        ">
        <p style="text-align:left; font-size:16px; font-weight:bold">Selected Location</p>
        <table style="width:25%; height: 25%; box: none;">
        """ 
    legend_html += """
        </table>
    </div>
    """

    ############################### Add latitude and longitude grid layers ############################################
    # Add latitude and longitude grid layers
    grid_layer_lat = folium.FeatureGroup(name='Latitudes', show=False, overlay=True)
    grid_layer_lon = folium.FeatureGroup(name='Longitudes', show=False, overlay=True)
    grid_spacing = 25 # Grid spacing in degrees

    # Add latitude grid layer
    for lat in range(-90, 91, grid_spacing):
        grid_layer_lat.add_child(folium.PolyLine([(lat, -180), (lat, 180)], color='black', weight=0.5, opacity=0.3, dash_array='2'))

    # Add longitude grid layer
    for lon in range(-180, 181, grid_spacing):
        grid_layer_lon.add_child(folium.PolyLine([(-90, lon), (90, lon)], color='black', weight=0.5, opacity=0.3, dash_array='2'))

    # Add grid layers to the map
    map.add_child(grid_layer_lat)
    map.add_child(grid_layer_lon)


    map.get_root().html.add_child(folium.Element(legend_html))

   
    # Save the map as an HTML string
    map_html = map._repr_html_()

    # Display the map in Streamlit
    components.html(map_html, width=700, height=400)
   
   
   
    longitudes = np.vstack((longitudes))
    latitudes = np.vstack((latitudes))
    Locations = np.array(Locations)
    Date = np.array(Date)
    
    return map, latitudes, longitudes, Locations, Date