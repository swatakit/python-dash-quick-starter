#########################################
# The other dash components - table/cards
#
# ref: https://dash.plotly.com/datatable
#


# Layout compose
import dash
import dash_table
import pandas as pd
import dash_html_components as html
import dash_bootstrap_components as dbc

df = pd.read_csv('solar.csv')

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

a_table = dash_table.DataTable(
    data=df.to_dict('records'),
    id='table',    columns=[{"name": i, "id": i} for i in df.columns],
)

a_table_styled = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],

    style_cell_conditional=[
        {
            'if': {'column_id': c},
            'textAlign': 'left'
        } for c in ['Date', 'Region']
    ],
    style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(248, 248, 248)'
        },
        {
            'if': {
                'column_id': 'Number of Solar Plants',
                'filter_query': '{Number of Solar Plants} > 100'
            },
            'backgroundColor': '#3D9970',
            'color': 'white',
        }
    ],
    style_header={
        'backgroundColor': 'rgb(230, 230, 230)',
        'fontWeight': 'bold'
    }
)


card_content = [
    dbc.CardHeader("Card header"),
    dbc.CardBody(
        [
            html.H5("Card title", className="card-title"),
            html.P(
                "This is some card content that we'll reuse",
                className="card-text",
            ),
        ]
    ),
]


app.layout = html.Div([
            dbc.Container([
                html.Br(),
                html.H1('Dash - Table'),
                a_table,
                html.H1('Dash - Table styled'),
                a_table_styled,
                html.H1('Dash Bootstrap Component - Cards'),
                 dbc.Row(
                    [
                        dbc.Col(dbc.Card(card_content, color="success", inverse=True)),
                        dbc.Col(dbc.Card(card_content, color="warning", inverse=True)),
                        dbc.Col(dbc.Card(card_content, color="danger", inverse=True)),
                    ],
                    className="mb-4",
                ),
    ])
])


if __name__ == "__main__":
    app.run_server(debug=True)
