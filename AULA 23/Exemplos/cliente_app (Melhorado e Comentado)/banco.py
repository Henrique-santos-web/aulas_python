# Importa o módulo nativo do Python para trabalhar com o banco de dados SQLite.
# O SQLite é um banco de dados leve que salva as informações em um único arquivo local.
import sqlite3

def conectar():
    """
    Estabelece e retorna uma conexão com o banco de dados.
    Se o arquivo 'clientes_app.db' não existir, o sqlite3 o criará automaticamente na mesma pasta.
    """
    # A função connect() abre a comunicação com o arquivo do banco de dados
    return sqlite3.connect("clientes_app.db")


def criar_tabela():
    """
    Cria a tabela 'clientes' no banco de dados, definindo suas colunas e regras.
    Esta função deve ser executada apenas uma vez (ou sempre que o sistema iniciar) 
    para garantir que a estrutura onde os dados serão salvos exista.
    """
    try:
        # Abre a conexão usando o 'with'. Isso garante que a conexão será fechada e as 
        # alterações serão salvas (commit) automaticamente ao final do bloco, mesmo se der erro.
        with conectar() as conexao:
            
            # O cursor é o objeto responsável por executar os comandos SQL dentro do banco
            cursor = conexao.cursor()
            
            # Comando SQL para criar a tabela.
            # As aspas triplas (""") permitem escrever o comando em várias linhas para facilitar a leitura.
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes(
                    -- 'id' é um número inteiro. 
                    -- 'PRIMARY KEY' significa que é o identificador único (não existem dois iguais).
                    -- 'AUTOINCREMENT' faz o banco gerar esse número sozinho (1, 2, 3...) a cada novo cliente.
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    
                    -- 'nome' é um texto. 
                    -- 'NOT NULL' proíbe que o banco aceite salvar um cliente sem nome.
                    nome TEXT NOT NULL,
                    
                    -- 'email' é um texto. 
                    -- 'NOT NULL' proíbe salvar sem e-mail.
                    email TEXT NOT NULL
                )
            """)
            # Nota: Não precisamos colocar conexao.commit() nem conexao.close() aqui, 
            # pois o comando 'with' já faz isso automaticamente para nós.

    except sqlite3.Error as erro:
        # Se ocorrer qualquer problema com o banco de dados (ex: arquivo corrompido, bloqueado),
        # o programa não "crasha" imediatamente, mas exibe o erro no terminal.
        print(f"OCORREU UM ERRO NO BANCO: {erro}")


# ==========================================
# --- Ponto de Partida ---
# ==========================================

# Esta verificação garante que a tabela só seja criada automaticamente se você executar
# o arquivo 'banco.py' diretamente. 
# Quando o 'main.py' importar este arquivo (from banco import conectar), 
# este bloco 'if' NÃO será executado lá, evitando rodar a criação da tabela sem necessidade.
if __name__ == "__main__":
    criar_tabela()