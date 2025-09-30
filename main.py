from model.Paciente import *
from model.Profissional import Profissional
#from model.Usuario import Usuario
from connection.connection import *
from connection.paciente_dao import *
from connection.profissional_dao import *
from flask import request, render_template, Flask, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'chave_secreta_super_segura_vidaplus'

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        login = request.form.get("login")
        senha = request.form.get("senha")
        conexao = criar_conexao()
        cursor = conexao.cursor()
        try:
            sql = "SELECT * FROM usuario WHERE nomeUsuario = %s AND senha = %s"
            cursor.execute(sql, (login, senha))
            usuario = cursor.fetchone()
            if usuario:
                session['usuario'] = usuario[1]  # salva o nome do usuário
                print(usuario[1], usuario[2], usuario[3], usuario[4])
                if usuario[3] == 1:
                    session['isAdmin'] = True
                return redirect(url_for('index'))
            else:
                return render_template('login.html', erro="Usuário ou senha incorretos.")
        finally:
            cursor.close()
            conexao.close()
    return render_template('login.html')


@app.route("/index", methods=["GET"])
def index():
    usuario = session.get('usuario')
    return render_template('index.html', usuario=usuario)

@app.route("/cadastrar_paciente", methods=["GET", "POST"])
def cadastrarPacienteRoute():
    usuario = session.get('usuario')
    if request.method == "POST":
        cadastrarPaciente()
    return render_template('cadastro.html', tipo='paciente', usuario=usuario)


@app.route("/cadastrar_profissional", methods=["GET","POST"])
def cadastrarProfissionalRoute():
    usuario = session.get('usuario')
    if request.method == "POST":
        cadastrarProfissional()
    return render_template('cadastro.html', tipo='profissional', usuario=usuario)

@app.route("/marcar_consulta", methods=["GET","POST"])
def marcarConsultaRoute():
    usuario = session.get('usuario')
    pacientes = buscarPacientes("")
    profissionais = buscarProfissionais("")
    if request.method == "POST":
        if cadastrarConsulta():
            print("Sucesso")
            return render_template('marcarConsulta.html', sucesso="Consulta marcada com sucesso!", pacientes=pacientes, profissionais=profissionais, usuario=usuario)
        else:
            print("Erro")
            return render_template('marcarConsulta.html', erro="Horário indisponível para o profissional selecionado.", pacientes=pacientes, profissionais=profissionais, usuario=usuario)
    return render_template('marcarConsulta.html', pacientes=pacientes, profissionais=profissionais, usuario=usuario)

@app.route("/buscar_paciente", methods=["GET","POST"])
def buscarPacienteRoute():
    usuario = session.get('usuario')
    if request.method == "POST":
        nome = request.form.get("nome")
        paciente = buscarPacientes(nome)
        print(paciente)
        if len(paciente) == 0:
            return render_template('buscas.html', tipo='paciente', erro="Paciente não encontrado.", usuario=usuario)
        return render_template('buscaResultado.html', tipo='paciente', pacientes=paciente, usuario=usuario)
    return render_template('buscas.html', tipo='paciente', usuario=usuario)

@app.route("/selecionar_paciente/<int:id>", methods=["GET"])
def selecionarPacienteRoute(id):
    usuario = session.get('usuario')
    paciente = buscarPacientePorId(id)
    return render_template('resultado.html', tipo='paciente', paciente=paciente, usuario=usuario)

@app.route("/buscar_profissional", methods=["GET","POST"])
def buscarProfissionalRoute():
    usuario = session.get('usuario')
    if request.method == "POST":
        nome = request.form.get("nome")
        profissional = buscarProfissionais(nome)
        print(profissional)
        if len(profissional) == 0:
            return render_template('buscas.html', tipo='profissional', erro="Profissional não encontrado.", usuario=usuario)
        return render_template('buscaResultado.html', tipo='profissional', profissionais=profissional, usuario=usuario)
    return render_template('buscas.html', tipo='profissional', usuario=usuario)

@app.route("/selecionar_profissional/<int:id>", methods=["GET"])
def selecionarProfissionalRoute(id):
    usuario = session.get('usuario')
    profissional = buscarProfissionalPorId(id)
    return render_template('resultado.html', tipo='profissional', profissional=profissional, usuario=usuario)


def cadastrarPaciente():
    #pega os dados do paciente do formulário na route  
    nome = request.form.get("nome")
    dataNasc = request.form.get("data_nascimento")
    endereco = request.form.get("endereco")
    telefone = request.form.get("telefone")
    cpf = request.form.get("cpf")
    #cria o objeto paciente
    paciente = Paciente(nome=nome, dataNasc=dataNasc, endereco=endereco, cpf=cpf, telefone=telefone)
    #cadastra o paciente no banco de dados
    try:
        registrarPaciente(paciente)
        print(f"Paciente {nome} cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar paciente: {e}")

def cadastrarProfissional():
    nome = request.form.get("nome")
    email = request.form.get("email")
    telefone = request.form.get("telefone")
    cargo = request.form.get("cargo")
    crm = request.form.get("crm")
    telefone = request.form.get("telefone")
    dataNasc = request.form.get("data_nascimento")
    #cria o objeto profissional
    profissional = Profissional(nome=nome, email=email, dataNasc=dataNasc, crm=crm,  telefone=telefone, cargo=cargo )
    try:
        registrarProfissional(profissional)
        print(f"Profissional {profissional.nome} cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar profissional: {e}")

def cadastrarConsulta():
    paciente = request.form.get("paciente")
    profissional = request.form.get("profissional")
    data = request.form.get("data")
    hora = request.form.get("hora")
    motivo = request.form.get("motivo")
    observacoes = request.form.get("observacoes")
    if verificaDisponibilidade(profissional, f'{data} {hora}'):
        try:
            registrarConsulta(paciente, profissional, data, hora, motivo, observacoes)
        except Exception as e:
            print(f"Erro ao marcar consulta: {e}")
        return True
    else:
        print("Horário indisponível para o profissional selecionado.")
        return False

def cadastrarLocal():
    nome = request.form.get("nome")
    endereco = request.form.get("endereco")
    tipo = request.form.get("tipo")
    try:
        registrarLocal(nome, endereco, tipo)
        print(f"Unidade {nome} cadastrada com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar unidade: {e}")

def cadastrarReceita():
    pass

def cadastrarProntuario():
    
    # TODO Disponível para profissionais.
    # TODO Cadastrar prontuário para paciente que seja a primeira consulta
    # TODO Pegar informações da consulta
    # TODO Cadastrar prontuário no banco de dados
    # TODO Poder realizar anotações para cada consulta
    pass


def verificarProntuario(nome):
    #consultaProntuario(nome)
    pass
