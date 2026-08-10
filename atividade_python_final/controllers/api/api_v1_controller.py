from datetime import datetime

from flask import Blueprint, jsonify, request

from models import Tarefas, Usuarios, db


api_v1_bp = Blueprint("api_v1", __name__, url_prefix="/api/v1")


@api_v1_bp.route("/dashboard/<int:usuario_id>", methods=["GET"]) 
def api_listar_tarefas():
    tarefas = tarefa.listar_com_detalhes()
    return jsonify([
        {
            "id": tar.id,
            "titulo": tar.tarefa.titulo,
            "descricao": tar.tarefa.descricao,
            "status": tar.tarefa.status,
            "usuario": tar.usuario_id,
            
        }
        for tar in tarefas
    ])



@api_v1_bp.route("/nova_tarefa", methods=["POST"])
def api_criar_tarefa():
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Envie JSON no body"}), 400
    try:
        tar = tarefa(
            usuario_id=int(dados["usuario_id"]),
            titulo=str(dados["titulo"]),
            descricao = str(dados["descricao"]),
            status = str(dados["status"]),
            data_inicio=datetime.strptime(dados["data_inicio"], "%Y-%m-%d").date(),
            data_fim=datetime.strptime(dados["data_fim"], "%Y-%m-%d").date(),
        )
    except (KeyError, ValueError):
        return jsonify({"erro": "Campos inválidos"}), 400
    db.session.add(tar)
    db.session.commit()
    return jsonify({"id": tar.id, "mensagem": "tarefa criada"}), 201



@api_v1_bp.route("/editar/<int:tarefa_id>", methods=["PUT"])
def api_editar_tarefa():
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Envie JSON no body"}), 400
        tar = tarefa.query.get_or_404(tarefa_id)
    
    try:
        if "titulo" in dados:
            tar.titulo = str(dados["titulo"])
        if "descricao" in dados:
            tar.descricao = str(dados["descricao"])
        if "status" in dados:
            tar.status = str(dados["status"])
            
    except (KeyError, ValueError):
        return jsonify({"erro": "Campos inválidos"}), 400

    db.session.commit()
    
    return jsonify({
        "id": tar.id, 
        "mensagem": "Tarefa atualizada com sucesso"
    }), 200

@api_v1_bp.route("/deletar/<int:tarefa_id>", methods=["DELETE"])
def api_deletar_tarefa(tarefa_id):
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Envie JSON no body"}), 400
        tar = tarefa.query.get_or_404(tarefa_id)
    
    try:
        db.session.delete(tar)
        db.session.commit()
    except Exception:
        db.session.rollback() 
        return jsonify({"erro": "Não foi possível deletar a tarefa"}), 500
        
    return jsonify({
        "id": tarefa_id,
        "mensagem": "Tarefa deletada com sucesso"
    }), 200