##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################

import os, sys, requests, logging, pathlib
import taipy as tp
from taipy import Config, Gui, Scenario
from taipy.gui import Gui, Icon, navigate
import taipy.gui.builder as tgb
import taipy.core as tc
import taipy.gui_core as tgc
import taipy.config as tpc
import taipy.gui.data as tgd
from taipy.gui import Markdown


from src.pages.getting_started import getting_started_md
#######################################################################################################

# custom theme
my_theme = {
    "palette": {
        "background": {"default": "#E7E8D1"},  
        "text": {"primary": "#2A2F33"}, 
        "primary": {"main": "#2A2F33"},  
        "secondary": {"main": "#2A2F33"},  
        "link": {"main": "#2A2F33"},  #       
    }
}



root_md = Markdown("""
# Welcome to Taipy Cheat Sheets
<|navbar|>
This is the home page of the Taipy Cheat Sheets application. Use the navigation to explore different features and guides.

## Available Pages

- [Getting Started](#/getting_started)
- [Taipy Core](#/taipy_core)
- [Taipy GUI](#/taipy_gui)
- [Taipy REST](#/taipy_rest)
- [Taipy Enterprise](#/taipy_enterprise)
- [Deployment](#/deployment)
- [Best Practices](#/best_practices)
- [Integrations](#/integrations)
- [User Examples](#/user_examples)
- [Related Resources](#/related_resources)
""")













































pages = {"/": root_md,
    "Getting Started": getting_started_md}


# Run the application
Gui(pages=pages).run(debug=True,use_reloader=True)










#######################################################################################################
#Running all the Pages 
#######################################################################################################







#######################################################################################################
#Application run
#######################################################################################################