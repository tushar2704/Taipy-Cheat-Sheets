##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
from taipy.gui import Markdown, Gui, Dropdown

page = """
# Taipy GUI

Taipy GUI allows you to create interactive web interfaces for your Taipy applications.

<|Dropdown|label=Layout Code|>
"""
from taipy.gui import Gui, Markdown, Button

page = """
<|layout|columns=2 1|
<|
# Left Column
|>

<|
# Right Column
<|Button|label=Click Me|on_action=button_clicked|>
|>
|>
"""

def button_clicked(state):
    print("Button clicked!")

Gui(page=Markdown(page)).run()