#########################################
# Dash with a few simple graphs, with bootstrap grid system
#
# ref: https://dash.plotly.com/introduction
# ref: https://plotly.com/python/
# ref: bootstrap-crash-course
# ref: https://getbootstrap.com/docs/4.4/getting-started/introduction/

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd

# if not already in a folder 'assets', dash will retrieve from internet
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

# Basic plotly express graph, with dataframe as input
data_canada = px.data.gapminder().query("country == 'Canada'")
fig_1 = px.bar(data_frame=data_canada, x='year', y='pop')
fig_2 = px.bar(data_frame=data_canada, x='year', y='pop',template='ggplot2')

df = px.data.gapminder()
df_2007 = df.query("year==2007")
fig_3 = px.scatter(df_2007,x="gdpPercap", y="lifeExp", size="pop", color="continent",
                     log_x=True, size_max=60,
                     template='seaborn', title="Gapminder 2007: '%s' theme" % 'seaborn')

z_data = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv")
fig_4 = go.Figure(
    data=go.Surface(z=z_data.values),
    layout=go.Layout(
        title="Mt Bruno Elevation: '%s' theme" % 'plotly_dark',
        width=500,
        height=500,
        template='plotly_dark'
    ))

app.layout = html.Div([
    dbc.Row([
        html.H1('Hello, this is a Dash Application',style={'margin-left': '30px'})
    ]),
    dbc.Row([
        dbc.Button(['This is Bootstrap Button'],color='primary',className='ml-3 mt-3'),
        dbc.Button(['This is Bootstrap Button'],color='info',className='ml-3 mt-3'),
        dbc.Button(['This is Bootstrap Button'],color='success',className='ml-3 mt-3'),
        dbc.Button(['This is Bootstrap Button'],color='warning',className='ml-3 mt-3'),
        dbc.Button(['This is Bootstrap Button'],color='danger',className='ml-3 mt-3'),
    ]),
    dbc.Row([
        dbc.Col([dcc.Graph(figure=fig_1)]),
        dbc.Col([dcc.Graph(figure=fig_2)]),
    ]),
    dbc.Row([
        dbc.Col([dcc.Graph(figure=fig_3)]),
        dbc.Col([dcc.Graph(figure=fig_4)]),
    ])
])

if __name__ == "__main__":
    app.run_server(debug=False)
