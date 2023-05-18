from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import *

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash_bootstrap_templates import load_figure_template
from styles.styles_login import *
from styles.styles_index import *


load_figure_template(["slate"])
card_style = {
    'width': '800px',
    'min-height': '300px',
    'padding-top': '25px',
    'padding-right': '25px',
    'padding-left': '25px',
}

df = pd.DataFrame(np.random.randn(100, 1), columns=["data"])
fig = px.line(df, x=df.index, y="data", template="slate")


# =========  Layout  =========== #
def render_layout(Leonardo):
    layout = dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.Img(id="logo", src=app.get_asset_url("logoD7PAR_Branca.png"), height=60,
                             style={'margin-top': "20px"}),
                    html.H1('Business Modelling', style=h1_1_style)
                        ]),
        html.Hr(style=hr_1_styles),
                    ], md=12)
                ])
    ], fluid=True)

    return layout


