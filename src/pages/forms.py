##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
from taipy.gui import Markdown, Gui, Dropdown

def create_forms_page():
    return """
## Forms

Explore how to create and manage forms in Taipy.
<|{name}|input|label=Name|>
<|{age}|input|label=Age|type=number|>
<|Submit|button|on_action=submit_form|>
"""

def submit_form(state):
    print(f"Name: {state.name}, Age: {state.age}")
