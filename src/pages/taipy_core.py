##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
from taipy.gui import Markdown, Gui, Dropdown

page = """
# Taipy Core

Taipy Core provides the building blocks for creating data-driven applications.

<|Dropdown|label=Scenario Code|>
"""
from taipy import Scenario

scenario = Scenario(
    id="my_scenario",
    pipelines=[pipeline1, pipeline2],
    frequency="D",
    start_date="2023-01-01"
)