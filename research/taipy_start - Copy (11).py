#© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
from taipy.gui import Gui, Markdown, notify

import datetime
import pytz

utc_time = datetime.datetime.now(pytz.utc)
ist_time = utc_time.astimezone(pytz.timezone('Asia/Kolkata'))

md = Markdown("""
# 🌍 UTC to IST Time Zone Converter

## 🕐 Enter UTC time
<|{utc_time}|date|on_change=update_ist_time|>

<|{utc_time}|time|on_change=update_ist_time|>

## 🕰️ IST time
<|{ist_time}|date_time|active=False|>

<|Convert Time|button|on_action=convert_time|>
""")

def update_ist_time(state):
    state.ist_time = state.utc_time.astimezone(pytz.timezone('Asia/Kolkata'))
    
def convert_time(state):
    utc = pytz.utc.localize(state.utc_time)
    ist = utc.astimezone(pytz.timezone('Asia/Kolkata'))
    state.ist_time = ist
    notify(state, "Time converted successfully! 🎉", "success")

Gui(page=md).run()
