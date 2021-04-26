# Import Libraries
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import datetime

# Read CSV file 

df = pd.read_csv("covid19pt_data.csv")

## set the index as the data column
## all of the remaining columns are now of the same int64 type

df = df.set_index('data')

# assign colors to column  using a dictionary
colors = dict('casos_novos_t':'coral',
          'casos_novos_d':'darkviolet')

# Assing the chart to a variable 
fig = go.Figure()

#set up ONE trace
fig.add_trace(go.Bar(x=df.index,
						 y=df[df.columns[0]],
						 marker_color = colors,
						 visible=True))


updatemenu = []
buttons = []

# button with one option for each column 
for col in df.columns:
    buttons.append(dict(method='restyle',
                        label=col,
                        visible=True,
                        args=[{'y':[df[col]],
                               'x':[df.index],
                               'type':'bar'}, [0]],
                        )
                  )

# adjustments to the updatemenus

updatemenu = []
main_menu = dict()
updatemenu.append(main_menu)

updatemenu[0]['buttons'] = buttons
updatemenu[0]['direction'] = 'down'
updatemenu[0]['showactive'] = True

# add dropdown menus to the figure
fig.update_layout(showlegend=False, updatemenus=updatemenu)

# Show Graphics
fig.show()


