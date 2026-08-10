from . import db

from datetime import datetime

class ModeloBase(db.Model):
    """
    Superclasse abstrata — não vira tabela no banco.
    Cliente, Pedido etc. herdam id e datas sem repetir código.
    """

    # __abstract__ = True  →  "sou molde, não vire tabela modelo_base no SQLite"
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    data_criacao = db.Column(
        db.DateTime, default=datetime.now, nullable=False
    )