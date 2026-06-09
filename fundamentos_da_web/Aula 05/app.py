from flask import Flask, request, jsonify

app = Flask(__name__)

LISTA_EMAILS = []

@app.route("/api/emails", methods=["POST"])
def cadastrar():
    dados = request.get_json()
    
    novo_email = {
        "id" : len(LISTA_EMAILS) + 1,
        "email" : dados["@gmail"],
    }

    LISTA_EMAILS.append(novo_email)

    return jsonify(novo_email), 201


@app.route("/api/emails", methods=["GET"])
def emails():

    return jsonify(LISTA_EMAILS), 200


if __name__ == "__main__":
    app.run(debug=True)