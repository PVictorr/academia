from flask import Flask, g, render_template,\
    request, redirect, url_for, flash, session

import mysql.connector

from models.usuario import Usuario
from models.usuarioDAO import UsuarioDAO

app = Flask(__name__)
app.secret_key = "senha123"

DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = ""
<<<<<<< HEAD
DB_NAME = "ACADEMIADB"
=======
DB_NAME = "academiadb"
>>>>>>> 5a16e447470ad47c8f06359fe824d0ab285c1fd1

app.auth = {
    # acao: { perfil:permissao }
    'painel': {0:1, 1:1},
    'logout': {0:1, 1:1},
    'cadastrar_exercicio': {0:1, 1:1},
    'listar_exercicio': {0:1, 1:1},
    'cadastrar_saida': {0:1, 1:1}
}

@app.before_request
def autorizacao():
    acao = request.path[1:]
    acao = acao.split('/')
    if len(acao)>=1:
        acao = acao[0]

    acoes = app.auth.keys()
    if acao in list(acoes):
        if session.get('logado') is None:
            return redirect(url_for('login'))

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME
        )
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == "POST":
        # valor = request.form['campoHTML']
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        objetivo = request.form['objetivo']

        usuario = Usuario(nome, email, senha, objetivo)

        dao = UsuarioDAO(get_db())
        codigo = dao.inserir(usuario)

        if codigo > 0:
            flash("Cadastrado com sucesso! Código %d" % codigo, "success")
        else:
            flash("Erro ao cadastrar!", "danger")

    vartitulo = "Cadastro"
    return render_template("cadastrar.html", titulo=vartitulo)


@app.route('/cadastrar_treino', methods=['GET', 'POST'])
def cadastrar_exercicios():
    if request.method == "POST":
        nome_excc = request.form['nome_excc']
        series = request.form['series']
        repeticoes = request.form['repeticoes']



<<<<<<< HEAD
        exercicios = Exercicios(nome_excc, series, repeticoes)
=======
        exercicios = Exercicios (nome_excc, series, repeticoes)
>>>>>>> 5a16e447470ad47c8f06359fe824d0ab285c1fd1


        dao = exercicioDAO(get_db())
        codigo = dao.inserir(exercicios)

        if codigo > 0:
            flash("Cadastrado com sucesso! Código %d" % codigo, "success")
        else:
            flash("Erro ao cadastrar!", "danger")

    vartitulo = "Cadastro de Exercicio"
    return render_template("exercicio-cadastrar.html", titulo=vartitulo)

@app.route('/listar_exercicio', methods=['GET',])
def listar_exercicio():
    dao = exercicioDAO(get_db())
    exercicios_db = dao.listar()
    return render_template("exercicio-listar.html", exercicios=exercicios_db)

@app.route('/cadastrar_saida', methods=['GET', 'POST'])
def cadastrar_saida():
    daoUsuario = UsuarioDAO(get_db())
    daoPlanta = PlantaDAO(get_db())

    if request.method == "POST":

        dtsaida = request.form['dtsaida']
        usuario = request.form['usuario']
        planta = request.form['planta']
        saida = Saida(usuario, planta, dtsaida)

        daoSaida = SaidaDAO(get_db())
        codigo = daoSaida.inserir(saida)
        if codigo > 0:
            flash("Saída cadastrada com sucesso! Código %d" % codigo, "success")
        else:
            flash("Erro ao registrar saída!", "danger")


    usuarios_db = daoUsuario.listar()
    plantas_db = daoPlanta.listar()
    return render_template("saida-cadastrar.html",
                           usuarios=usuarios_db, plantas=plantas_db)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        senha = request.form['senha']

        # Verificar dados
        dao = UsuarioDAO(get_db())
        usuario = dao.autenticar(email, senha)

        if usuario is not None:
            session['logado'] = {
                'codigo': usuario[0],
                'nome': usuario[3],
                'email': usuario[1],
            }
            return redirect(url_for('painel'))
        else:
            flash("Erro ao efetuar login!", "danger")

    return render_template("login.html", titulo="Login")


@app.route('/logout')
def logout():
    session['logado'] = None
    session.clear()
    return redirect(url_for('index'))


@app.route('/painel')
def painel():
    return render_template("index.html", titulo="Painel")


if __name__=='__main__':
    app.run(host="0.0.0.0", port=80, debug=True)