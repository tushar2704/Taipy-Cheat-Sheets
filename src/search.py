##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
from taipy.gui import Markdown, Input, Button

def search_content(state, query):
    # TODO: Implement search logic to find relevant content based on the query
    results = []
    state.search_results = Markdown("\n".join(results))

search_page = """
# Search Taipy Cheatsheets

<|Input|label=Search|on_change=search_content|>

<|Button|label=Search|on_action=search_content|>

<|{search_results}|>
"""