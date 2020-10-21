#########################################
# Dash with a few simple graphs, with css 
#
# ref: https://dash.plotly.com/introduction
# ref: https://plotly.com/python/
# ref : https://plotly.com/python/templates/

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px

app = dash.Dash(__name__)

# Basic plotly graph 
animals=['giraffes', 'orangutans', 'monkeys']
fig_1 = go.Figure([go.Bar(x=animals, y=[20, 14, 23],)])
fig_1.update_layout({'plot_bgcolor': 'gray',
                    'paper_bgcolor': 'black',
                    'font': {'color': 'lightblue'},
                    'title' : 'A Simple Barchart'})


# Basic plotly express graph, with dataframe as input, with  theme
data_canada = px.data.gapminder().query("country == 'Canada'")
fig_2 = px.bar(data_frame=data_canada, x='year', y='pop',
               template='ggplot2')

# Layout compose
app.layout = html.Div([
    html.H1('Hello, this is a Dash Application',style={'color':'red'}),
    html.Hr(),
    html.H3('Graph #1 - Simple Plotly'),
    dcc.Graph(figure=fig_1),
    html.Hr(),
    html.H3('Graph #2 - Simple Plotly Express'),
    dcc.Graph(figure=fig_2),
])

if __name__ == "__main__":
    app.run_server(debug=False)
