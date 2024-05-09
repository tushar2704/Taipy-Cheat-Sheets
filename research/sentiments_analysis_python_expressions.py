#© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
# Import necessary modules from Taipy
import numpy as np
import pandas as pd
from taipy.gui import Gui, notify
# custom theme
my_theme = {
    "palette": {
        "background": {"default": "#E7E8D1"},  
        "text": {"primary": "#2A2F33"}, 
        "primary": {"main": "#2A2F33"},  
        "secondary": {"main": "#2A2F33"},  
        "link": {"main": "#2A2F33"},  #       
    }
}
# Sample data
text = "Taipy is a powerful and intuitive Python library for building interactive web applications."

dataframe = pd.DataFrame({
    "Text": ["Taipy is awesome!", "The documentation is comprehensive.", "Looking forward to exploring more features."],
    "Score Pos": [0.9, 0.8, 0.95], 
    "Score Neu": [0.05, 0.15, 0.05],
    "Score Neg": [0.05, 0.05, 0.0],
    "Overall": [0.85, 0.75, 0.95]
})

# Function to analyze sentiment of input text
def analyze_sentiment(text):
    # Placeholder function, replace with actual sentiment analysis logic
    return {
        "Text": text,
        "Score Pos": np.random.uniform(0.7, 1.0),
        "Score Neu": np.random.uniform(0.0, 0.2),
        "Score Neg": np.random.uniform(0.0, 0.1),
        "Overall": np.random.uniform(0.7, 1.0)
    }

# Callback function to update sentiment scores
def update_sentiment(state):
    notify(state, "info", f"Analyzing sentiment for: {state.text}")
    sentiment = analyze_sentiment(state.text)
    state.dataframe = pd.concat([state.dataframe, pd.DataFrame([sentiment])], ignore_index=True)
    state.text = ""

# Taipy GUI markdown 
page = """
# [Taipy Cheat Sheets](https://github.com/tushar2704/Taipy-Cheat-Sheets)

### by [Tushar Aggarwal](https://www.linkedin.com/in/tusharaggarwalinseec/)

## Sentiment Analysis & Python Expresions Demo with Taipy 

Enter text to analyze sentiment: <|{text}|input|>

<|Analyze|button|on_action=update_sentiment|>

## Overall Sentiment Metrics

### Average Positive Score
<|{np.mean(dataframe["Score Pos"])}|text|format=%.2f|>

### Average Neutral Score  
<|{np.mean(dataframe["Score Neu"])}|text|format=%.2f|>

### Average Negative Score
<|{np.mean(dataframe["Score Neg"])}|text|format=%.2f|>

## Sentiment Analysis Results

<|{dataframe}|table|width=100%|>

<|{dataframe}|chart|type=bar|x=Text|y[1]=Score Pos|y[2]=Score Neu|y[3]=Score Neg|color[1]=green|color[2]=gray|color[3]=red|>
"""

Gui(page).run(title="Sentiment Analysis", debug=True,use_reloader=True, theme=my_theme)