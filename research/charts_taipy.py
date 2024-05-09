# © 2024 Tushar Aggarwal. All rights reserved. (https://tushar-aggarwal.com)
## Taipy Cheat Sheets (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
# Charts Application Demo by Tushar Aggarwal
#######################################################################################################
import taipy as tp
import pandas as pd
import numpy as np
from taipy.gui import Gui
import plotly.graph_objects as go
import folium

# Create sample data
data1 = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
data2 = pd.DataFrame({'category': ['A', 'B', 'C'], 'value': [10, 20, 30]})
data3 = pd.DataFrame({'x': range(100), 'y': np.random.randn(100).cumsum()})
data4 = pd.DataFrame({'country': ['USA', 'Canada', 'Mexico', 'Brazil', 'Argentina'],
                      'population': [331002651, 37742154, 128932753, 212559417, 45195774]})
data5 = pd.DataFrame({'year': [2010, 2011, 2012, 2013, 2014],
                      'sales': [100, 120, 150, 200, 180]})
data6 = pd.DataFrame({'product': ['A', 'B', 'C', 'D'],
                      'Q1': [100, 150, 200, 120],
                      'Q2': [120, 180, 220, 140],
                      'Q3': [140, 200, 240, 160],
                      'Q4': [160, 220, 260, 180]})

# Create a Plotly figure
fig = go.Figure(data=go.Scatter(x=data3['x'], y=data3['y']))

# Create a Folium map
m = folium.Map(location=[45.5236, -122.6750], zoom_start=13)
folium.Marker(
    location=[45.5244, -122.6699], 
    popup="The Waterfront",
    icon=folium.Icon(color="blue")
).add_to(m)

# Define the Taipy page
page = """
# Chart with Taipy Demo

## Built-in Taipy Charts

### Line Chart
<|{data1}|chart|x=x|y=y|>

### Bar Chart
<|{data2}|chart|x=category|y=value|type=bar|>

### Scatter Plot
<|{data3}|chart|x=x|y=y|mode=markers|>

## Plotly Integration

<|chart|figure={fig}|>

## Folium Map Integration

<|{m}|part|>

## More Chart Examples

### Pie Chart
<|{data4}|chart|values=population|labels=country|type=pie|>

### Stacked Bar Chart
<|{data5}|chart|x=year|y[1]=sales|y[2]=sales|type[1]=bar|type[2]=bar|color[1]=blue|color[2]=red|>

### Bubble Chart
<|{data1}|chart|x=x|y=y|size=y|mode=markers|>

### Heatmap
<|[[1, 20, 30], [20, 1, 60], [30, 60, 1]]|chart|type=heatmap|>

### 3D Surface Plot
<|[[1, 2, 3], [4, 5, 6], [7, 8, 9]]|chart|type=surface|>

### Stacked Area Chart
<|{data6}|chart|x=product|y[1]=Q1|y[2]=Q2|y[3]=Q3|y[4]=Q4|type[1]=area|type[2]=area|type[3]=area|type[4]=area|>

### Radar Chart
<|{data6}|chart|theta=product|r[1]=Q1|r[2]=Q2|r[3]=Q3|r[4]=Q4|type=scatterpolar|fill=toself|>

### Funnel Chart
<|{data2}|chart|y=value|x=category|type=funnel|>

### Gauge Chart
<|{data2}|chart|value=value|type=indicator|mode=gauge|gauge={{'axis': {'range': [0, 50]}}}|>


"""

# Run the Taipy application
Gui(page).run()