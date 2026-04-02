perfil = {
    "nome" : "Henrique Dos Santos Miranda",
    "idade" : 20,
    "email" : "miranda.3bpe@gmail.com"
}

print(f"Olá, {perfil['nome']}, vi que você tem {perfil['idade']} anos e seu e-mail é {perfil['email']}")

perfil.pop("email")

print(perfil)