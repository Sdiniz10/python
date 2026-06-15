from . import db
from .base import ModeloBase
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base


class Figurinha(ModeloBase):
    __tablename__ = "figurinhas"
    id_figurinha = db.Column(Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False)
    nome_jogador = db.Column(db.String(100), nullable=False)
    time = db.Column(db.String(80), nullable=False)

    @classmethod
    def listar(cls):
        return cls.query.order_by(cls.numero).all()
