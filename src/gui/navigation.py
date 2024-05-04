##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
from taipy.gui import Markdown, Icon, Nav, NavItem

def get_navigation():
    return Nav(
        [
            NavItem("Getting Started", "/getting-started", Icon("home")),
            NavItem("Taipy Core", "/taipy-core", Icon("code")),
            NavItem("Taipy GUI", "/taipy-gui", Icon("desktop")),
            NavItem("Taipy REST", "/taipy-rest", Icon("cloud")),
            NavItem("Taipy Enterprise", "/taipy-enterprise", Icon("building")),
            NavItem("Deployment", "/deployment", Icon("rocket")),
            NavItem("Best Practices", "/best-practices", Icon("check-circle")),
            NavItem("Integrations", "/integrations", Icon("plug")),
        ],
        active="/getting-started",
    )