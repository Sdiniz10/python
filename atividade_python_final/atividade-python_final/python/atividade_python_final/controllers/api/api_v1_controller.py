from flask import Blueprint, jsonify, request

from models import Tarefas, Usuarios, db
from models.tarefas import STATUS_VALIDOS

api_v1_bp = Blueprint("api_v1", __name__, url_prefix="/api/v1")


@api_v1_bp.route("/tarefas", methods=["GET"])
def api_listar_todas():
    return jsonify([t.como_dicionario() for t in Tarefas.listar_com_detalhes()])


@api_v1_bp.route("/dashboard/<int:usuario_id>", methods=["GET"])
def api_listar_tarefas(usuario_id):
    Usuarios.query.get_or_404(usuario_id)
    return jsonify([t.como_dicionario() for t in Tarefas.listar_do_usuario(usuario_id)])


@api_v1_bp.route("/registro", methods=["POST"])
def api_registrar():
    dados = request.get_json(silent=True)
    if not dados:
        return jsonify({"erro": "Envie JSON no body"}), 400
    usuario, erro = Usuarios.registrar(
        dados.get("nome"), dados.get("email"), dados.get("senha")
    )
    if erro:
        return jsonify({"erro": erro}), 400
    return jsonify({"id": usuario.id, "mensagem": "Usuário criado"}), 201


@api_v1_bp.route("/login", methods=["POST"])
def api_login():
    dados = request.get_json(silent=True)
    if not dados:
        return jsonify({"erro": "Envie JSON no body"}), 400
    usuario, erro = Usuarios.autenticar(dados.get("email"), dados.get("senha"))
    if erro:
        return jsonify({"erro": erro}), 401
    return jsonify({"id": usuario.id, "nome": usuario.nome}), 200


@api_v1_bp.route("/nova_tarefa", methods=["POST"])
def api_criar_tarefa():
    dados = request.get_json(silent=True)
    if not dados:
        return jsonify({"erro": "Envie JSON no body"}), 400

    tarefa, erro = Tarefas.criar(
        titulo=dados.get("titulo"),
        descricao=dados.get("descricao"),
        status=dados.get("status", "Pendente"),
        usuario_id=dados.get("usuario_id"),
    )
    if erro:
        return jsonify({"erro": erro}), 400
    return jsonify({"id": tarefa.id, "mensagem": "Tarefa criada"}), 201


@api_v1_bp.route("/editar/<int:tarefa_id>", methods=["PUT"])
def api_editar_tarefa(tarefa_id):
    dados = request.get_json(silent=True)
    if not dados:
        return jsonify({"erro": "Envie JSON no body"}), 400

    tarefa = Tarefas.query.get_or_404(tarefa_id)
    if "titulo" in dados:
        tarefa.titulo = str(dados["titulo"]).strip()
    if "descricao" in dados:
        tarefa.descricao = str(dados["descricao"]).strip()
    if "status" in dados:
        if dados["status"] not in STATUS_VALIDOS:
            return jsonify({"erro": "Status inválido"}), 400
        tarefa.status = dados["status"]

    db.session.commit()
    return jsonify({"id": tarefa.id, "mensagem": "Tarefa atualizada"}), 200


@api_v1_bp.route("/deletar/<int:tarefa_id>", methods=["DELETE"])
def api_deletar_tarefa(tarefa_id):
    tarefa = Tarefas.query.get_or_404(tarefa_id)
    try:
        db.session.delete(tarefa)
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"erro": "Não foi possível deletar a tarefa"}), 500
    return jsonify({"id": tarefa_id, "mensagem": "Tarefa deletada"}), 200


@api_v1_bp.route("/tarefas/status", methods=["GET"])
def api_contagem_status():
    return jsonify(
        {
            "pendente": Tarefas.query.filter_by(status="Pendente").count(),
            "em andamento": Tarefas.query.filter_by(status="Em andamento").count(),
            "concluida": Tarefas.query.filter_by(status="Concluida").count(),
        }
    )
