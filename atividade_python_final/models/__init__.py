from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .base import ModeloBase
from .tarefas import Tarefas
from .usuarios import Usuarios

__all__ = ["db", "ModeloBase", "Usuarios", "Tarefas"]