# © 2024 Tushar Aggarwal. All rights reserved. (https://tushar-aggarwal.com)
## Taipy Cheat Sheets (https://github.com/tushar2704/Taipy-Cheat-Sheets)

#######################################################################################################
# Importing dependencies
#######################################################################################################
import taipy as tp
from taipy import Gui
from taipy.gui import state
import plotly.express as px
import numpy as np

# Create a simple plot using Plotly
def create_plot():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    fig = px.line(x=x, y=y, labels={'x': 'X', 'y': 'Y'}, title='Simple Sine Wave Plot')
    fig.update_layout(legend_title_text='Curve')
    return fig

# Custom theme
my_theme = {
    "global": {
        "background_color": "#E7E8D1",
        "font_color": "#2A2F33",
    },
    "chart": {
        "primary_color": "#2A2F33",
        "secondary_color": "#2A2F33",
    }
}

# Define the GUI layout
page = """
# [Taipy Cheat Sheets](https://github.com/tushar2704/Taipy-Cheat-Sheets)

by [Tushar Aggarwal](https://www.linkedin.com/in/tusharaggarwalinseec/)

<|{chart}|chart|>
"""

# Create a Gui instance
gui = Gui(page=page)

# Function to update the chart
def update_chart(gui):
    gui.state.chart = create_plot()

# Set initial state and bind update function
gui.state.chart = create_plot()
gui.on_init(update_chart)

# Run the GUI
gui.run(debug=True, use_reloader=True, theme=my_theme)