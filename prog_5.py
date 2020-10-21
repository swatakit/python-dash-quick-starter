#########################################
# Dash with a few simple graphs, with bootstrap container and navbar
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

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

data_canada = px.data.gapminder().query("country == 'Canada'")
fig_1 = px.bar(data_frame=data_canada, x='year', y='pop',template='ggplot2')
fig_2 = px.bar(data_frame=data_canada, x='year', y='pop',template='plotly_dark')

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="NavbarSimple",
    brand_href="#",
    sticky="top",
    className='navbar navbar-dark bg-dark',
)

# Layout compose
app.layout = html.Div([
    navbar,
    dbc.Container([
        html.Br(),
        html.H1('Hello, this is a Dash Application'),
        dcc.Graph(figure=fig_1),
        dcc.Graph(figure=fig_2),
    ])
])

if __name__ == "__main__":
    app.run_server(debug=False)


