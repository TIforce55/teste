from flask import Flask, render_template

app_Daniel = Flask(__name__ , template_folder='template')

@app_Daniel.route("/index")
def indice():
    return render_template ("index.html")

@app_Daniel.route("/")
def homepage():
    return render_template ("homepage.html")

@app_Daniel.route("/contato")
def contato():
    return render_template("contato.html")

@app_Daniel.route("/usuario")
def dados_usuario():
    nome_usuario="Daniel"
    return render_template("usuario.html", nome = nome_usuario )


if __name__ == "__main__":
    app_Daniel.run(port = 8000)
