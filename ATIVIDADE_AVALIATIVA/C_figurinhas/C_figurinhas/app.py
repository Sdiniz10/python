import os
from flask import Flask, redirect, url_for
from models import db
from controllers.figurinhas_controller import figurinhas_bp

def criar_app():
    app = Flask(
        __name__,
        template_folder="views/templates",
        static_folder="views/static",
    )

    pasta = os.path.abspath(os.path.dirname(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(pasta, "figurinhas.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.register_blueprint(figurinhas_bp)

    @app.route("/")
    def index():
        return redirect(url_for("figurinhas.index"))

    with app.app_context():
        db.create_all()
    

    return app


app = criar_app()

if __name__ == "__main__":
    app.run(debug=True)