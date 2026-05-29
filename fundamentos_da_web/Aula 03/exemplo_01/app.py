from flask import Flask, request

app = Flask(__name__)

@app.route('/dobro/<int:numero>')
def calculadora(numero): #* tem que ser igual ao numero dentro do route
    return f"resultado {numero} é {numero * 2}"
    # * aqui o comando é http://127.0.0.1:5000/dobro/*o numero que sera multiplicado por 2

@app.route("/loja")
def listar_produtos():
    categoria = request.args.get("categoria")

    if categoria:
        return f"Mostrando produtos: {categoria}"
    else:
        return "Mostrando todos os produtos"
    
    #* http://127.0.0.1:5000/loja?categoria=*nome do produto
    # * aqui só funciona esse comando ao usar o request 


if __name__ == "__main__":
    app.run(debug=True)