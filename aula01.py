from flask import Flask

app_Daniel = Flask (__name__)

@app_Daniel.route('/')
def raiz():
    return 'Olá, turma!'

app_Daniel.run()
