import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd 
import plotly.express as px 


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle


# Read CSV file 

df = pd.read_csv("covid19pt_data.csv")

## set the index as the data column
## all of the remaining columns are now of the same int64 type
df = df.set_index('data')

# Plot
fig = px.bar(df)

# fig.show()


app.layout = html.Div(children=[
    html.H1(children='COVID-19'),

    html.Div(children='''
        DASHBOARD COVID-19
    '''),

    dcc.Graph(
        id='covid19',
        figure=fig
    )
])




if __name__ == '__main__':
    app.run_server()

