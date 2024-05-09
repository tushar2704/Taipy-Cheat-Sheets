#© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
import taipy as tp
import pandas as pd

# Define the data nodes with the required config_id
input_data_node = tp.DataNode(config_id="input_data_config", default_data=pd.DataFrame([1, 2, 3, 4, 5]))
processed_data_node = tp.DataNode(config_id="processed_data_config", default_data=pd.DataFrame())
visualization_data_node = tp.DataNode(config_id="visualization_data_config", default_data=pd.DataFrame())

# Define the task functions
def data_processing_task(input_data):
    # Simple data processing
    processed_data = input_data * 2  # Multiply input data by 2
    return processed_data

def data_visualization_task(processed_data):
    # Simple data visualization logic
    visualization_data = processed_data.mean()  # Calculate mean of the processed data
    return visualization_data

# Create tasks
processing_task = tp.Task(
    config_id="processing_task_config",
    id="processing_task",
    function=data_processing_task,
    input=[input_data_node],
    output=[processed_data_node],
    properties={}
)

visualization_task = tp.Task(
    config_id="visualization_task_config",
    id="visualization_task",
    function=data_visualization_task,
    input=[processed_data_node],
    output=[visualization_data_node],
    properties={}
)

# Create the scenario
scenario = tp.Scenario(id="example_scenario", tasks=[processing_task, visualization_task])

# Example usage
if __name__ == "__main__":
    scenario.run()
    print("Processed Data:", processed_data_node.read())
    print("Visualization Data:", visualization_data_node.read())

