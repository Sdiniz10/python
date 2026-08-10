from . import db
from .base import ModeloBase


class Tarefas(ModeloBase):
    __tablename__ = "tarefa"

    titulo = db.Column(db.String(60), nullable=False)
    descricao = db.Column(db.String(150), nullable=False)
    status = db.Column (db.String, nullable = False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable = False)
    # TODO ALUNO: relationship ofertas
    usuario = db.relationship('Usuarios', back_populates='tarefas')
    @classmethod
    def listar_com_detalhes(cls):
        return cls.query.order_by(cls.titulo).all()
