from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    nome = "Samuel"
    idade = 17
    email = "dinizsamuel400@gmail.com"
    return render_template('index.html', nome = nome, idade = idade)

if __name__ == "__main__":
    app.run(debug = True)
