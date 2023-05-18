# Esse arquivo teste serve para testarmos o conteúdo que foi criado no banco de dados e verificar se os dados foram cadastrados

import pandas as pd
c = conn.cursor()
df = pd.read_sql('select * from users', conn)
df