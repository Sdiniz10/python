from flask import Blueprint, redirect, render_template, request, url_for

from models import Colecionador, Figurinha, ItemOferta, OfertaTroca, db

figurinhas_bp = Blueprint("figurinhas", __name__, url_prefix="/figurinhas")


@figurinhas_bp.route("/")
def index():
    ofertas = OfertaTroca.listar_com_colecionador()
    return render_template("figurinhas/lista_ofertas.html", ofertas=ofertas)


@figurinhas_bp.route("/oferta/cadastrar", methods=["GET", "POST"])
def cadastrar_oferta():
    colecionadores = Colecionador.listar()
    figurinhas = Figurinha.listar()

    if request.method == "POST":
        oferta = OfertaTroca(
            colecionador_id=int(request.form["colecionador_id"]),
            observacao=request.form.get("observacao", ""),
        )
        db.session.add(oferta)
        db.session.flush()  # gera o id da oferta antes de criar os itens

        db.session.add(ItemOferta(
            oferta_id=oferta.id,
            figurinha_id=int(request.form["figurinha_oferece_id"]),
            tipo="oferece",
        ))
        db.session.add(ItemOferta(
            oferta_id=oferta.id,
            figurinha_id=int(request.form["figurinha_deseja_id"]),
            tipo="deseja",
        ))
        db.session.commit()
        return redirect(url_for("figurinhas.index"))

    return render_template("figurinhas/formulario_oferta.html",
                           colecionadores=colecionadores, figurinhas=figurinhas)


@figurinhas_bp.route("/colecionadores")
def listar_colecionadores():
    colecionadores = Colecionador.listar()
    return render_template("figurinhas/colecionadores.html", colecionadores=colecionadores)


@figurinhas_bp.route("/colecionadores/cadastrar", methods=["GET", "POST"])
def cadastrar_colecionador():
    if request.method == "POST":
        c = Colecionador(
            apelido=request.form["apelido"],
            cidade=request.form["cidade"],
        )
        db.session.add(c)
        db.session.commit()
        return redirect(url_for("figurinhas.listar_colecionadores"))
    return render_template("figurinhas/formulario_colecionador.html")


@figurinhas_bp.route("/figurinhas")
def listar_figurinhas():
    figurinhas = Figurinha.listar()
    return render_template("figurinhas/figurinhas.html", figurinhas=figurinhas)


@figurinhas_bp.route("/figurinhas/cadastrar", methods=["GET", "POST"])
def cadastrar_figurinha():
    if request.method == "POST":
        f = Figurinha(
            numero=int(request.form["numero"]),
            nome_jogador=request.form["nome_jogador"],
            time=request.form["time"],
        )
        db.session.add(f)
        db.session.commit()
        return redirect(url_for("figurinhas.listar_figurinhas"))
    return render_template("figurinhas/formulario_figurinha.html")