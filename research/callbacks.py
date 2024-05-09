#© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
from taipy.gui import Gui, Markdown, notify

my_theme = {
    "palette": {
        "background": {"default": "#E7E8D1"},  
        "text": {"primary": "#2A2F33"}, 
        "primary": {"main": "#2A2F33"},  
        "secondary": {"main": "#2A2F33"},  
        "link": {"main": "#2A2F33"},  #       
    }
}

# Global variables
temperature_c = 25
temperature_f = None
temperature_k = None
message = ""

# Utility functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Callbacks
def update_temperatures(state):
    state.temperature_f = celsius_to_fahrenheit(state.temperature_c)
    state.temperature_k = celsius_to_kelvin(state.temperature_c)

def show_message(state):
    notify(state, "info", f"You entered: {state.message}")

def on_change(state, var_name, var_value):
    if var_name == "temperature_c":
        update_temperatures(state)

# Markdown string
md = """
# [Taipy Cheat Sheets](https://github.com/tushar2704/Taipy-Cheat-Sheets)

### by [Tushar Aggarwal](https://www.linkedin.com/in/tusharaggarwalinseec/)

# 🌡️ All about Callbacks in Taipy

## 1. Local Callback Example

Adjust the Celsius temperature and see the Fahrenheit and Kelvin values update automatically:

**Celsius:** <|{temperature_c}|slider|min=0|max=100|step=1|on_change=update_temperatures|>

**Fahrenheit:** <|{temperature_f}|>

**Kelvin:** <|{temperature_k}|>

## 2. Global Callback Example

Enter a message and click the button to trigger a global callback:

**Message:** <|{message}|input|>

<|Show Message|button|on_action=show_message|>

## 3. Callback Types

Taipy supports various types of callbacks:

- `on_change`: Triggered when a variable's value changes
- `on_action`: Triggered by user actions (e.g., button click)
- `on_init`: Called when the application starts
- `on_navigate`: Called when navigating between pages
- `on_exception`: Called when an exception occurs

Explore the code to see how these callbacks are used!
"""

# Run the application
Gui(page=Markdown(md)).run(debug=True,use_reloader=True, theme=my_theme)
