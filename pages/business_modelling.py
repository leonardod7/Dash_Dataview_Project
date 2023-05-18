from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import *
from dash_bootstrap_templates import load_figure_template
from styles.styles_index import *

active_label_style = {
    "background-color": '#ffcc00',
    'color': '#ffcc00',
    'border-color':'#ffcc00'
}

# =========  Layout  =========== #
def render_layout():
    layout = dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.Img(id="logo", src=app.get_asset_url("DW_transp_amarelo.png"), height=40,
                             style={'margin-top': "20px"}),
                    html.Br(),
                    html.H1('Business Modelling', style=h1_1_style_BM)
                        ]),
                html.Hr(style=hr_1_styles)
            ], md=12)
                ]),
        dbc.Row([
            dbc.Col([
                dbc.Tabs([

                    dbc.Tab([
                        html.Ul([
                            html.Li('xxxx'),
                        ]),
                    ], label='Disclaimer', style={'fontSize': '12px'}, active_label_style=active_label_style),

                    dbc.Tab([
                        html.Ul([
                            html.Li('xxxx'),
                        ])
                    ], label='Project Info', style={'fontSize': '12px'}, active_label_style=active_label_style),

                    dbc.Tab([
                        html.Ul([
                            html.Li('Revenues'),
                        ])
                    ], label='Operational Assumptions', style={'fontSize': '12px'}, active_label_style=active_label_style),

                    dbc.Tab([
                        html.Ul([
                            html.Li('Indirect Tax'),
                        ])
                    ], label='Financial Assumptions', style={'fontSize': '12px'}, active_label_style=active_label_style),

                    dbc.Tab([
                        html.Ul([
                            html.Li('Costs & Expenses'),
                        ])
                    ], label='Revenues', style={'fontSize': '12px'}, active_label_style=active_label_style),

                    dbc.Tab([
                        html.Ul([
                            html.Li('ROL & EBITDA'),
                        ])
                    ], label='Indirect Tax', style={'fontSize': '12px'}, active_label_style=active_label_style),

                    dbc.Tab([
                        html.Ul([
                            html.Li('ROL & EBITDA'),
                        ])
                    ], label='Costs', style={'fontSize': '12px'}, active_label_style=active_label_style),

                    dbc.Tab([
                        html.Ul([
                            html.Li('ROL & EBITDA'),
                        ])
                    ], label='Expenses', style={'fontSize': '12px'}, active_label_style=active_label_style),

                    dbc.Tab([
                        html.Ul([
                            html.Li('ROL & EBITDA'),
                        ])
                    ], label='Operational Results', style={'fontSize': '12px'}, active_label_style=active_label_style)

                ], style={'fontSize': '12px'})
                    ], md=12)
                ])
        ], fluid=True)

    return layout