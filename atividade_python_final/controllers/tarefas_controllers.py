from datetime import datetime

from flask import Blueprint, redirect, render_template, request, url_for

from models import Tarefas, Usuarios, db

tarefas_bp = Blueprint("tarefa", __name__, url_prefix="/tarefa")

@tarefas_bp.route("/dashboard")
def index():
    tarefas = tarefa.listar_com_detalhes()
    return render_template("templates/registro.html", tarefas = tarefas)


@tarefas_bp.route("/nova_tarefa", methods=["GET", "POST"])
def nova_tarefa():
    usuarios = usuarios.listar()

    if request.method == "POST":
        tar = tarefa(
            usuario_id=int(request.form["usuario_id"]),
            data_inicio=datetime.strptime(
                request.form["data_inicio"], "%Y-%m-%d"
            ).date(),
            data_fim=datetime.strptime(request.form["data_fim"], "%Y-%m-%d").date(),
        )
        db.session.add(tar)
        db.session.commit()
        return redirect(url_for("registro.index"))

    return render_template(
        "templates/login.html",
        usuarios = usuarios,
        
    )

