#© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
from taipy import Gui
from taipy import Gui
from taipy.gui import navigate
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
    {"name": "Charts", "description": "Learn how to create various types of charts using Taipy."},
    {"name": "DataTables", "description": "Understand how to use DataTables for displaying tabular data."},
    {"name": "Forms", "description": "Explore how to create and manage forms in Taipy."},
    {"name": "Navigation", "description": "Get to know the navigation features in Taipy."},
    {"name": "Themes", "description": "Customize the look and feel of your Taipy application with themes."},
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

# Page to display feature details
def create_feature_page(feature):
    return f"""
## {feature['name']}

{feature['description']}
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
    pages[page_name] = create_feature_page(feature)

# Run the application
Gui(pages=pages).run(debug=True, use_reloader=True)