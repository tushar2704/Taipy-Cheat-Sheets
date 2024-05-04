##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
from taipy.gui import Markdown

def get_navigation():
    return Markdown(
        """
        <navbar>
            <nav-item label="Home" value="/"></nav-item>
            <nav-item label="Getting Started" value="/getting-started"></nav-item>
            <nav-item label="Taipy Core" value="/taipy-core"></nav-item>
            <nav-item label="Taipy GUI" value="/taipy-gui"></nav-item>
            <nav-item label="Taipy REST" value="/taipy-rest"></nav-item>
            <nav-item label="Taipy Enterprise" value="/taipy-enterprise"></nav-item>
            <nav-item label="Deployment" value="/deployment"></nav-item>
            <nav-item label="Best Practices" value="/best-practices"></nav-item>
            <nav-item label="Integrations" value="/integrations"></nav-item>
        </navbar>
        """
    )