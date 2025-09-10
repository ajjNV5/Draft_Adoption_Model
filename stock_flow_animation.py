import plotly.express as px
import pandas as pd
import numpy as np

# Generate data for a stock and flow system over time
data = []
for t in np.arange(0, 100, 1):
    inflow = 1.0 + 0.5 * np.sin(t / 10)
    outflow = 0.8 + 0.3 * np.cos(t / 15)
    stock = 100 + (inflow - outflow) * t
    
    # Data for the "stock" bubble
    data.append([t, 'Stock', stock, 'blue'])
    # Data for the "inflow" bubble
    data.append([t, 'Flow', inflow * 50, 'green'])
    # Data for the "outflow" bubble
    data.append([t, 'Flow', outflow * 50, 'red'])

# Create a Pandas DataFrame
df = pd.DataFrame(data, columns=['time', 'type', 'value', 'color'])

# Create the animated scatter plot
fig = px.scatter(
    df,
    x="time",
    y="value",
    size="value",
    color="color",
    hover_name="type",
    animation_frame="time",
    animation_group="type",
    range_x=[0, 100],
    range_y=[0, 150],
    title="Interactive Stock and Flow Animation"
)

# Fix axis ranges so the plot doesn't jump
fig.update_layout(yaxis={'range': [0, 150]}, xaxis={'range': [0, 100]})

# Display the plot
fig.show()
