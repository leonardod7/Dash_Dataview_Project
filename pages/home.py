from dash import html, dcc
from dash.dependencies import Input, Output, State
from app import *
from styles.styles_index import *
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user
from dash.exceptions import PreventUpdate

# =========  Layout  =========== #
def render_layout(username):
    layout = dbc.Container([

        dcc.Location(id="home-url"), # isso vai permitir que eu altere o nome da página que estams
        html.Legend('Welcome to Dataview, {}!'.format(username), className="legend-home"),

        dbc.Row([
            dbc.Col([
                html.Div([
                    html.Img(id="logo", src=app.get_asset_url("DW_transp_amarelo.png"), className="img-dataview"),
                    html.Br(),
                        ]),
            ], md=12),

        dbc.Row([
            dbc.Col([
                html.Nav([
                    html.A("oi")
                ]),

                html.Div([
                ], className="menu")

            ], md=12)
        ]),


        html.Div([
            dbc.Button("Logout", id="logout_button", className="button-logout") #n_clicks=[] não podemos informar essa propriedade, se não ele faz logout
                ], style={"padding": "20px", "justify-content": "end", "display": "flex"})

                ])
        ],className="container-home", fluid=True)
    return layout


# =========  Callbacks Page1  =========== #
@app.callback(
    Output(component_id='home-url', component_property='pathname'),
    Input(component_id='logout_button', component_property='n_clicks'),
)
def successful(n_clicks):
    if n_clicks == None:
        raise PreventUpdate

    if current_user.is_authenticated: # se o usuário estiver autenticado:
        logout_user() # faz logout
        return '/login' # volta para a página de login
    else:
        return '/login' # do contrário, volta para a página login




# @app.callback(
#     Output(component_id='home-url', component_property='pathname'),
#     Input(component_id='logout_button', component_property='n_clicks'),
# )
# def successful(n_clicks):
#     if n_clicks == None:
#         raise PreventUpdate
#
#     if current_user.is_authenticated: # se o usuário estiver autenticado:
#         logout_user() # faz logout
#         return '/login' # volta para a página de login
#     else:
#         return '/login' # do contrário, volta para a página login


# =========  Layout  =========== #
# def render_layout(username):
#     layout = dbc.Container([
#         dcc.Location(id="home-url"), # isso vai permitir que eu altere o nome da página que estams
#         html.Legend('Welcome to Dataview, {}!'.format(username)),
#         dbc.Row([
#             dbc.Col([
#                 html.Div([
#                     html.Img(id="logo", src=app.get_asset_url("DW_transp_amarelo.png"), className="img-dataview"),
#                     html.Br(),
#                     html.H1('Home', style=h1_1_style)
#                         ]),
#                 html.Hr(style=hr_1_styles),
#                 html.Div([
#                     dbc.Button("Logout", id="logout_button") #n_clicks=[] não podemos informar essa propriedade, se não ele faz logout
#                         ], style={"padding": "20px", "justify-content": "end", "display": "flex"})
#                     ], md=12)
#                 ])
#         ], fluid=True)
#     return layout