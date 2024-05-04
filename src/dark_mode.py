##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
from taipy.gui import Markdown, Switch

def toggle_dark_mode(state):
    state.dark_mode = not state.dark_mode

dark_mode_toggle = """
<|Switch|label=Dark Mode|value={dark_mode}|on_change=toggle_dark_mode|>
"""