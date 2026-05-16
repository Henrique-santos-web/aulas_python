import sqlite3

def conectar():
    return sqlite3.connect("clientes_app.db")


def criar_tabela():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL
                )
        """)

        conexao.commit()
    except sqlite3.Error as erro:
        print(f"OCORREU UM ERRO: {erro}")
    finally:
        if conexao:
            conexao.close()


if __name__ == "__main__":
    criar_tabela()