from . import db
from .base import ModeloBase
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base


class OfertaTroca(ModeloBase):
    __tablename__ = "ofertas_troca"

    # TODO ALUNO: FK colecionador_id → colecionadores.id
    id_oferta = db.Column(Integer, primary_key=True)
    observacao = db.Column(db.String(255), nullable=True)
    itens = Column(Integer, ForeignKey('oferta.id_figurinha'))
    colecionadores = relationship("colecionador", back_populates="ofertas")
    # TODO ALUNO: relationship colecionador, itens

    @classmethod
    def listar_com_colecionador(cls):
        return cls.query.order_by(cls.data_criacao.desc()).all()


class ItemOferta(ModeloBase):
    __tablename__ = "itens_oferta"

    # TODO ALUNO: FK oferta_id, FK figurinha_id
    tipo = db.Column(db.String(20), nullable=False)  # "oferece" ou "deseja"
    quantidade = db.Column(db.Integer, nullable=False, default=1)
    id_oferta = Column(Integer, ForeignKey('oferta.id_oferta'))
    id_figurinha = Column(Integer, ForeignKey('figurinha.id_figurinha'))
    ofertas = relationship("oferta", back_populates="figurinha")
    figurinhas = relationship("figurinha", back_populates="oferta")

    # TODO ALUNO: relationship oferta, figurinha
