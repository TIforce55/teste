from flask import Flask

app_Daniel = Flask (__name__)


@app_Daniel.route('/')
@app_Daniel.route('/rota1')
def rota1():
    return 'Ola, turma!'

@app_Daniel.route('/rota2')
def rota2():
    resposta = "<H3> Essa é outra página da rota 2 <H3>"
    return resposta

def saudacoes (nome):
    return f'Olá, {nome}'

if __name__ == "__main__" :
    app_Daniel.run()