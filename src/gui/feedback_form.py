##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
from taipy.gui import Markdown, Input, Textarea, Button

def submit_feedback(state):
    # TODO: Implement logic to submit feedback (e.g., send email, store in database)
    state.feedback_name = ""
    state.feedback_email = ""
    state.feedback_message = ""
    state.feedback_submitted = True

feedback_form = """
# Feedback

We value your feedback! Please let us know your thoughts or suggestions.

<|Input|label=Name|value={feedback_name}|>
<|Input|label=Email|value={feedback_email}|>
<|Textarea|label=Message|value={feedback_message}|>

<|Button|label=Submit|on_action=submit_feedback|>

<|{feedback_submitted}|>
"""