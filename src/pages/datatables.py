##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
from taipy.gui import Markdown, Gui

def create_datatables_page():
    return """
## DataTables

Understand how to use DataTables for displaying tabular data.
<|{data}|table|>
"""

# Sample data for the table
data = [
    {"Name": "Alice", "Age": 30, "Country": "USA"},
    {"Name": "Bob", "Age": 25, "Country": "UK"},
    {"Name": "Charlie", "Age": 35, "Country": "Canada"},
]