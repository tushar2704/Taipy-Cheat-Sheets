#© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
from taipy import Gui
from taipy import Gui
from taipy.gui import navigate
# custom theme
my_theme = {
    "palette": {
        "background": {"default": "#E7E8D1"},  
        "text": {"primary": "#112A46"}, 
        "primary": {"main": "#112A46"},  
        "secondary": {"main": "#112A463"},  
        "link": {"main": "#112A46"},
        "info": {"main": "#112A46"},
        "success": {"main": "#112A46"},
        "error": {"main": "#112A46"},
        "warning": {"main": "#112A46"},
    },
    "taipyNavbar": {
        "mainText": "#112A46", 
        "mainBackground": "#E7E8D1", 
    },
    "taipyMenu": {
        "mainText": "#112A46", 
        "mainBackground": "#E7E8D1", 
    },
}

# Define the data for the countries
countries = [
    {"name": "United States", "population": 331002651, "area": 9833520},
    {"name": "China", "population": 1439323776, "area": 9596960},
    {"name": "India", "population": 1380004385, "area": 3287590},
    {"name": "Russia", "population": 145934462, "area": 17098242},
    {"name": "Brazil", "population": 212559417, "area": 8515767},
]

# Root page with navbar and menu
root_md = """
<|navbar|>
# [Taipy Cheat Sheets](https://github.com/tushar2704/Taipy-Cheat-Sheets)

### by [Tushar Aggarwal](https://www.linkedin.com/in/tusharaggarwalinseec/)

<|menu|label=Select Country|lov={[c['name'] for c in countries]}|on_action=on_menu|>

# Country Stats
Welcome to the Country Stats application! Use the menu on the left to select a country and view its statistics.
"""

# Page to display country details
def create_country_page(country):
    return f"""
## {country['name']}

Population: {country['population']:,}
Area: {country['area']:,} sq km
"""

# Callback for menu selection
def on_menu(state, action, info):
    country_name = info["args"][0]
    country = next(c for c in countries if c['name'] == country_name)
    page_name = country_name.replace(" ", "_")  # Replace spaces with underscores
    navigate(state, to=page_name)

# Create the pages dictionary
pages = {"/": root_md}
for country in countries:
    page_name = country["name"].replace(" ", "_")
    pages[page_name] = create_country_page(country)

# Run the application
Gui(pages=pages).run(debug=True,use_reloader=True, theme=my_theme)