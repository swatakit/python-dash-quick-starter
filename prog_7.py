#########################################
# Dash with dcc and callbacks - advanced
#
# ref: https://dash.plotly.com/introduction
# ref: https://plotly.com/python/
# ref: https://dash.plotly.com/dash-core-components


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

all_options = {
    'America': ['New York City', 'San Francisco', 'Cincinnati'],
    'Canada': [u'Montréal', 'Toronto', 'Ottawa']
}

themes = ['Blackbody', 'Bluered', 'Blues', 'Earth', 'Electric', 'Greens', 'Greys', 'Hot', 'Jet',
          'Picnic', 'Portland', 'Rainbow', 'RdBu', 'Reds', 'Viridis', 'YlGnBu', 'YlOrRd']
options_themes = [{'label': theme, 'value': theme} for theme in themes]

# Layout compose
app.layout = html.Div([
    dbc.Container([
        html.Br(),
        html.H1('Dash Core Components and Callbacks - Advanced'),
        html.H3('Please inspect Callback Graph',style={'color':'blue'}),
        html.Hr(),
        html.H3('Callback #5 Chained callback between 2 radio button group, and a Div'),
        html.Br(),
        dbc.RadioItems(
            id='countries-radio',
            options=[{'label': k, 'value': k} for k in all_options.keys()],
            value='America'
        ),
        html.Br(),
        dbc.RadioItems(id='cities-radio'),
        html.Br(),
        html.Div(id='display-selected-values'),
        html.Hr(),
        html.H3('Callback #6 One Input > Multiple Outputs'),
        dcc.Input(
            id='num-multi',
            type='number',
            value=5
        ),
        html.Table([
            html.Tr([html.Td(['x', html.Sup(2)]), html.Td(id='square')]),
            html.Tr([html.Td(['x', html.Sup(3)]), html.Td(id='cube')]),
            html.Tr([html.Td([2, html.Sup('x')]), html.Td(id='twos')]),
            html.Tr([html.Td([3, html.Sup('x')]), html.Td(id='threes')]),
            html.Tr([html.Td(['x', html.Sup('x')]), html.Td(id='x^x')]),
        ]),
        html.Hr(),
        html.H3('Callback #7 Graph Callbacks'),
        html.Label("Choose Themes"),
        html.Div(id='selected-theme'),
        dcc.Dropdown(
            id='dropdown-theme',
            options=options_themes,
            value='Viridis'
        ),
        dcc.Graph(id='themed-graph')
    ])
])

# Callback #5 : Chained callback between 2 radio button group and a Div
# Action #1 : By selecting a country, 'set_cities_options()' is fired, sending option-value-lists to the object 'cities-radio'
# Action #2 : upon receiving option-value-lists, 'set_cities_value()' is fired. the first value is set at 'cities-radio' , triggering the 'set_display_children()' to be fired
# Action #3 : upon triggering, a customized text is sent to the div id='display-selected-values'
@app.callback(
    Output('cities-radio', 'options'),
    [Input('countries-radio', 'value')])
def set_cities_options(selected_country):
    return [{'label': i, 'value': i} for i in all_options[selected_country]]

@app.callback(
    Output('cities-radio', 'value'),
    [Input('cities-radio', 'options')])
def set_cities_value(available_options):
    return available_options[0]['value']

@app.callback(
    Output('display-selected-values', 'children'),
    [Input('countries-radio', 'value'),
     Input('cities-radio', 'value')])
def set_display_children(selected_country, selected_city):
    return dbc.Alert("{} is a city in {}".format(selected_city, selected_country),color='primary',className="mt-2") 

# Callback #6 One Input > Multiple Outputs
@app.callback(
    [Output('square', 'children'),
     Output('cube', 'children'),
     Output('twos', 'children'),
     Output('threes', 'children'),
     Output('x^x', 'children')],
    [Input('num-multi', 'value')])
def callback_a(x):
    return x**2, x**3, 2**x, 3**x, x**x

# Callback #7 Graph Callbacks
@app.callback(
    Output('themed-graph', 'figure'),
    [Input('dropdown-theme', 'value')])
def update_graph_theme(selected_theme):
    xs = ['giraffes', 'orangutans', 'monkeys']
    ys = [20, 14, 23]
    fig = go.Figure(data=[go.Bar(x=xs,
                                 y=ys,
                                 marker={
                                     'color': ys,
                                     'colorscale': selected_theme
                                 },
                                 hoverinfo='y+text')]
                    )
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)