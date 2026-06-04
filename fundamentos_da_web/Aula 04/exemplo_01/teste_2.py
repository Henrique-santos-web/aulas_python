from flask import Flask, jsonify

app = Flask(__name__)

PRODUTOS = [
    {"id" : 1, "nome": "Notebook", "preco": 5000.0},
    {"id" : 2, "nome": "Mouse", "preco": 150.0},
    {"id" : 3, "nome": "Teclado", "preco": 350.0}
]

@app.route("/api/produtos", methods=["GET"])
def index():
    return jsonify({
        "produtos" : PRODUTOS,
        "total" : len(PRODUTOS)
    }), 200

@app.route("/api/produto/<int:id_produtos>", methods=["GET"])
def obter_produto(id_produto):
    produto_encontrado = None
    for produto in PRODUTOS:
        if produto["id"] == id_produto:
            produto_encontrado = produto
            break

    if produto_encontrado is None:
        return jsonify({
            "erro": "PRODUTO_NAO_ENCONTRADO",
            "mensagem" : f"ID {id_produto} inexistente"
        }), 404

    return jsonify(produto_encontrado), 200


if __name__ == "__main__":
    app.run(debug=True)