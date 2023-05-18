# Importando Bibliotecas ==============================================================================================
from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user


# Importando Páginas e Elementos ======================================================================================
from app import *


# =========  página de login completa  =========== #

def render_layout(message):
    message = "Ocorreu algum erro durante o login" if message == 'error' else message
    # =========  Layout da Página  =========== #
    login_user_layout = html.Div([
        dbc.Card([

            dbc.Row([
                dbc.Col([
                    html.Legend("Login", className="Legend-Login-Card"),
                ], md=8),
                dbc.Col([
                    html.Img(id="logo", src=app.get_asset_url("DW_transp_amarelo.png"), className="Img-Login-DataView")
                ], md=4)
            ]),

            dbc.Row([
                dbc.Col([
                    html.Br(),
                    dbc.Input(id="user_login", placeholder="Username", type='text', size="sm"),
                    html.Br(),
                    dbc.Input(id="pwd_login", placeholder="Password", type='password', size="sm"),
                    html.Br(),
                    dbc.Button("Login", className="Button-Login-Card", id="login_button", size="sm", n_clicks=0),
                ], md=12)
            ]),

            dbc.Row([
                dbc.Col([
                    html.Span(message, className="Span-Login"),
                    html.Div([
                        html.Label("Ou", style={"margin-right": "5px"}),
                        dcc.Link("Registre-se", href="/register", style={"color": "gray"}),
                    ], style={"padding": "20px", "justify-content": "center", "display": "flex"})
                ], md=12)
            ])
        ], className="Login-Box")
    ], className="Div-Login")

    # =========  Renderizar a Página  =========== #
    layout_page = dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.Img(id="logo", src=app.get_asset_url("logoD7PAR_Branca.png"), className="layout-page-login-img-D7PAR"),
                    html.H1('Business Transformation - Business Modelling',className="layout-page-login-h1-1"),
                    html.H1('Corporate Finance & Artificial Intelligence', className="layout-page-login-h1-2"),
                    html.H2('Data Science Team', className="layout-page-login-h2"),
                        ])
                    ], md=12, style={'margin-left': '1%'})
                ]),
        html.Br(),
        dbc.Row([
            dbc.Col([
                html.Div(children=login_user_layout)], md=12)
                ]),
        html.Br(),
        dbc.Row([
            dbc.Col([
                dmc.Blockquote("Everything we hear is an opinion, not a fact. Everything we see is a perspective, not the truth.",
                               cite="- Marcus Aurelius , Meditations",
                               className="layout-page-login-blockquote")
                    ], md=12)
                ]),
        ], className="Container-Login", fluid=True)
    return layout_page


# =========  Callback Login User - Função de Login dentro da página template login  =========== #

@app.callback(
    Output(component_id='login-state', component_property='data'),
    Input(component_id='login_button', component_property='n_clicks'),
    [State(component_id='user_login', component_property='value'),
    State(component_id='pwd_login', component_property='value')],
    )
def successful(n_clicks, username, password):
    if n_clicks == None:
        raise PreventUpdate

    user = Users.query.filter_by(username=username).first()

    if user and password is not None:
        if check_password_hash(user.password, password): # se o password do usuário comparando com o password que passamos for igual, ele executa abaixo o login
            login_user(user) # logar o usuário
            return "success"
        else:
            return "error"
    else:
        return "error"





# TODO: user = Users.query.filter_by(username=username).first()         Retorna um id do usuário com o que ele encontrou dentro da base de dados. Se não econtrar ninguém, ele volta nan