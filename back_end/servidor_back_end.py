from config import *
from modelo import Livro

@app.route("/")
def inicio():
    return 'Sistema para cadastrar livros. '+\
        '<a href="/listar_livros">Listar Livros</a>'

@app.route("/listar_livros")
def listar_livros():
    livros = db.session.query(Livro).all()
    livro_em_json = [ x.json() for x in livros ]
    resposta = jsonify(livro_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

app.run(debug=True)