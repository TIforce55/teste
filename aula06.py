

@app_Daniel.route('/<id>')
def saudacao(id):
    return render_template('homepage_nome.html', nome=id)

@app_Daniel.route("/usuario/<nome_usuario>;<nome_profissao>")

def usuario (nome_usuario, nome_profissao):

    return render_template ("usuario.html", nome=nome_usuario)

