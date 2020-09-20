
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# Define app
app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1.0"}], external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
map_fig = px.scatter_mapbox(df, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Population"],color_discrete_sequence=["red"], zoom=4)
map_fig.update_layout(mapbox_style="open-street-map")
map_fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})



card_content = [
    dbc.CardHeader("Agent Name"),
    dbc.CardBody(
        [
            html.H5("Action", className="card-title"),
            html.P(
                "Here goes some action description",
                className="card-text",
            ),
        ]
    ),
]

cards = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dbc.Card(card_content,id="Agent1",color="success", inverse=True,style={"margin-top": 10})),
                dbc.Col(dbc.Card(card_content,id="Agent2", color="warning", inverse=True,style={"margin-top": 10})),
                dbc.Col(dbc.Card(card_content,id="Agent3", color="danger", inverse=True,style={"margin-top": 10})),
            ],
            className="mb-4",
        )
    ]
)

controls = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label("Parameter 1"),
                dcc.Slider(
                    id="p-1",
                    min=0,
                    max=100,
                    value=30,
                    marks={i: str(i) for i in range(10, 101, 10)},
                ),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Parameter 2"),
                dcc.Slider(
                    id="p-2",
                    min=0,
                    max=100,
                    value=20,
                    marks={i: str(i) for i in range(10, 101, 10)},
                ),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Parameter 3"),
                dcc.Slider(
                    id="p-3",
                    min=0,
                    max=100,
                    value=20,
                    marks={i: str(i) for i in range(10, 101, 10)},
                ),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Spinner(
                    [
                        dbc.Button("Run Simulation", id="button-run",n_clicks=0)
                    ]
                )
            ]
        ),
    ],
    body=True,
    style={'height':'330px','background': '#7FDBFF'},
)

# Define Layout
app.layout = dbc.Container(
    fluid=True,
        style={'background': '#DAF7A6','textAlign': 'center'},
    children=[
        html.H1("Covid-19 Critical Infrastructure Resilience Simulation", style={'textAlign': 'center',}),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    width=5,
                    children=[
                        controls,
                        dbc.Card(
                            body=True,
                                style={"background": "#FFFFFF","margin-top": 5},
                            children=[
                                dbc.FormGroup(
                                    [
                                        dcc.Graph(id="summarized-content",
                                        style={"background": "#7FDBFF","width": "100%","height": "calc(75vh - 330px)"})
                                    ]
                                )
                            ],
                        )
                    ],
                ),
                dbc.Col(
                    width=7,
                    children=[
                        dbc.Card(
                            body=True,
                                style={"background": "#7FDBFF"},
                            children=[
                                dbc.FormGroup(
                                    [
                                        dcc.Graph( figure=map_fig,
                                                   id="map-fig",
                                                   style={"height": "45vh"},)
                                    ]
                                )
                            ],
                        ),
                    cards
                    ],
                ),
            ]
        ),
    ],
)


@app.callback(
    [Output("Agent1", "color"),Output("Agent2", "color"),Output("Agent3", "color")],
    [
        Input("button-run", "n_clicks")
    ],
)
def summarize(n_clicks):
    if n_clicks%2 == 0:
        return 'success','warning','danger'
    else:
        return 'danger','success','warning'


if __name__ == "__main__":
    app.run_server()

