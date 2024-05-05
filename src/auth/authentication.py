##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
from taipy.gui import Markdown, Input, Button

def login(state, username, password):
    # TODO: Implement login logic (e.g., check credentials against database)
    state.user = username
    state.is_authenticated = True

def logout(state):
    state.user = None
    state.is_authenticated = False

login_form = """
# Login

<|Input|label=Username|value={username}|>
<|Input|label=Password|type=password|value={password}|>

<|Button|label=Login|on_action=login|>
"""

logout_button = """
<|Button|label=Logout|on_action=logout|>
"""