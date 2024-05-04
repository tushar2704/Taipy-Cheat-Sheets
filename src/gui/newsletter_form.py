##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
from taipy.gui import Markdown, Input, Button

def subscribe_to_newsletter(state, email):
    # TODO: Implement logic to subscribe to the newsletter (e.g., add to mailing list)
    state.newsletter_email = ""
    state.newsletter_subscribed = True

newsletter_form = """
## Subscribe to Our Newsletter

Stay up to date with the latest Taipy news and updates!

<|Input|label=Email|value={newsletter_email}|>
<|Button|label=Subscribe|on_action=subscribe_to_newsletter|>

<|{newsletter_subscribed}|>
"""