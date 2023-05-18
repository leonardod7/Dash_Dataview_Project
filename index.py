# Importando Bibliotecas ==============================================================================================
from dash import html, dcc
from dash.dependencies import Input, Output, State
from styles.styles_index import *
from flask_login import current_user


# Importando Páginas e Elementos ======================================================================================
from app import *
from pages import login, home, register


# Instanciando o Login ================================================================================================
login_manager = LoginManager()
login_manager.init_app(server) # inicie o app baseado no servidor.
login_manager.login_view = '/login' # estamos dizendo que a página padrão de visita do login é essa.


# Criando o app =======================================================================================================
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dcc.Location(id="base-url", refresh=False),
            dcc.Store(id='login-state', data=""),
            dcc.Store(id='register-state', data=""),
            html.Div(id="page-content", children=[]),
                ], md=12)
            ]),
        ], fluid=True)


# 1) Callback =========================================================================================================
# Vamos criar um callback fazer o load do usuário que será buscado no banco de dados
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


# 2) Callback =========================================================================================================
# Vamos criar um callback para que o output desse callback seja a URL e o input sejam os estados (no outro callback)
@app.callback(Output(component_id="base-url", component_property="pathname"),
              [Input(component_id="login-state", component_property="data"),
               Input(component_id="register-state", component_property="data")])
def render_page_content(login_state, register_state):
    ctx = dash.callback_context
    if ctx.triggered:
        trigg_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if trigg_id == 'login-state' and login_state == "success":
            return '/home'
        if trigg_id == 'login-state' and login_state == "error":
            return '/login'

        elif trigg_id == 'register-state':
            print(register_state, register_state == '')
            if register_state == "":
                return '/login'
            else:
                return '/register'
    else:
        return '/'


# 3) Callback =========================================================================================================
# Só é chamado quando temos uma troca de URL. Ele recebe o input dos estados
@app.callback(
            Output(component_id="page-content", component_property="children"),
            Input(component_id="base-url", component_property="pathname"),
            [State(component_id="login-state", component_property="data"),
             State(component_id="register-state", component_property="data")]
              )
def render_page_content(pathname, login_state, register_state):
    if (pathname == "/login" or pathname == "/"):
        return login.render_layout(login_state)

    if pathname == "/register":
        return register.render_layout(register_state)

    if pathname == "/home":
        if current_user.is_authenticated: # Se o current user estiver autenticado:
            return home.render_layout(current_user.username)
        else:
            return login.render_layout(register_state)


if __name__ == "__main__":
    app.run_server(debug=True, port=8005)


# 3) Callback =========================================================================================================
# Só é chamado quando temos uma troca de URL. Ele recebe o input dos estados
# @app.callback(
#             [Output(component_id="page-content", component_property="children"),
#              Output(component_id="page-content", component_property="style")],
#             Input(component_id="base-url", component_property="pathname"),
#             [State(component_id="login-state", component_property="data"),
#              State(component_id="register-state", component_property="data")]
#               )
# def render_page_content(pathname, login_state, register_state):
#     if (pathname == "/login" or pathname == "/"):
#         return login.render_layout(login_state), div_style_index_login_register # estamos passando o login_state para renderizar na hora que fizemos o login
#
#     if pathname == "/register":
#         return register.render_layout(register_state), div_style_index_login_register
#
#     if pathname == "/home":
#         if current_user.is_authenticated: # Se o current user estiver autenticado:
#             return home.render_layout(current_user.username), div_style_index_home  # Vamos permitir que renderize esse layout, acessando o elemento current_user passando o username
#         else:
#             return login.render_layout(register_state), div_style_index_login_register # se não, volte para a página de login
