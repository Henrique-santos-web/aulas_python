def hack_sistema():
    global senha 
    senha = "123456"


hack_sistema()
print(senha)


# "Ah, mas a variável está dentro de uma def". Meu amigo, quando se usa o "global" antes da variável, ela automaticamente se torna global
# mas ela pode facilmente se tornar um vício, e como qualquer vício, é algo ruim caso usado demasiadamente