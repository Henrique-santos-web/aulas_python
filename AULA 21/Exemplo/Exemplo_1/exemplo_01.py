import sqlite3


try:
    conexao = sqlite3.Connection("meu_banco.db")

    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER
    )
    """)
    conexao.commit()
    print("Banco configurado!")
except sqlite3.Error as erro:
    print(f"Erro: {erro}")
finally:
    if conexao:
        conexao.close()

# * isso é um banco de dados que fica dentro de uma função (deve, pelo menos), pra salvar as funções.
# ! sempre coloque p try, except e finally