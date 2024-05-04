##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
from taipy.gui import Markdown, Icon, Button

def rate_page(state, page, rating):
    # TODO: Implement logic to store page ratings (e.g., in a database)
    state.page_ratings[page] = rating

def get_rating_buttons(page):
    return [
        Button(
            label=Icon("star"),
            on_action=rate_page,
            active=state.page_ratings.get(page, 0) >= i,
        )
        for i in range(1, 6)
    ]