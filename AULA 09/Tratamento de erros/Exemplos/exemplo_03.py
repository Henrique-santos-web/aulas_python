try:
    senha = int(input("Senha..."))
    print("Processando acesso")

except ValueError:
    print("Formato Inválido")

finally:
    print("Encerrando verificação...")