from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from models import Usuarios

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        usuario, erro = Usuarios.registrar(
            request.form.get("nome"),
            request.form.get("email"),
            request.form.get("senha"),
        )
        if erro:
            flash(erro, "erro")
            return render_template("registro.html"), 400

        session["usuario_id"] = usuario.id
        session["usuario_nome"] = usuario.nome
        flash("Conta criada com sucesso!", "sucesso")
        return redirect(url_for("tarefa.index"))

    return render_template("registro.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario, erro = Usuarios.autenticar(
            request.form.get("email"), request.form.get("senha")
        )
        if erro:
            flash(erro, "erro")
            return render_template("login.html"), 401

        session["usuario_id"] = usuario.id
        session["usuario_nome"] = usuario.nome
        flash(f"Bem-vindo, {usuario.nome}!", "sucesso")
        return redirect(url_for("tarefa.index"))

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    return render_template("logout.html")
