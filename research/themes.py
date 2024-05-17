##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
from taipy.gui import Markdown, Gui, Dropdown

def create_themes_page():
    return """
## Themes

Customize the look and feel of your Taipy application with themes.
<|theme_selector|selector|lov={['Light', 'Dark']}|on_change=change_theme|>
"""

def change_theme(state, action, info):
    print(f"Theme changed to: {info['args'][0]}")
