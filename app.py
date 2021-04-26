# Import Libraries
# Import Libraries

import pandas as pd 
import plotly.express as px 
import dash
import dash_core_components as dcc
import dash_html_components as html

# HTML Heading 

myheading='Flying Dog Beers'
tabtitle='COVID-19'

# Read CSV file 

df = pd.read_csv("covid19pt_data.csv")

## set the index as the data column
## all of the remaining columns are now of the same int64 type
df = df.set_index('data')

# Plot
fig = px.bar(df)

# fig.show()


########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='flyingdog',
        figure=fig 
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A('Data Source', href=sourceurl),
    ]
)

if __name__ == '__main__':
    app.run_server()


