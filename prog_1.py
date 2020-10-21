#########################################
# The Simplest form of dash application
#
# ref: https://dash.plotly.com/introduction

import dash
import dash_html_components as html

app = dash.Dash(__name__)

# Layout compose
app.layout = html.Div([
    html.H1('Hello, this is a Dash Application'),
])

if __name__ == "__main__":
    app.run_server(debug=False)
