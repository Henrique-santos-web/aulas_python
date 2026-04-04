clientes = {
    "Pedro":"MG",
    "Julia":"SC",
    "Gabriel":"SP"
}

usuario = input("Qual a sua cidade? ").upper()

encontrado = False

for cliente, estado in clientes.items():
    if encontrado == True:  
        if usuario == estado:
            print(f"Olá, {cliente}")

if encontrado == False:
    print("Desculpe, não temos clientes neste estado ainda")