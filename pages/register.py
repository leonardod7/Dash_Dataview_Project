
# =========  Import Libraries  =========== #
from styles.styles_login import *
from styles.styles_index import *
from dash import html, dcc
import dash_mantine_components as dmc
from werkzeug.security import generate_password_hash
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
from app import *


# =========  Renderização da Página  =========== #
def render_layout(message):
    message = "Ocorreu algum erro durante o registro" if message == 'error' else message

    # =========  Layout da Página  =========== #
    login_register_layout = html.Div([
        dbc.Card([

            dbc.Row([
                dbc.Col([
                    html.Legend("Register", className="Legend-Register-Card")
                ], md=8),
                dbc.Col([
                    html.Img(id="logo", src=app.get_asset_url("DW_transp_amarelo.png"), height=30)
                ], md=4)
            ]),

            dbc.Row([
                dbc.Col([
                    html.Br(),
                    dbc.Input(id="user_register", placeholder="Username", type='text', size="sm"),
                    html.Br(),
                    dbc.Input(id="pwd_register", placeholder="Password", type='password', size="sm"),
                    html.Br(),
                    dbc.Input(id="email_register", placeholder="E-mail", type='email', size="sm"),
                    html.Br(),
                    dbc.Button("Registrar", className="Button-Register-Card", id="register-button", size="sm", n_clicks=0)
                ], md=12)
            ]),

            dbc.Row([
                dbc.Col([
                    html.Span(message, style=span),
                    html.Div([
                        html.Label("Or", style={"margin-right": "5px"}),
                        dcc.Link("Login", href="/login", style={"color": "gray"}),
                    ], style={"padding": "20px", "justify-content": "center", "display": "flex"})
                ], md=12)
            ])
        ], className="Register-Box")
    ], className="Div-Register")

    # =========  Renderizar a página de login com os elementos estáticos  =========== #
    layout_page = dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.Img(id="logo", src=app.get_asset_url("logoD7PAR_Branca.png"), height=60, style={'margin-top':"20px"}),
                    html.H1('Business Transformation - Business Modelling', style=h1_1_style),
                    html.H1('Corporate Finance & Artificial Intelligence', style=h1_2_style),
                    html.H2('Data Science Team', style=h2_1_style),
                        ])
                    ], md=12, style={'margin-left': '1%'})
                ]),
        html.Br(),
        dbc.Row([
            dbc.Col([
                html.Div(children=login_register_layout)
                    ], md=12)
                ]),
        html.Br(),
        dbc.Row([
            dbc.Col([
                dmc.Blockquote(
                    "Everything we hear is an opinion, not a fact. Everything we see is a perspective, not the truth.",
                    cite="- Marcus Aurelius , Meditations", style=blockquote_style)
                    ], md=12)
                ]),
        ], className="Container-Register", fluid=True)

    return layout_page



# =========  Callback Registrar Usuários  =========== #
@app.callback(
    Output(component_id='register-state', component_property='data'),
    Input(component_id='register-button', component_property='n_clicks'),

    [State(component_id='user_register', component_property='value'),
    State(component_id='pwd_register', component_property='value'),
    State(component_id='email_register', component_property='value')],
    )
def successful(n_clicks, username, password, email):
    if n_clicks == None:
        raise PreventUpdate

    if username is not None and password is not None and email is not None:
        hashed_password = generate_password_hash(password, method='sha256')
        ins = Users_table.insert().values(username=username,  password=hashed_password, email=email)
        conn = engine.connect()
        conn.execute(ins)
        conn.close()
        return ''
    else:
        return 'error'

# conn.commit() # Grava no banco