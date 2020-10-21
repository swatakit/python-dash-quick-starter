#########################################
# Dash with dcc and callbacks
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

# Layout compose
app.layout = html.Div([
    dbc.Container([
        html.H1('Dash Core Components and Callbacks'),
        html.H3('Please inspect Callback Graph',style={'color':'blue'}),
        html.Hr(),
        html.H3('Callback #1 Dropdown'),
        dcc.Dropdown(
            id='dropdown',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montreal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            value='NYC'
            ),
        html.Div(id='output-div-dd'),
        html.Hr(),
        html.H3('Callback #2 Radio button'),
        dbc.RadioItems(
            id='radio',
            options=[
                {'label': 'Chicken', 'value': 'Chicken'},
                {'label': 'Duck', 'value': 'Duck'},
                {'label': 'Pigeon', 'value': 'Pigeon'}
            ],
            value='Pigeon',
            #inline=True
        ),
        html.Div(id='output-div-rd'),
        html.Hr(),
        html.H3('Callback #3 Switch Tab'),
        dbc.Tabs(
            [
                dbc.Tab(label="Tab 1", tab_id="tab-1"),
                dbc.Tab(label="Tab 2", tab_id="tab-2"),
            ],
            id="tabs",
            active_tab="tab-1",
        ),
        html.Div(id="output-div-tab"),
        html.Hr(),
        html.H3('Callback #4 Textbox and Button'),
        html.Div(dcc.Input(id='input-box', type='text')),
        html.Button('Submit', id='button'),
        html.Div(id='output-div',children='Enter a value and press submit')

    ])
])

# Callback #1 Dropdown
@app.callback(
    Output('output-div-dd', 'children'),
    [Input('dropdown', 'value')])
def update_output_dp(value):
    return 'You have selected "{}"'.format(value)

# Callback #2 Radio button
@app.callback(
    Output('output-div-rd', 'children'),
    [Input('radio', 'value')])
def update_output_rd(value):
    return 'You have selected "{}"'.format(value)

# Callback #3 Switch Tab
@app.callback(
    Output("output-div-tab", "children"), 
    [Input("tabs", "active_tab")])
def switch_tab(at):
    if at == "tab-1":
        return dbc.Alert("Tab 1 Selected",color='primary',className="mt-2")
    elif at == "tab-2":
        return dbc.Alert("Tab 2 Selected",color='success',className="mt-2")
        
    return html.P("This shouldn't ever be displayed...")

# Callback #4 Textbox and Button
@app.callback(
    Output('output-div', 'children'),
    [Input('button', 'n_clicks')],
    [State('input-box', 'value')])
def update_output_txtbox(n_clicks, value):
    return 'The input value was "{}" and the button has been clicked {} times'.format(value,n_clicks )

if __name__ == "__main__":
    app.run_server(debug=True)
