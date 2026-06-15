# BLUEPRINT figurinhas — pluga as rotas /figurinhas/ no Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .base import ModeloBase
from .colecionador import Colecionador
from .figurinha import Figurinha
from .oferta import OfertaTroca, ItemOferta
app = Flask(__name__)

__all__ = ["db", "ModeloBase", "Colecionador", "Figurinha", "OfertaTroca", "ItemOferta"]
from controllers.figurinhas_controller import figurinhas_bp
app.register_blueprint(figurinhas_bp)


# layout.html: url_for('figurinhas.index')
