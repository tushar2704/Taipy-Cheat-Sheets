##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################

import os, sys, requests, logging, pathlib
import taipy as tp
from taipy import Config
from taipy.gui import Gui, Icon, navigate
import taipy.gui.builder as tgb
import taipy.core as tc
import taipy.gui_core as tgc
import taipy.config as tpc
import taipy.gui.data as tgd
from taipy.gui import Markdown

from taipy.gui import Gui, Markdown
from src.gui.navigation import get_navigation
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
#######################################################################################################





























































#######################################################################################################
#Running all the Pages 
#######################################################################################################


pages = {
    "/": getting_started.page,
    "/getting-started": getting_started.page,
    "/taipy-core": taipy_core.page,
    "/taipy-gui": taipy_gui.page,
    "/taipy-rest": taipy_rest.page,
    "/taipy-enterprise": taipy_enterprise.page,
    "/deployment": deployment.page,
    "/best-practices": best_practices.page,
    "/integrations": integrations.page,
    "/search": search_page,
}








#######################################################################################################
#Application run
#######################################################################################################
Gui(pages=pages, nav=get_navigation()).run()