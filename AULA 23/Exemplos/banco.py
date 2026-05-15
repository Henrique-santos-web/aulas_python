import sqlite3
def conectar():
    return sqlite3.Connection("estoque_app.db")

def criar_tabela():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL
    )
    """)

        conexao.commit()
    except sqlite3.Error as erro:
        print(f"ERRO: {erro}")
    finally:
        if conexao:
            conexao.close()

def banco_estoque():
    try:
        conexao = conectar()
        cursos = conexao.cursor()
        cursos.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_produto TEXT NOT NULL,
                quantidade INTEGER NOT NULL
)
""")
        conexao.commit()
        return sqlite3.Connection("estoque_app.db")

    except sqlite3.Error as erro:
        print(f"ERRO: {erro}")
    finally:
        if conexao:
            conexao.close()

def buscar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM clientes")
    dados = cursor.fetchall()

    conexao.close()
    return dados


if __name__ == "__main__":
    banco_estoque()