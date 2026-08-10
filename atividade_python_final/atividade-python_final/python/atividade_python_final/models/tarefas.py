from . import db
from .base import ModeloBase

STATUS_VALIDOS = ["Pendente", "Em andamento", "Concluida"]


class Tarefas(ModeloBase):
    __tablename__ = "tarefa"

    titulo = db.Column(db.String(60), nullable=False)
    descricao = db.Column(db.String(150), nullable=False)
    status = db.Column(db.String(20), nullable=False, default="Pendente")
    usuario_id = db.Column(
        db.Integer, db.ForeignKey("usuario.id"), nullable=False, index=True
    )

    usuario = db.relationship("Usuarios", back_populates="tarefas")

    @classmethod
    def criar(cls, titulo, descricao, status, usuario_id):
        """Salva uma nova tarefa no banco. Retorna (tarefa, erro)."""
        titulo = (titulo or "").strip()
        descricao = (descricao or "").strip()
        status = (status or "Pendente").strip()
        if not titulo or not descricao:
            return None, "Informe título e descrição."
        if status not in STATUS_VALIDOS:
            return None, "Status inválido."
        if not usuario_id:
            return None, "Selecione o usuário responsável."

        tarefa = cls(
            titulo=titulo,
            descricao=descricao,
            status=status,
            usuario_id=int(usuario_id),
        )
        db.session.add(tarefa)
        db.session.commit()
        return tarefa, None

    @classmethod
    def listar_com_detalhes(cls):
        return cls.query.order_by(cls.data_criacao.desc()).all()

    @classmethod
    def listar_do_usuario(cls, usuario_id):
        return (
            cls.query.filter_by(usuario_id=usuario_id)
            .order_by(cls.data_criacao.desc())
            .all()
        )

    def como_dicionario(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "status": self.status,
            "usuario_id": self.usuario_id,
            "usuario": self.usuario.nome if self.usuario else None,
            "data_criacao": self.data_criacao.isoformat(),
        }
