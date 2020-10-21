
#########################################
# Dash with json maps
#
# ref: https://plotly.com/python/mapbox-county-choropleth/

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import json
import plotly.express as px

with open('th_geo.json', "r") as jsonFile:
    geojson = json.load(jsonFile)

df = pd.read_csv('th_data.csv')

fig = px.choropleth_mapbox(df, 
                           geojson=geojson, 
                           color="total_pop",
                           locations="name", 
                           featureidkey="properties.name",
                           center={"lat": 12.85, "lon": 100.60},
                           mapbox_style="carto-positron", 
                           color_continuous_scale="PuRd",
                           hover_data=['avg_income','mkt_penlt'],
                           zoom=4)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Mapbox in Dash"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)
