import sqlite3

conexao = sqlite3.Connection("loja.db")
cursor = conexao.cursor()

while True:
    def cadastrar_produto():
        try:

            #* Aqui cria os produtos (especificadamente o método Create (criar))
            nome_produto = input("Digite o nome do Produto: ")
            preco = float(input("Qual o valor do produto: "))

            cmd_sql = "INSERT INTO produtos (nome, preco) VALUES (?, ?)"

            cursor.execute(cmd_sql, (nome_produto, preco))
            conexao.commit()
            print("Produto cadastrado!")

        except sqlite3.Error as erro:
            print(f"ERRO: {erro}")

        except ValueError:
            print("Digite um valor válido para o produto!")

        finally:
            if conexao:
                conexao.close()

    def listar_produtos():
        try:

            #* Aqui chama os produtos (seleciona os produtos pelo for e printa no final)
            #* Pra ser mais especifico: aqui fica o método Read (ler(busca dos dados))
            cursor.execute("SELECT * FROM produtos")
            conexao.commit()

            #* Pra extrair os dados lidos pelo SELECT dentro do cursor e mandarmos para a variável, usamos os método fetchall() - Buscar todos
            dados = cursor.fetchall()

            for linha in dados:
                print(f"Produto: {linha[0]} | {linha[1]} | {linha[2]}")


        except sqlite3.Error as erro:
            print(f"ERRO: {erro}")

        except ValueError:
            print("Digite um valor válido para o produto!")

        finally:
            if conexao:
                conexao.close()


    def update_produto():
        try:
            id_produto = int(input("Digite o id do Produto: "))
            novo_preco = float(input("Qual o novo valor do produto: "))

            sql = "UPDATE produtos SET preco = ? WHERE id = ?"

            cursor.execute(sql, (novo_preco, id_produto))
            conexao.commit()

            if cursor.rowcount == 0:
                print("ERRO: Produto não encontrado")
            else:
                print(f"Sucesso! {cursor.rowcount} linha(s) alterada(s)")

        except sqlite3.Error as erro:
            print(f"ERRO: {erro}")

        except ValueError:
            print("Digite um valor válido para o produto!")

        finally:
            if conexao:
                conexao.close()

    # cadastrar_produto()
    # cadastrar_produto()    
    # cadastrar_produto()
    #? Mas pq foi comentado essas def's? Foram, pois os produtos já foram criados (primeiro desafio era criar o banco de dados e cadastras os produtos, o segundo era chamar eles)

    update_produto()