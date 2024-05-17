##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################

import os, sys, requests, logging, pathlib
import taipy as tp
from taipy import Config, Gui, Scenario
from taipy.gui import Gui, Icon, navigate
import taipy.gui.builder as tgb
import taipy.core as tc
import taipy.gui_core as tgc
import taipy.config as tpc
import taipy.gui.data as tgd
from taipy.gui import Markdown


# from src.pages.getting_started import getting_started_md
# #######################################################################################################

# # custom theme
# my_theme = {
#     "palette": {
#         "background": {"default": "#E7E8D1"},  
#         "text": {"primary": "#2A2F33"}, 
#         "primary": {"main": "#2A2F33"},  
#         "secondary": {"main": "#2A2F33"},  
#         "link": {"main": "#2A2F33"},  #       
#     }
# }



# root_md = Markdown("""
# # Welcome to Taipy Cheat Sheets
# <|navbar|>
# This is the home page of the Taipy Cheat Sheets application. Use the navigation to explore different features and guides.

# ## Available Pages

# - [Getting Started](#/getting_started)
# - [Taipy Core](#/taipy_core)
# - [Taipy GUI](#/taipy_gui)
# - [Taipy REST](#/taipy_rest)
# - [Taipy Enterprise](#/taipy_enterprise)
# - [Deployment](#/deployment)
# - [Best Practices](#/best_practices)
# - [Integrations](#/integrations)
# - [User Examples](#/user_examples)
# - [Related Resources](#/related_resources)
# """)













































# pages = {"/": root_md,
#     "Getting Started": getting_started_md}


# # Run the application
# Gui(pages=pages).run(debug=True,use_reloader=True)










#######################################################################################################
#Running all the Pages 
#######################################################################################################







#######################################################################################################
#Application run
#######################################################################################################


# main.py
from taipy import Gui
from taipy.gui import navigate
from src.pages.charts import create_charts_page
from src.pages.datatables import create_datatables_page
from src.pages.forms import create_forms_page
from src.pages.navigation import create_navigation_page
from src.pages.themes import create_themes_page

# Custom theme
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

# Features
features = [
    {"name": "Charts", "page": create_charts_page()},
    {"name": "DataTables", "page": create_datatables_page()},
    {"name": "Forms", "page": create_forms_page()},
    {"name": "Navigation", "page": create_navigation_page()},
    {"name": "Themes", "page": create_themes_page()},
]

# Root page with navbar and menu
root_md = """
<|navbar|>
# [Taipy Cheat Sheets](https://github.com/tushar2704/Taipy-Cheat-Sheets)

### by [Tushar Aggarwal](https://www.linkedin.com/in/tusharaggarwalinseec/)

<|menu|label=Features|lov={[c['name'] for c in features]}|on_action=on_menu|>

# Taipy Features
Welcome to the Taipy Cheat Sheets application! Use the menu on the left to select a feature and view its details.
"""

# Callback for menu selection
def on_menu(state, action, info):
    feature_name = info["args"][0]
    feature = next(c for c in features if c['name'] == feature_name)
    page_name = feature_name.replace(" ", "_")  # Replace spaces with underscores
    navigate(state, to=page_name)

# Create the pages dictionary
pages = {"/": root_md}
for feature in features:
    page_name = feature["name"].replace(" ", "_")
    pages[page_name] = feature["page"]

# Run the application
Gui(pages=pages).run(debug=True, use_reloader=True)
