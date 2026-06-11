from flask import Flask, request, jsonify
from extensions import db 
from models import Usuario

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///empresa.db"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db.init_app(app)


with app.app_context():
    db.create_all()
    print("Banco de dados e tabela criadas com sucesso!")


@app.route("/api/usuarios", methods="POST")
def criar_usuario():
    dados = request.get_json()

    novo_usuario = Usuario(nome=dados["nome"], email=dados["email"])

    db.session.add(novo_usuario)
    db.session.commit()

    return jsonify(novo_usuario.to_dict()), 201

@app.route("/api/usuarios", methods="GET")
def listar_usuarios():
    usuarios = Usuario.query.all()

    lista_json = [usuario.to_dict() for usuario in usuarios] # * transforme usuario em dicionario para(for) cada usuario em(in) usuarios

    return jsonify(lista_json), 200

if __name__ == "__main__":
    app.run(debug=True)