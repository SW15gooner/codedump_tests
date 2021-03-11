import plotly.graph_objects as go

import pandas as pd

# Read data from a csv
z_data = pd.read_csv('CMAP_full.csv')

fig = go.Figure(data=[go.Surface(z=z_data.values)])

fig.update_layout(title='Mt Bruno Elevation', autosize=True,
                  width=1000, height=1000,
                  margin=dict(l=65, r=50, b=65, t=90))

fig.show()
