from sqlalchemy import Column, Integer, String
from database import Base, Session, engine

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String)


Base.metadata.create_all(engine)