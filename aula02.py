"""
@author: Daniel
"""
from flask import Flask

app_Daniel = Flask (__name__)


@app_Daniel.route('/')
@app_Daniel.route('/ola')

def raiz():
    return 'ola, tuma!'

def saudacoes (nome):
    return f'Olá, {nome}'

if __name__ == "__main__":
    app_Daniel.run(port = 8080, debug= True)
