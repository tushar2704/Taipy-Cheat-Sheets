#© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
import taipy as tp
from taipy import Gui
page = """
# My Taipy App

This is my Taipy application.

[Taipy Cheat Sheets](https://github.com/tushar2704/Taipy-Cheat-Sheets)
by [Tushar Aggarwal](https://www.linkedin.com/in/tusharaggarwalinseec/)
"""
tp.Core().run()
Gui(page=page).run(debug=True,use_reloader=True) 