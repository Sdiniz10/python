from . import db
from .base import ModeloBase


class Usuarios(ModeloBase):
    __tablename__ = "usuario"

    nome = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    senha =  db.Column(db.String(20), nullable=False)

    tarefas = db.relationship('Tarefas', back_populates='usuario')
    @classmethod
    def listar_com_detalhes(cls):
        return cls.query.order_by(cls.nome).all()
