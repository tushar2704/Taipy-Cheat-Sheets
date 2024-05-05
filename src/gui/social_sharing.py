##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
from taipy.gui import Markdown, Icon, Button

def share_on_twitter(page):
    # TODO: Implement logic to share on Twitter
    pass

def share_on_facebook(page):
    # TODO: Implement logic to share on Facebook
    pass

def share_on_linkedin(page):
    # TODO: Implement logic to share on LinkedIn
    pass

def get_social_sharing_buttons(page):
    return f"""
    <|Button|label=Icon("twitter")|on_action=share_on_twitter|>
    <|Button|label=Icon("facebook")|on_action=share_on_facebook|>
    <|Button|label=Icon("linkedin")|on_action=share_on_linkedin|>
    """