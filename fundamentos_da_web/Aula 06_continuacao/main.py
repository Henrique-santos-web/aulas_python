from database import sessao 
from models import Usuario

def cadastrar(nome, email):
    novo_usuario = Usuario(nome=nome, email=email + "@gmail.com")
    sessao.add(novo_usuario)
    sessao.commit()

    print("Novo cadastro realizado com sucesso!")


if __name__ == "__main__":
    cadastrar("Henrique", "miranda")