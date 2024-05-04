##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
import os
from taipy.gui import Gui, Markdown
from .gui.navigation import get_navigation
from .gui.code_editor import get_code_editor
from .gui.feedback_form import feedback_form
from src.pages import (
    getting_started,
    taipy_core,
    taipy_gui,
    taipy_rest,
    taipy_enterprise,
    deployment,
    best_practices,
    integrations,
)
from src.search import search_page
from src.dark_mode import dark_mode_toggle
#######################################################################################################
#Pages
#######################################################################################################
def get_page_content(page):
    return f"""
<|layout|columns=1 1|
<|
{page}
|>

<|
{get_code_editor(page)}
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
    "/search": search_page,
    "/feedback": feedback_form,
}








#######################################################################################################
#Application run
#######################################################################################################
Gui(
    pages=pages,
    nav=get_navigation(),
    dark_mode=dark_mode_toggle,
).run()