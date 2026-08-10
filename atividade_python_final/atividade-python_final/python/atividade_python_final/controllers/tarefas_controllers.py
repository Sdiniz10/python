from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from models import Tarefas, Usuarios, db

from .auth_utils import login_obrigatorio

tarefas_bp = Blueprint("tarefa", __name__, url_prefix="/tarefa")


@tarefas_bp.route("/dashboard")
@login_obrigatorio
def index():
    """Lê do banco as tarefas do usuário logado."""
    tarefas = Tarefas.listar_do_usuario(session["usuario_id"])
    return render_template("tarefas/lista.html", tarefas=tarefas)


@tarefas_bp.route("/nova_tarefa", methods=["GET", "POST"])
@login_obrigatorio
def nova_tarefa():
    usuarios = Usuarios.listar_com_detalhes()

    if request.method == "POST":
        _, erro = Tarefas.criar(
            titulo=request.form.get("titulo"),
            descricao=request.form.get("descricao"),
            status=request.form.get("status"),
            usuario_id=request.form.get("usuario_id") or session["usuario_id"],
        )
        if erro:
            flash(erro, "erro")
            return (
                render_template(
                    "tarefas/formulario.html", usuarios=usuarios, tarefa=None
                ),
                400,
            )

        flash("Tarefa salva no banco!", "sucesso")
        return redirect(url_for("tarefa.index"))

    return render_template("tarefas/formulario.html", usuarios=usuarios, tarefa=None)


@tarefas_bp.route("/editar/<int:tarefa_id>", methods=["GET", "POST"])
@login_obrigatorio
def editar(tarefa_id):
    tarefa = Tarefas.query.get_or_404(tarefa_id)
    usuarios = Usuarios.listar_com_detalhes()

    if request.method == "POST":
        tarefa.titulo = (request.form.get("titulo") or "").strip()
        tarefa.descricao = (request.form.get("descricao") or "").strip()
        tarefa.status = request.form.get("status") or tarefa.status
        tarefa.usuario_id = int(request.form.get("usuario_id") or tarefa.usuario_id)
        db.session.commit()
        flash("Tarefa atualizada.", "sucesso")
        return redirect(url_for("tarefa.index"))

    return render_template("tarefas/formulario.html", usuarios=usuarios, tarefa=tarefa)


@tarefas_bp.route("/excluir/<int:tarefa_id>")
@login_obrigatorio
def excluir(tarefa_id):
    tarefa = Tarefas.query.get_or_404(tarefa_id)
    db.session.delete(tarefa)
    db.session.commit()
    flash("Tarefa excluída.", "sucesso")
    return redirect(url_for("tarefa.index"))
