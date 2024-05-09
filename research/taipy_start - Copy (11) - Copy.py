#© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
import tempfile
import folium
from folium.folium import Map
import pandas as pd
from taipy.gui import Gui, Markdown

def expose_folium(fol_map: Map):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as temp_file:
        fol_map.save(temp_file.name)
        with open(temp_file.name, "rb") as f:
            html_content = f.read()
    return Markdown(f"<iframe srcdoc='{html_content.decode()}' width='100%' height='600px'></iframe>")

def load_data():
    # Load country data from GeoJSON file
    countries_url = "http://geojson.xyz/naturalearth-3.3.0/ne_50m_admin_0_countries.geojson"
    countries_data = folium.GeoJson(countries_url, name='Countries')
    
    # Load population data from CSV file
    population_data = pd.read_csv("population_data.csv")
    
    return countries_data, population_data

def create_folium_map(countries_data, population_data):
    # Create the Folium map centered on a specific location
    fol_map = folium.Map(location=[20, 0], zoom_start=2, tiles="cartodb positron")
    
    # Add choropleth layer to visualize population data
    folium.Choropleth(
        geo_data=countries_data,
        name='Population',
        data=population_data,
        columns=['Country', 'Population'],
        key_on='feature.properties.name',
        fill_color='YlOrRd',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Population'
    ).add_to(fol_map)
    
    # Add layer control to toggle visibility of layers
    folium.LayerControl().add_to(fol_map)
    
    return fol_map

def folium_map():
    countries_data, population_data = load_data()
    fol_map = create_folium_map(countries_data, population_data)
    return fol_map

Gui.register_content_provider(Map, expose_folium)

page = """
# Population Visualization with Folium Map

This application demonstrates the integration of a Folium map as a third-party component in Taipy.

The map visualizes population data for countries around the world using a choropleth layer. 
You can interact with the map, zoom in/out, and toggle the visibility of layers using the layer control.

<|{folium_map()}|>
"""

Gui(page).run(port=5000)
