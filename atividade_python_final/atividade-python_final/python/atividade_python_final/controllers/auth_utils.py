from functools import wraps

from flask import flash, redirect, session, url_for

from models import Usuarios


def login_obrigatorio(view):
    """Bloqueia páginas que exigem usuário logado."""

    @wraps(view)
    def envelope(*args, **kwargs):
        if not session.get("usuario_id"):
            flash("Faça login para continuar.", "erro")
            return redirect(url_for("auth.login"))
        return view(*args, **kwargs)

    return envelope


def usuario_atual():
    usuario_id = session.get("usuario_id")
    if not usuario_id:
        return None
    return Usuarios.query.get(usuario_id)
