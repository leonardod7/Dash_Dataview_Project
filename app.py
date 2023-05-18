# Importando Bibliotecas ==============================================================================================
import dash
import dash_bootstrap_components as dbc
import sqlite3
from sqlalchemy import Table, create_engine
from sqlalchemy.sql import select

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
import os #sistema operacional


# Criando Conexão com o Banco de Dados ================================================================================
conn = sqlite3.connect('data.sqlite')
engine = create_engine('sqlite:///data.sqlite')
db = SQLAlchemy()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
Users_table = Table('users', Users.metadata)


#  Instanciando o app =================================================================================================
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SLATE])
server = app.server
app.config.suppress_callback_exceptions = True     # TODO: Restringe erros de callback

server.config.update(
    SECRET_KEY=os.urandom(12), # chave para que o nosso servidor ele consiga ter uma informacao de criptografia para garantir que a sessao esta sendo salva de forma adequada. Estamos gerando uma chave aleatória
    SQLALCHEMY_DATABASE_URI='sqlite:///data.sqlite',
    SQLALCHEMY_TRACK_MODIFICATIONS=False) # Não monitore as modificações que foram feitas

# Iniciar o nosso banco de dados (SQLAlchemy) utilizando o servidor que acabamos de modificar conforme configurações acima
db.init_app(server)

# Vamos criar uma classe que é uma classe representativa mais simples, que vai ter uma estrutura básica de usuários que o nosso flask login vai fazer o uso depois
# Ela herda 2 classes. UserMixmin é uma classe feita pelo flask para que tudo funcione bem. Users é a nossa tabela que criamos no banco de dados
class Users(UserMixin, Users):
    pass