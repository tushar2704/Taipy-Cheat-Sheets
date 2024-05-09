#© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
import taipy as tp

# Define the data nodes
input_data_node = tp.DataNode(name="input_data", default_data=None)
processed_data_node = tp.DataNode(name="processed_data", default_data=None)
visualization_data_node = tp.DataNode(name="visualization_data", default_data=None)

# Define the task functions
def data_processing_task(input_data):
    # Perform data processing and manipulation using Taipy Core
    processed_data = input_data.apply(lambda x: x ** 2)
    return processed_data

def data_visualization_task(processed_data):
    # Create visualizations using the processed data
    visualization_data = processed_data.plot(kind="bar")
    return visualization_data

# Create the pipeline
pipeline = tp.Pipeline(name="taipy_core_demo")

# Add the tasks to the pipeline
pipeline.add_task(task_func=data_processing_task, input=input_data_node, output=processed_data_node)
pipeline.add_task(task_func=data_visualization_task, input=processed_data_node, output=visualization_data_node)

# Create the scenario
scenario = tp.Scenario(name="taipy_core_scenario", pipeline=pipeline)

# Define the user interface
page = """
# All About Taipy Core

## Data Input
<|{input_data}|>

## Data Processing
<|{processed_data}|>

## Data Visualization
<|{visualization_data}|>
"""

# Create the Taipy GUI
gui = tp.Gui(page=page)

# Bind the data nodes to the GUI
gui.add_data_node(input_data_node)
gui.add_data_node(processed_data_node)
gui.add_data_node(visualization_data_node)

# Run the Taipy Core application
if __name__ == "__main__":
    # Set the input data
    input_data = tp.DataNode(name="input_data", default_data=[1, 2, 3, 4, 5])
    
    # Submit the scenario
    tp.submit(scenario)
    
    # Run the GUI
    gui.run()
