import sqlite3
try:
    conexao = sqlite3.Connection("loja.db")
    cursor = conexao.cursor()

    def cadastrar_produto():
        nome_produto = input("Digite o nome do Produto: ")
        preco = float(input("Qual o valor do produto: "))

        cmd_sql = "INSERT INTO produtos (nome, preco) VALUES (?, ?)"

        cursor.execute(cmd_sql, (nome_produto, preco))
        conexao.commit()
        print("Produto cadastrado!")

    cadastrar_produto()
    cadastrar_produto()    
    cadastrar_produto()

except sqlite3.Error as erro:
    print(f"ERRO: {erro}")
finally:
    if conexao:
        conexao.close()