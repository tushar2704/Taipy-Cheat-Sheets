##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
from taipy.gui import Markdown, Gui, Dropdown

page = """
# Taipy REST

Taipy REST allows you to expose your Taipy scenarios as RESTful APIs.

<|Dropdown|label=Endpoint Code|>
""" 
from taipy.rest import Rest, endpoint

@endpoint(path="/hello", methods=["GET"])
def hello():
    return {"message": "Hello, World!"}

rest = Rest()
rest.run()