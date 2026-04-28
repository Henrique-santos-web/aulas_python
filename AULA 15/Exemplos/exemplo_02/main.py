from Usuario import Usuario

cliente_01 = Usuario()
cliente_02 = Usuario()

if __name__ == "__main__":
    cliente_01.nome = "Joao"   
    cliente_01.idade = 23

    cliente_02.nome = "Fernanda"
    cliente_02.idade = 42


print(f"{cliente_01.nome} | {cliente_01.idade}")
print(f"{cliente_02.nome} | {cliente_02.idade}")