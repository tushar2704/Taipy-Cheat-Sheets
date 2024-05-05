##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
from taipy.gui import Markdown, Input, Textarea, Button

def submit_comment(state, page, comment):
    # TODO: Implement logic to store comments (e.g., in a database)
    state.comments[page].append(comment)
    state.comment_text = ""

def get_comments_section(page):
    return f"""
    ## Comments

    {''.join(f"- {comment}\n" for comment in state.comments.get(page, []))}

    <|Textarea|label=Leave a comment|value={{comment_text}}|>
    <|Button|label=Submit|on_action=submit_comment|>
    """