from flask import Flask, request, jsonify
from extensions import db 
from models import Produto

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///estoque.db" # *Caminho para o banco de dados
app.config['SQLALCHEMY_TRACK_'] = False # *Essa config é pra não mostrar toda hora no terminal as transações no banco de dados
db.init_app(app)

with app.app_context():
    db.create_all()
    print("Banco de dados e tabela criadas com sucesso!")

@app.route("/api/produtos", methods="POST") 
def cadastrar_produto():
    dados = request.get_json()
    # *o request é uma requisição (dados enviado pelo usuario (neste caso aqui é enviado por nos pelo app postman) que está salvo dentro do Flask)
    # *chamamos essa requisição usando o command = request 
    # *e após o ponto é o formato que queremos esses dados (neste caso é em json) 

    novo_produto = Produto(nome=dados["nome"], preco=dados["preco"])

    db.session.add(novo_produto)
    db.session.commit()

    return jsonify(novo_produto.to_dict()), 201


@app.route("/api/produtos", methods="GET")
def listar_produto():
    produtos = Produto.query.all()

    lista_json = [produto.to_dict() for produto in produtos]

    return jsonify(lista_json), 200 # *por mais que convertemos para dicionario, usamos o jsonify para converter em json, pois ao enviar mesmo que em formato de dicionario, quem recebe vai receber em formato de texto normal e não em dicionario ou json
    # * De forma crua, ele está pegando os dados em formato de dict e retornando em jsonify
    # * e é muito importante a conversão dos dados em dict, pois se não quebra o jsonify


if __name__ == "__main__":
    app.run(debug=True)