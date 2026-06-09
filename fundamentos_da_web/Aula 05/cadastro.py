from flask import Flask, request, jsonify

app = Flask(__name__)

LISTA_CADASTRO = []

@app.route("/api/produtos", methods=["GET"])
def cadastrar():
    dados = request.get_json()

    novo_email = {
        "id" : len(LISTA_CADASTRO) + 1,
        "email" : dados["email"]
    }

    LISTA_CADASTRO.append(novo_email)

    return jsonify(novo_email), 201

if __name__ == "__main__":
    app.run(debug=True)