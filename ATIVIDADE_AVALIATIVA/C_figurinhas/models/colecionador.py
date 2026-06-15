from . import db
from .base import ModeloBase
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base



class Colecionador(ModeloBase):
    __tablename__ = "colecionadores"
    id_colecionador = db.Column(Integer, primary_key=True)
    apelido = db.Column(db.String(60), nullable=False)
    cidade = db.Column(db.String(80), nullable=False)
    # TODO ALUNO: relationship ofertas
    ofertas = relationship("oferta", back_populates="colecionador")
    @classmethod
    def listar(cls):
        return cls.query.order_by(cls.apelido).all()
