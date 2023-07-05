#Puxar uma query usando Python

import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('nome_do_banco_de_dados.db')

# Criar um cursor
cursor = conn.cursor()

# Executar uma query
query = "SELECT * FROM nome_da_tabela"
cursor.execute(query)

# Recuperar os resultados da query
results = cursor.fetchall()

# Exibir os resultados
for row in results:
    print(row)

# Fechar a conexão com o banco de dados
conn.close()


#Lembre-se de substituir 'nome_do_banco_de_dados.db' pelo nome do arquivo do seu banco de dados e 'nome_da_tabela' pelo nome da tabela que você deseja consultar.
