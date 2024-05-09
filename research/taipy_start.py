#© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
## Start with Taipy Application Demo by Tushar Aggarwal
#######################################################################################################
import taipy as tp
from taipy import Gui
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
page = """
# [Taipy Cheat Sheets](https://github.com/tushar2704/Taipy-Cheat-Sheets)

by [Tushar Aggarwal](https://www.linkedin.com/in/tusharaggarwalinseec/)
"""

Gui(page=page).run(debug=True,use_reloader=True, theme=my_theme)  