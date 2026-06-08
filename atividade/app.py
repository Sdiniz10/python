import os

from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

pasta_aula = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    pasta_aula, "produtos.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)



class Produto(db.Model):
    __tablename__ = "produtos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    categoria = db.Column(db.String(60), nullable=False)
    preco = db.column(db.Float(), nullable = False)
    estoque = db.column(db.Integer, nullable = False)

    def __repr__(self):
        return f"<produtos {self.id} {self.nome}>"


with app.app_context():
    db.create_all()



@app.route("/")
def index():
    produtos = produto.query.order_by(produto.nome).all()
    return render_template("lista.html", produtos = produtos)


@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        categoria = request.form.get("categoria", "").strip()
        preco = request.form.get ('preco', "").strip()
        estoque = request.form.get ("estoque", "").strip()

        
        if not nome or not categoria:
            return render_template(
                "formulario.html",
                titulo="Cadastrar produto",
                erro="Preencha nome e categoria.",
                nome=nome,
                categoria=categoria,
                preco = preco,
                estoque = estoque
            )
        produto = Produto(nome=nome, categoria=categoria)
        db.session.add(produto)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("formulario.html", titulo="Cadastrar produto")



@app.route("/editar/<int:produto_id>", methods=["GET", "POST"])
def editar(produto_id):
    produto = db.session.get(Produto, produto_id)
    if not produto:
        return redirect(url_for("index"))

    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        categoria = request.form.get("categoria", "").strip()
        if not nome or not categoria:
            return render_template(
                "formulario.html",
                titulo="Editar produto",
                erro="Preencha nome e categoria.",
                nome=nome,
                categoria=categoria,
                preco = preco,
                estoque = estoque,
                produto_id=produto.id,
                
            )
        produto.nome = nome
        produto.categoria = categoria
        db.session.commit()
        return redirect(url_for("index"))

    return render_template(
        "formulario.html",
        titulo="Editar produto",
        nome=produto.nome,
        categoria=produto.categoria,
        preco = preco,
        estoque = estoque,
        produto_id=produto.id,
    )


@app.route("/excluir/<int:produto_id>", methods=["POST"])
def excluir(produto_id):
    produto = db.session.get(Produto, produto_id)
    if produto:
        db.session.delete(produto)
        db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)