from flask import Flask, g, render_template,\
    request, redirect, url_for, flash, session


import hashlib
import os
import mysql.connector
import google.oauth2.credentials
import google_auth_oauthlib.flow
from google.auth.transport import requests
import requests, json

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


from models.usuario import Usuario
from models.usuarioDAO import UsuarioDAO
from models.exercicio import exercicio
from models.exercicioDAO import ExercicioDAO
from models.avaliacao import Avaliacao
from models.avaliacaoDAO import AvaliacaoDAO

app = Flask(__name__)
app.secret_key = "senha123"

DB_HOST = "localhost"
DB_USER = "root"
DB_NAME = "academiadb"
DB_PASS = ""

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
        else:
            tipo = session['logado']
            if app.auth[acao] == 0:
                return redirect(url_for('painel'))

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
    return render_template("login.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == "POST":
        # valor = request.form['campoHTML']
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        email = request.form['email']
        senha = request.form['senha']

        usuario = Usuario(nome, sobrenome, email, senha)

        dao = UsuarioDAO(get_db())
        codigo = dao.inserir(usuario)

        if codigo > 0:
            msg = ("Cadastrado com sucesso!")
        else:
            msg = ("Erro ao cadastrar!")

    vartitulo = "Cadastro"
    return render_template("register.html", titulo=vartitulo, msg=msg)


@app.route('/cadastrar_treino', methods=['GET', 'POST'])
def cadastrar_exercicios():
    if request.method == "POST":
        carga = request.form['carga']
        series = request.form['series']
        repeticoes = request.form['repeticoes']

        exercicios = exercicio(carga, series, repeticoes)

        dao = ExercicioDAO(get_db())
        codigo = dao.inserir(exercicios)

        if codigo > 0:
            flash("Cadastrado com sucesso! Código %d" % codigo, "success")
        else:
            flash("Erro ao cadastrar!", "danger")

    vartitulo = "Cadastro de Exercicio"
    return render_template("exercicio-cadastrar.html", titulo=vartitulo)

@app.route('/avaliacao', methods=['GET', 'POST'])
def avaliacao():
    if request.method == "POST":
        peso = request.form['peso']
        altura = request.form['altura']
        braco = request.form['braco']
        ombro = request.form['ombro']
        peito = request.form['peito']
        cintura = request.form['cintura']
        quadril = request.form['quadril']
        abdominal = request.form['abdominal']
        coxaMedial = request.form['coxaMedial']
        panturrilha = request.form['panturrilha']

        avaliacao = Avaliacao(peso, altura, braco, ombro, peito, cintura, quadril,
                              abdominal, coxaMedial, panturrilha,session['logado']['codigo'] )

        dao = AvaliacaoDAO(get_db())
        codigo = dao.inserir(avaliacao)

        if codigo > 0:
            flash("Cadastrado com sucesso! Código %d" % codigo, "success")
        else:
            flash("Erro ao cadastrar!", "danger")

    vartitulo = "Avaliacao"
    return render_template("avaliacao.html", titulo=vartitulo)

@app.route('/listar_exercicio', methods=['GET',])
def listar_exercicio():
    dao = ExercicioDAO(get_db())
    exercicios_db = dao.listar()
    return render_template("exercicio-listar.html", exercicios=exercicios_db)

@app.route('/listaraval', methods=['GET', 'POST'])
def listaraval():
    dao = AvaliacaoDAO(get_db())
    avaliacao_db = dao.listar()
    return render_template("listaraval.html", avaliacao=avaliacao_db)

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
        email = request.form["email"]
        senha = request.form["senha"]

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
            flash("Erro ao efetuar login!")

    return render_template("login.html", titulo="Login")


@app.route('/logout')
def logout():
    session['logado'] = None
    session.clear()
    return redirect(url_for('index'))

@app.route('/forgot')
def forgot():
    return render_template("forgot-password.html", titulo ="Esqueci minha senha")

@app.route('/painel')
def painel():
    return render_template("index.html", titulo="index")

@app.route('/peito', methods=['GET', 'POST'])
def peito():
    dao = ExercicioDAO(get_db())
    exercicio_db = dao.listar_peito()
    exercicio = list(exercicio_db)
    print(exercicio)

    video_url = [0, "https://www.youtube.com/embed/R08gYyypGto?si=ugbVi8tG0J354KOq"]
    return render_template("peito.html", titulo="peito", exercicio=exercicio, video_url = video_url)

@app.route('/perna', methods=['GET', 'POST'])
def perna():
    dao = ExercicioDAO(get_db())
    exercicio_db = dao.listar_perna()
    return render_template("perna.html", titulo="perna", exercicio=exercicio_db)

@app.route('/braco', methods=['GET', 'POST'])
def braco():
    dao = ExercicioDAO(get_db())
    exercicio_db = dao.listar_braco()
    return render_template("braco.html", titulo="braco", exercicio=exercicio_db)

@app.route('/costas', methods=['GET', 'POST'])
def costas():
    dao = ExercicioDAO(get_db())
    exercicio_db = dao.listar_costas()
    return render_template("costas.html", titulo="costas", exercicio=exercicio_db)

@app.route('/abdomen', methods=['GET', 'POST'])
def abdomen():
    dao = ExercicioDAO(get_db())
    exercicio_db = dao.listar_abdomen()
    return render_template("abdomen.html", titulo="abdomen", exercicio=exercicio_db)

@app.route('/alongamento', methods=['GET', 'POST'])
def alongamento():
    dao = ExercicioDAO(get_db())
    exercicio_db = dao.listar_alongamento()
    return render_template("alongamento.html", titulo="alongamento", exercicio=exercicio_db)



@app.route('/mainaval')
def mainaval():
    return render_template("mainaval.html", titulo="mainaval")

@app.route("/login_google")
def login_google():

    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        'client_secret.json',
        scopes=['https://www.googleapis.com/auth/userinfo.email',
                'https://www.googleapis.com/auth/userinfo.profile', 'openid'])

    flow.redirect_uri = 'http://localhost/callback'

    authorization_url, state = flow.authorization_url(
        acess_type='offline',
        include_granted_scopes='true')

    return redirect(authorization_url)

@app.route('/callback')
def callback():

    state = request.args.get('state')
    code = request.args.get('code')

    if code is None or code == '':
        flash('Erro ao logar com conta google', 'danger')
        return redirect(url_for('login'))

    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        'client_secret.json',
        scopes=['https://www.googleapis.com/auth/userinfo.email',
                'https://www.googleapis.com/auth/userinfo.profile', 'openid'],
        state=state)

    flow.redirect_uri = url_for('callback', _external=True)

    authorization_response = request.url
    flow.fetch_token(authorization_response=authorization_response)

    credentials = flow.credentials

    resposta_api = requests.get("https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token=" +
                                credentials.token)
    user_info = resposta_api.json()

    email = str(user_info['email'])
    dao = UsuarioDAO(get_db())
    user = dao.obter(email)
    print((user_info["email"]))

    if user is None:
        hash = hashlib.sha512()
        senha = os.urandom(50)
        secret = app.config['SECRET_KEY']
        hash.update(f'{secret}{senha}'.encode('utf-8'))
        senha_criptografa = hash.hexdigest()

        usuario = Usuario(
            user_info['name'],
            user_info['email'],
            senha_criptografa,
            '',
        )

        id = None
        if usuario.senha and usuario.nome and usuario.email:
            id = UsuarioDAO.inserir(usuario)
            print(id)

        if id is None or id <=0:
            flash('Erro ao cadastrar usuário', 'danger')
            return redirect(url_for('login'))
        else:
            user = UsuarioDAO.obter(user_info['email'])

            session['logado'] = user
            flash(f'Seja bem-vindo, {user[1]}!', 'primary')

            revoke = requests.post(
                'https://gauth2.googleapis.com/revoke',
                params={'token': credentials.token},
                headers={'content-type': 'application/x-www-form-urlencoded'})

            return redirect(url_for('painel'))



if __name__=='__main__':
    app.run(host="0.0.0.0", port=80, debug=True)