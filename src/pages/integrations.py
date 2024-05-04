##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################from taipy.gui import Markdown, Gui, Dropdown

page = """
# Integrations

Taipy integrates with various databases, machine learning libraries, and cloud platforms.

<|Dropdown|label=Database Integration Code|>
```python
from taipy.core.data import PostgreSQLDataNode

data_node = PostgreSQLDataNode(
    id="my_data",
    host="localhost",
    port=5432,
    database="my_db",
    username="user",
    password="password",
    table="my_table"
)
"""