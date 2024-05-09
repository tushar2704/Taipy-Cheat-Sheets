#© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
#All about Table with Taipy by Tushar Aggarwal
#######################################################################################################
from taipy.gui import Gui, Markdown, notify
import pandas as pd
# custom theme
my_theme = {
    "palette": {
        "background": {"default": "#E7E8D1"},  
        "text": {"primary": "#ef0041"}, 
        "primary": {"main": "#2A2F33"},  
        "secondary": {"main": "#2A2F33"},  
        "link": {"main": "#2A2F33"},  #       
    }
}

# Sample food data
food_df = pd.DataFrame({
    "Meal": ["Lunch", "Dinner", "Lunch", "Lunch", "Breakfast", "Breakfast", "Lunch", "Dinner"],
    "Category": ["Entree", "Entree", "Beverage", "Entree", "Entree", "Beverage", "Dessert", "Dessert"],
    "Item": ["Burger", "Pizza", "Soda", "Salad", "Omelette", "Coffee", "Ice Cream", "Cake"],
    "Calories": [500, 800, 150, 250, 400, 5, 300, 600],
    "Price": [8.99, 12.99, 1.99, 6.99, 7.99, 2.99, 4.99, 5.99]
})

# Callback functions for table editing
def food_df_on_edit(state, var_name, payload):
    index = payload["index"] 
    col = payload["col"]
    value = payload["value"]
    
    old_value = state.food_df.loc[index, col]
    new_food_df = state.food_df.copy()
    new_food_df.loc[index, col] = value
    state.food_df = new_food_df
    notify(state, "info", f"Edited value from '{old_value}' to '{value}'. (index '{index}', column '{col}')")

def food_df_on_delete(state, var_name, payload):
    index = payload["index"]
    state.food_df = state.food_df.drop(index=index)
    notify(state, "error", f"Deleted row at index '{index}'")

def food_df_on_add(state, var_name, payload):
    empty_row = pd.DataFrame([[None for _ in state.food_df.columns]], columns=state.food_df.columns) 
    state.food_df = pd.concat([empty_row, state.food_df], ignore_index=True)
    notify(state, "success", f"Added a new row.")

# Table properties
table_properties = {
    "class_name": "rows-bordered",
    "filter": True,
    "on_edit": food_df_on_edit,
    "on_delete": food_df_on_delete,
    "on_add": food_df_on_add,
    "group_by[Category]": True,
    "apply[Calories]": "sum",
    "apply[Price]": "mean"
}

# Markdown content
main_md = Markdown("""
# [Taipy Cheat Sheets](https://github.com/tushar2704/Taipy-Cheat-Sheets)

### by [Tushar Aggarwal](https://www.linkedin.com/in/tusharaggarwalinseec/)

# All About Tables in Taipy

Taipy tables provide powerful features for displaying and interacting with data.

## Basic Table

<|{food_df}|table|>

## Table with Editing, Filtering and Grouping

<|{food_df}|table|properties=table_properties|>

This table demonstrates:
- Editing cells with on_edit callback 
- Deleting rows with on_delete callback
- Adding new rows with on_add callback  
- Filtering data
- Grouping by Category column
- Aggregating Calories with sum and Price with mean
""")

Gui(page=main_md).run(debug=True,use_reloader=True, theme=my_theme)