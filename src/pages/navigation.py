##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
from taipy.gui import Markdown, Gui, Dropdown

def create_navigation_page():
    return """
## Navigation

Get to know the navigation features in Taipy.
<|menu|label=Navigation|lov={['Home', 'About', 'Contact']}|on_action=navigate|>
"""

def navigate(state, action, info):
    print(f"Navigating to: {info['args'][0]}")
