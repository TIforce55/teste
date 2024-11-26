from flask import Flask

app_Daniel = Flask (__name__)

@app_Daniel.route('/<id>')
def saudacao():
    return render_template('homepage_nome.html', nome=id)
