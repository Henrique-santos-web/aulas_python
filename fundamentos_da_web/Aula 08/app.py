from flask import Flask, request, jsonify
from extensions import db, cors
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash
from models import Usuario

app = Flask()

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///empresa.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

cors.init_app(app, resources={
    r"/api/*":{
        "origins": [
            "https://wwww.meusite.com"
        ]
    }
})

with app.app_context():
    db.create_all()
    print("Banco de dados e tabelas criadas com sucesso!")

@app.route("/api/usuarios", mathods=["POST"])
def criar_usuario():
    dados = request.get_json()