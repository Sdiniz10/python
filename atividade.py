from flask import Flask

app = Flask(__name__) # inicio o flask
teste = 2 + 2
@app.route('/') # Isso é o decorator, ele é usado para mapear a função abaixo para a rota '/'
def decorator():
    return 'O Decorator é usado para mapear a função abaixo para a rota barra\
         mas caso você especifique o nome, ele poderá mapear uma rota mais rápida ' + str(soma(2,4)) # Isso é o que será retornado quando a rota '/' for acessada

@app.route('/soma') # Isso é o decorator, ele é usado para mapear a função abaixo para a rota '/'
def soma(a, b):
    return a + b
if __name__ == '__main__':
    app.run(debug=True) # Isso inicia o servidor Flask em modo de depuração, o que é útil para desenvolvimento

