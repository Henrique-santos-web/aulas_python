from flask import Flask, jsonify

app = Flask(__name__)

PRODUTOS = [
    {"id" : 1, "nome": "Notebook", "preco": 5000.0},
    {"id" : 2, "nome": "Mouse", "preco": 150.0},
    {"id" : 3, "nome": "Teclado", "preco": 350.0}
]

@app.route("/", method="GET")
def index():
    return jsonify(PRODUTOS)

if __name__ == "__main__":
    app.run(debug=True)