from flask import Blueprint, redirect, render_template, request, url_for

from models import Colecionador, Figurinha, ItemOferta, OfertaTroca, db

# Apelido "figurinhas" → use url_for('figurinhas.index') nos templates
figurinhas_bp = Blueprint("figurinhas", __name__, url_prefix="/figurinhas")


@figurinhas_bp.route("/")
def index():
    # TODO ALUNO: ofertas = OfertaTroca.listar_com_colecionador()
    return render_template("figurinhas/lista_ofertas.html", ofertas=[])


@figurinhas_bp.route("/oferta/cadastrar", methods=["GET", "POST"])
def cadastrar_oferta():
    colecionadores = Colecionador.listar()
    figurinhas = Figurinha.listar()

    if request.method == "POST":
        # TODO ALUNO: criar OfertaTroca + ItemOferta (oferece/deseja)
        pass

    return render_template(
        "figurinhas/formulario_oferta.html",
        colecionadores=colecionadores,
        figurinhas=figurinhas,
    )









@app.route("/")
def index():
    figurinhas = figurinha.query.order_by(figurinha.apelido).all()
    return render_template("lista.html", figurinhas = figurinhas)


@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        apelido = request.form.get("apelido", "").strip()
        cidade = request.form.get("cidade", "").strip()
        observacao = request.form.get ('observacao', "").strip()
        data = request.form.get ("data", "").strip()

        
        if not apelido or not cidade:
            return render_template(
                "formulario.html",
                titulo="Cadastrar figurinha",
                erro="Preencha apelido e cidade.",
                apelido=apelido,
                cidade=cidade,
                observacao = observacao,
                data = data
            )
        figurinha = figurinha(apelido=apelido, cidade=cidade)
        db.session.add(figurinha)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("formulario.html", titulo="Cadastrar figurinha")



@app.route("/editar/<int:figurinha_id>", methods=["GET", "POST"])
def editar(figurinha_id):
    figurinha = db.session.get(figurinha, figurinha_id)
    if not figurinha:
        return redirect(url_for("index"))

    if request.method == "POST":
        apelido = request.form.get("apelido", "").strip()
        cidade = request.form.get("cidade", "").strip()
        if not apelido or not cidade:
            return render_template(
                "formulario.html",
                titulo="Editar figurinha",
                erro="Preencha apelido e cidade.",
                apelido=apelido,
                cidade=cidade,
                observacao = observacao,
                data = data,
                figurinha_id=figurinha.id,
                
            )
        figurinha.apelido = apelido
        figurinha.cidade = cidade
        db.session.commit()
        return redirect(url_for("index"))

    return render_template(
        "formulario.html",
        titulo="Editar figurinha",
        apelido=figurinha.apelido,
        cidade=figurinha.cidade,
        observacao = observacao,
        data = data,
        figurinha_id=figurinha.id,
    )


@app.route("/excluir/<int:figurinha_id>", methods=["POST"])
def excluir(figurinha_id):
    figurinha = db.session.get(figurinha, figurinha_id)
    if figurinha:
        db.session.delete(figurinha)
        db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)