##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
from taipy import Gui
from taipy.gui import Markdown
# getting_started_md = """
# # [Taipy Cheat Sheets](https://github.com/tushar2704/Taipy-Cheat-Sheets)

# by [Tushar Aggarwal](https://www.linkedin.com/in/tusharaggarwalinseec/)

# Welcome! This guide will help you get up and running with Taipy quickly.


# """

root_md = Markdown("src/pages/getting_started.md")

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


Gui(page=root_md).run(debug=True,use_reloader=True, theme=my_theme)  