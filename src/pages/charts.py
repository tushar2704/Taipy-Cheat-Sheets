##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
from taipy.gui import Markdown, Gui


# charts.py
def create_charts_page():
    return """
## Charts

Learn how to create various types of charts using Taipy.
<|{data}|chart|type=bar|x=Country|y=Population|>
"""

# Sample data for the chart
data = [
    {"Country": "USA", "Population": 331002651},
    {"Country": "China", "Population": 1439323776},
    {"Country": "India", "Population": 1380004385},
]
