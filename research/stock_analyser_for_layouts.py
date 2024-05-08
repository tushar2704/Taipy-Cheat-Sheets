#© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#Importing dependecies
#######################################################################################################
import numpy as np
import pandas as pd
import yfinance as yf
from taipy.gui import Gui, notify

# Sample stock tickers
tickers = ["AAPL", "GOOGL", "MSFT", "AMZN", "FB"]
my_theme = {
    "palette": {
        "background": {"default": "#E7E8D1"},  
        "text": {"primary": "#ADD8E6"}, 
        "primary": {"main": "#2A2F33"},  
        "secondary": {"main": "#E7E8D1"},  
        "link": {"main": "#2A2F33"},  #       
    }
}

# Default stock ticker
selected_ticker = "AAPL"

# Function to fetch stock data
def fetch_stock_data(ticker):
    stock_data = yf.download(ticker, start="2022-01-01", end="2023-05-08")
    return stock_data

# Initialize stock data with the default ticker
stock_data = fetch_stock_data(selected_ticker)

# Callback function to update stock data
def update_stock_data(state):
    notify(state, "info", f"Fetching stock data for: {state.selected_ticker}")
    global stock_data
    stock_data = fetch_stock_data(state.selected_ticker)

# Taipy GUI markdown with page layouts
page = """
# [Taipy Cheat Sheets](https://github.com/tushar2704/Taipy-Cheat-Sheets)

### by [Tushar Aggarwal](https://www.linkedin.com/in/tusharaggarwalinseec/)

## Stock Visualization Dashboard

<|layout|columns=1 1|
<|part|
Select a stock ticker:
<|{selected_ticker}|selector|lov={tickers}|on_change=update_stock_data|>
|>

<|part|
## Stock Data
<|{stock_data}|table|width=100%|expandable|>
|>
|>

<|layout|columns=1 1 1|
<|part|
### Average Close Price
<|{stock_data['Close'].mean()}|text|format=%.2f|>
|>

<|part|
### Maximum Close Price
<|{stock_data['Close'].max()}|text|format=%.2f|>
|>

<|part|
### Minimum Close Price
<|{stock_data['Close'].min()}|text|format=%.2f|>
|>
|>

<|{stock_data}|chart|x=Date|y[1]=Open|y[2]=High|y[3]=Low|y[4]=Close|color[1]=blue|color[2]=green|color[3]=red|color[4]=purple|>
"""

Gui(page).run(title="Stock Visualization", debug=True,use_reloader=True, theme=my_theme)