#© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
import taipy as tp
from taipy import Config, Scenario
import pandas as pd
import datetime as dt
#Data nodes

#Meeting Schedule Application
# meeting_data: Contains the details of the meetings.
# selected_date: The date for which the user wants to schedule or reschedule a meeting.
# meeting_outcome: Stores the outcome after processing the meeting data for the selected date.


meeting_data_cfg = Config.configure_data_node(id="meeting_data")
selected_date_cfg = Config.configure_data_node(id="selected_date")
meeting_outcome_cfg = Config.configure_data_node(id="meeting_outcome")

#Task
def process_meetings(meeting_data: pd.DataFrame, selected_date: dt.datetime):
    # Filter meetings for the selected date
    result = meeting_data[meeting_data['date'] == pd.to_datetime(selected_date)]
    return result.describe()  # Summarize meeting data for the day

task_cfg = Config.configure_task(
    id="process_meetings",
    function=process_meetings,
    input=[meeting_data_cfg, selected_date_cfg],
    output=meeting_outcome_cfg
)

#Configure the Scenario
scenario_cfg = Config.configure_scenario(id="meeting_schedule_scenario", task_configs=[task_cfg])

#Instantiate and Run the Scenario

# Sample data
data = pd.DataFrame({
    'date': [dt.datetime.now().date(), dt.datetime.now().date() + dt.timedelta(days=1)],
    'meeting_title': ['Budget Review', 'Project Planning'],
    'duration': [2, 1.5]  # Duration in hours
})

# Run the Core
tp.Core().run()

# Creation of the scenario and execution
scenario = tp.create_scenario(scenario_cfg)
scenario.meeting_data.write(data)
scenario.selected_date.write(dt.datetime.now().date())
tp.submit(scenario)

print("Meeting data for today:", scenario.meeting_outcome.read())

