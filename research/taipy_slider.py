#© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
import taipy as tp
from taipy.gui import Gui, Markdown

# Initial values for sliders
number = 42
values = [20, 40, 80]  # Initial values for the multi-value slider

# custom theme
my_theme = {
    "palette": {
        "background": {"default": "#E7E8D1"},  
        "text": {"primary": "#2A2F33"}, 
        "primary": {"main": "#2A2F33"},  
        "secondary": {"main": "#2A2F33"},  
        "link": {"main": "#2A2F33"},  #       
    }
}

# Define the Markdown content with various sliders
page = Markdown("""
# [Taipy Cheat Sheets](https://github.com/tushar2704/Taipy-Cheat-Sheets)

by [Tushar Aggarwal](https://www.linkedin.com/in/tusharaggarwalinseec/)

# Incremental Number

<|{number}|slider|min=0|max=100|on_change=set_number|>

<|The current number is {number}.|>

# Vertical Incremental Number

<|{number}|slider|min=0|max=100|on_change=set_number|orientation=vert|>

<|The current Vertical number is {number}.|>

# Multi-Value Slider

<|{values}|slider|min=0|max=100|on_change=set_values|>

<|The selected values are {values}.|>
""")

# Callback function to update the single value slider
def set_number(state, var_name, var_value):
    state.number = var_value

# Callback function to update the multi-value slider
def set_values(state, var_name, var_value):
    state.values = var_value

# Create and run the GUI
gui = Gui(page=page)
gui.run(debug=True, use_reloader=True, theme=my_theme)