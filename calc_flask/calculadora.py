import requests
from flask import Flask, render_template, request


def calcular():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operacao = request.form['operacao']

    if operacao == "+":
        resultado = f'{num1} + {num2}'
    elif operacao == "-":
        resultado = f'{num1} + {num2}'
    elif operacao == "*":
        resultado = f'{num1} + {num2}'
    elif operacao == "/":
        resultado = f'{num1} + {num2}'
        if num2 == 0:
            "divisor inválido"
    return render_template('index.html', etapas = etapas, resultado = resultado)