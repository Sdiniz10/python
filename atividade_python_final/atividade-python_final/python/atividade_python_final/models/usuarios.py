from werkzeug.security import check_password_hash, generate_password_hash

from . import db
from .base import ModeloBase


class Usuarios(ModeloBase):
    __tablename__ = "usuario"

    nome = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True, index=True)
    senha = db.Column(db.String(255), nullable=False)

    tarefas = db.relationship(
        "Tarefas", back_populates="usuario", cascade="all, delete-orphan"
    )

    # --- Senha nunca é salva em texto puro ---
    def definir_senha(self, senha_pura: str) -> None:
        self.senha = generate_password_hash(senha_pura)

    def conferir_senha(self, senha_pura: str) -> bool:
        return check_password_hash(self.senha, senha_pura)

    @classmethod
    def buscar_por_email(cls, email: str):
        return cls.query.filter_by(email=(email or "").strip().lower()).first()

    @classmethod
    def registrar(cls, nome: str, email: str, senha: str):
        """Cria e salva um usuário no banco. Retorna (usuario, erro)."""
        nome = (nome or "").strip()
        email = (email or "").strip().lower()
        if not nome or not email or not senha:
            return None, "Preencha todos os campos."
        if len(senha) < 6:
            return None, "A senha deve ter ao menos 6 caracteres."
        if cls.buscar_por_email(email):
            return None, "Este e-mail já está cadastrado."

        usuario = cls(nome=nome, email=email)
        usuario.definir_senha(senha)
        db.session.add(usuario)
        db.session.commit()
        return usuario, None

    @classmethod
    def autenticar(cls, email: str, senha: str):
        usuario = cls.buscar_por_email(email)
        if usuario and usuario.conferir_senha(senha or ""):
            return usuario, None
        return None, "E-mail ou senha inválidos."

    @classmethod
    def listar_com_detalhes(cls):
        return cls.query.order_by(cls.nome).all()
