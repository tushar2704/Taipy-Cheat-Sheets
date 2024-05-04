##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
from taipy.gui import Markdown, Icon, Button

def toggle_favorite(state, page):
    if page in state.favorites:
        state.favorites.remove(page)
    else:
        state.favorites.append(page)

def get_favorite_button(page):
    return Button(
        label=Icon("star"),
        on_action=toggle_favorite,
        active=page in state.favorites,
    )