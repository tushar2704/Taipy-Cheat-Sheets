##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
from taipy.gui import Markdown, Gui, Dropdown

page = """
# Best Practices

Follow these best practices to write clean, maintainable, and efficient Taipy code.

<|Dropdown|label=Project Structure|>
<|my_project/
├── src/
│ ├── scenarios/
│ ├── pipelines/
│ ├── tasks/
│ ├── gui/
│ └── config/
├── tests/
├── data/
├── docs/
├── requirements.txt
└── README.md|>

## Demo

*TODO: Add a demo showcasing best practices in Taipy code organization*
"""

Gui(page=Markdown(page)).run()