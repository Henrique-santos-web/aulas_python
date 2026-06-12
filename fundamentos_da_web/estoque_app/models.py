from extensions import db

class Produto(db.Model):
    __tablename__ = "produtos"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(80), nullable=False)
    preco = db.Column(db.Float(120), unique=True, nullable=False)
    quantidade = db.Column(db.Intenger, nullable=False)

    def to_dict(self):
        return {"id" : self.id, "nome" : self.nome, "preco" : self.preco, "quantidade": self.quantidade}
