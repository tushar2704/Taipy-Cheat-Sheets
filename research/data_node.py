#© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
from taipy import Config, DataNode
import taipy as tp
from taipy import Gui

# Define the configuration for the data node
# Note: The 'configure_data_node' method is not directly available under 'Config' in Taipy.
# Instead, you should define a global variable for the data node configuration.
global_data_node_config = "global_data_config"
Config.configure_data_node(id=global_data_node_config, scope=tp.Scope.GLOBAL)

# Create the global data node using the configuration
# Note: The 'DataNode' constructor does not accept 'config_id' as a parameter.
# You should use 'tp.create_data_node' to create a data node based on its configuration ID.
global_data_node = tp.create_data_node(global_data_node_config)

# Define the cheat sheet content
cheat_sheet_content = """
## Taipy Data Node Cheat Sheet

### Key Attributes:
- **config_id**: Unique identifier for the Data Node configuration.
- **scope**: Defines the scope of the Data Node (e.g., global or scenario-specific).
- **id**: The unique identifier of the Data Node.
- **name**: A user-readable name of the Data Node.
- **last_edit_date**: The date and time of the last modification.

### Key Methods:
- **get()**: Retrieve an entity by its unique identifier.
- **create_global_data_node()**: This method does not exist. Use 'tp.create_data_node' instead.
- **delete()**: Delete an entity and its nested entities.
"""

# Define the user interface
# Note: The 'add_data_node' method expects a DataNode object and a variable name.
# The 'cheat_sheet_content' should be assigned to a DataNode for display in the GUI.
cheat_sheet_data_node = tp.DataNode(id="cheat_sheet_data", default_data=cheat_sheet_content, scope=tp.Scope.GLOBAL)

page = """
# Taipy Data Node Cheat Sheet

<|{cheat_sheet_data}|data_node|>
"""

# Create the Taipy GUI
gui = Gui(page=page)

# Bind the Data Node to the GUI
gui.add_data_node(cheat_sheet_data_node, "cheat_sheet_data")

if __name__ == "__main__":
    gui.run()
