from flask import Blueprint, redirect, render_template, request, url_for

from models import Tarefas, Usuarios

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/")
def index():
    return render_template(
        "index.html",
        total_usuarios=Usuarios.query.count(),
        total_tarefas=Tarefas.query.count(),
    )
    