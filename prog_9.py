#########################################
# Dash with dcc and callbacks, sidebar
#
# ref: https://dash.plotly.com/introduction
# ref: https://plotly.com/python/
# ref: https://dash.plotly.com/dash-core-components
# ref: https://dash.plot.ly/urls
# ref: https://github.com/facultyai/dash-bootstrap-components/tree/master/examples/multi-page-apps


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions = True


# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}


sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "A simple sidebar layout with navigation links", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/",id="page-home-link"),
                dbc.NavLink("Page 1", href="/page_1", id="page-1-link"),
                dbc.NavLink("Page 2", href="/page_2", id="page-2-link"),
                dbc.NavLink("Page 3", href="/page_3", id="page-3-link"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

data_canada = px.data.gapminder().query("country == 'Canada'")
fig_1 = px.bar(data_frame=data_canada, x='year', y='pop',template='ggplot2')
fig_2 = px.bar(data_frame=data_canada, x='year', y='pop',template='plotly_dark')
fig_3 = px.bar(data_frame=data_canada, x='year', y='pop',template='xgridoff')

page_home = html.Div([
    html.H1('Hello, this is Home'),
    html.Section(id="slideshow", children=[
        html.Div(id="slideshow-container", 
            children=[
                html.Div(id="image"),
                dcc.Interval(id='interval', interval=3000)
            ])
    ])
])

page_1 = html.Div([
            html.H1('Hello, this is Page-1'),
            dcc.Graph(figure=fig_1)
])

page_2 = html.Div([
            html.H1('Hello, this is Page-2'),
            dcc.Graph(figure=fig_2)
])

page_3 = html.Div([
            html.H1('Hello, this is Page-3'),
            dcc.Graph(figure=fig_3)
])

collapse = html.Div(
    [
        dbc.Button(
            "Open collapse",
            id="collapse-button",
            className="mb-3",
            color="primary",
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody('''Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
            Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
            Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.''')),
            id="collapse",className='nt-3 mb-3'
        ),
    ]
)


app.layout = html.Div([
    dcc.Location(id="url", refresh=False), 
    sidebar,
    html.Div([
        dbc.Jumbotron([
                collapse,
                dbc.Container(id="page-content")
            ])
        ],
        # this style has to go with outer Div, 
        # to have an equally balanced margin left-right
        style=CONTENT_STYLE) 
])

# this callback uses the current pathname to set the active state of the
# corresponding nav link to true, allowing users to tell see page they are on
@app.callback(
    [Output("page-home-link", "active"),
    Output("page-1-link", "active"),
    Output("page-2-link", "active"),
    Output("page-3-link", "active"),],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        return True, False, False, False
    if pathname == "/page_1":
        return False,True, False, False
    if pathname == "/page_2":
        return False, False, True, False
    if pathname == "/page_3":
        return False, False, False, True


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")],
)
def display_page(pathname):

    if pathname == "/":
        return page_home

    if pathname == "/page_1":
        return page_1

    elif pathname == "/page_2":
        return page_2

    elif pathname == "/page_3":
        return page_3

    else:
        return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognized..."),
        ]
        )

@app.callback(Output('image', 'children'),
              [Input('interval', 'n_intervals')])
def display_image(n):
    if n == None or n % 3 == 1:
        img = html.Img(src="https://source.unsplash.com/collection/190727/1400x700",height='550px')
    elif n % 3 == 2:
        img = html.Img(src="https://source.unsplash.com/collection/190727/1400x700",height='550px')
    elif n % 3 == 0:
        img = html.Img(src="https://source.unsplash.com/collection/190727/1400x700",height='550px')
    else:
        img = "None"
    return img

@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

if __name__ == "__main__":
    app.run_server(debug=True)