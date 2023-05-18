# Devemos rodar apenas uma vez esse arquivo quando criarmos do zero o aplicativo. Ele constrói o banco de dados.


# =========  Import Libraries  =========== #
from sqlalchemy import Table, create_engine
from sqlalchemy.sql import select
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import warnings
import os


# Vamos criar uma conexão:
conn = sqlite3.connect('../data.sqlite')

# Vamos manter essa conexão ativa através do engine
engine = create_engine('sqlite:///data.sqlite') # echo = True    Esse parâmetro vai habilitar o debug log durante os acessos ao banco

# Vamos criar uma instância do SQLAlchemy
db = SQLAlchemy()

class Users(db.Model):
    # Vamos definir os campos do nossa tabela do banco de dados
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))


# Vamos criar uma instância dessa tabela
Users_table = Table('users', Users.metadata)

# função que vai pegar esse banco de dados que a gente criou e criar essa tabela:
def create_users_table():
    Users.metadata.create_all(engine)
create_users_table() # Vamos criar a tabela executando a função

## Esse conteúdo está no arquivo teste
# import pandas as pd
# c = conn.cursor()
# df = pd.read_sql('select * from users', conn)
# df