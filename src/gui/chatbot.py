##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
from taipy.gui import Markdown, Input, Button

def get_chatbot_response(state, query):
    # TODO: Implement logic to generate chatbot response based on the query
    response = "I'm sorry, I don't have an answer for that yet. Please try asking something else."
    state.chatbot_history.append(("user", query))
    state.chatbot_history.append(("bot", response))
    state.chatbot_query = ""

def render_chatbot_history(state):
    history = ""
    for sender, message in state.chatbot_history:
        if sender == "user":
            history += f"<p><strong>You:</strong> {message}</p>"
        else:
            history += f"<p><strong>Chatbot:</strong> {message}</p>"
    return history

chatbot_component = """
<style>
.chatbot {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f0f0f0;
    border-radius: 5px;
}
.chatbot-history {
    max-height: 300px;
    overflow-y: auto;
    margin-bottom: 20px;
}
</style>

<div class="chatbot">
    <h2>Taipy Cheatsheets Chatbot</h2>
    
    <div class="chatbot-history">
        <|{render_chatbot_history(state)}|>
    </div>
    
    <|Input|label=Ask a question|value={chatbot_query}|>
    <|Button|label=Send|on_action=get_chatbot_response|>
</div>
"""