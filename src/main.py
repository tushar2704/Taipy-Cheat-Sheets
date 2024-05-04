##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
import os
from taipy.gui import Gui, Markdown
from taipy.gui import Gui, navigate
from src.gui.navigation import get_navigation
from src.gui.navigation import get_navigation
from src.gui.code_editor import get_code_editor
from src.gui.feedback_form import feedback_form
from src.gui.favorites import get_favorite_button
from src.gui.rating import get_rating_buttons
from src.gui.comments import get_comments_section
from src.gui.social_sharing import get_social_sharing_buttons
from src.gui.newsletter_form import newsletter_form
from src.gui.chatbot import chatbot_component
from src.pages import (
    getting_started,
    taipy_core,
    taipy_gui,
    taipy_rest,
    taipy_enterprise,
    deployment,
    best_practices,
    integrations,
    user_examples,
    related_resources,
)
from src.search import search_page
from src.dark_mode import dark_mode_toggle
from src.auth.authentication import login_form, logout_button
#######################################################################################################
#Pages
#######################################################################################################
def on_page_change(state, var_name, function_name, info):
    page = info['args']
    navigate(state, to=page)
def get_page_content(page):
    return f"""
<|layout|columns=1 1|
<|
{page}
|>

<|
{get_code_editor(page)}
|>

<|
{get_favorite_button(page)}
{''.join(get_rating_buttons(page))}
|>

<|
{get_comments_section(page)}
|>

<|
{get_social_sharing_buttons(page)}
|>
|>
"""


























































#######################################################################################################
#Running all the Pages 
#######################################################################################################


pages = {
    "/": get_page_content(getting_started.page),
    "/getting-started": get_page_content(getting_started.page),
    "/taipy-core": get_page_content(taipy_core.page),
    "/taipy-gui": get_page_content(taipy_gui.page),
    "/taipy-rest": get_page_content(taipy_rest.page),
    "/taipy-enterprise": get_page_content(taipy_enterprise.page),
    "/deployment": get_page_content(deployment.page),
    "/best-practices": get_page_content(best_practices.page),
    "/integrations": get_page_content(integrations.page),
    "/user-examples": get_page_content(user_examples.page),
    "/related-resources": get_page_content(related_resources.page),
    "/search": search_page,
    "/feedback": feedback_form,
    "/login": login_form,
    "/newsletter": newsletter_form,
    "/chatbot": chatbot_component,
}

# def get_header(state):
#     if state.is_authenticated:
#         return f"""
#         <|layout|columns=1 1|
#         <|
#         Welcome, {state.user}!
#         {logout_button}
#         |>
#         |>
#         """
#     else:
#         return ""





#######################################################################################################
#Application run
#######################################################################################################

Gui(
    pages=pages,
    nav=get_navigation(),
    dark_mode=dark_mode_toggle,
    header=get_header,
    on_page_change=on_page_change,
).run()