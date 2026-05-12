import sqlite3
try:
    conexao = sqlite3.Connection("loja.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            preco FLOAT
)
""")
    print("Loja configurada")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS fornecedor (
        id PRIMARY KEY AUTOINCREMENT,
        empresa TEXT, telefone TEXT
)
""")
    conexao.commit()
    print("Fornecedor criado")
except sqlite3.Error as erro:
    print(f"ERRO: {erro}")
finally:
    if conexao:
        conexao.close()