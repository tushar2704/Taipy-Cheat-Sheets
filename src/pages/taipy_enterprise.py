##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
from taipy.gui import Markdown, Gui, Dropdown

page = """
# Taipy Enterprise

Taipy Enterprise provides additional features for building production-ready applications.

<|Dropdown|label=User Management Code|>
"""
from taipy.enterprise import create_user

create_user(
    username="john", 
    password="secret",
    email="john@example.com",
    roles=["admin"]
)