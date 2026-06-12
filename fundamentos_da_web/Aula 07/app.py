from flask import Flask, request, jsonify
from extensions import db
from sqlalchemy.exc import IntegrityError
from models import Usuario

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///empresa.db"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db.init_app(app)


with app.app_context():
    db.create_all()
    print("Banco de dados e tabela criadas com sucesso!")


@app.route("/api/usuarios", methods=["POST"])
def criar_usuario():
    dados = request.get_json()

    if 

    novo_usuario = Usuario(nome=dados["nome"], email=dados["email"])

    db.session.add(novo_usuario)
    db.session.commit()


    return jsonify(novo_usuario.to_dict()), 201

@app.route("/api/usuarios", methods=["GET"])
def listar_usuarios():
    usuarios = Usuario.query.all()

    lista_json = [usuario.to_dict() for usuario in usuarios] # * transforme usuarios em dicionario para(for) cada usuario em(in) usuarios

    return jsonify(lista_json), 200


@app.route("/api/usuarios/<int:id>", methods=["PUT"])
def atualizar_usuario(id):
    user = Usuario.query.get_or_404(id)
    dados = request.get_json()

    user.nome = dados["nome"]
    user.email = dados["email"]

    db.session.commit()

    return jsonify({"mensagem" : "Atualizar"}), 200

@app.route("/api/usuarios", methods=["PATCH"])
def atualizar_parcial(id):
    user = Usuario.query.get_or_404(id)
    dados = request.get_json()

    if "nome" in dados:
        user.nome = dados["nome"]
    if "nome" in dados:
        user.email = dados["email"]

    db.session.commit()
    return jsonify({"mensagem" : "Registro Ajustado"}), 200


@app.route("/api/usuarios", methods=["DELETE"])
def deletar_usuario(id):
    user = Usuario.query.get_or_404(id)
    dados = request.get_json() # * no delete não é usado esse comando, pois esse comando serve pra pegar um corpo (comando em dicionario do postman no body -> row)

    db.session.delete(user)
    db.session.commit()

    return jsonify({"mensagem" : "Registro deletado"}), 200

@app.errorhandler(404)
def rota_nao_encontrada(erro):
    return jsonify({
        erro : "RONA_NAO_ENCONTRADA",
        "mensagem" : "O endpoint solicitado não existe"
    })


if __name__ == "__main__":
    app.run(debug=True)