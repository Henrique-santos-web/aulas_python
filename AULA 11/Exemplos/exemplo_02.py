email = "contato@empresa.com"

if "@" in email and ".com" in email:
    print("É um email válido")

bloqueados = ["Carlos", "Ana"]
usuario = input("Usuario: ").lower()

if usuario in bloqueados:
    print("Acesso negado")
else:
    print("Acesso liberado")

# ! Verificar por que deu errado o código