from model.Paciente import Paciente
from model.Profissional import Profissional
from connection.connection import *
from flask import request, render_template, Flask

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/cadastrar_paciente", methods=["GET", "POST"])
def cadastrarPacienteRoute():
    if request.method == "POST":
        cadastrarPaciente()
    return render_template('cadastro.html', tipo='paciente')


@app.route("/cadastrar_profissional", methods=["GET","POST"])
def cadastrarProfissionalRoute():
    if request.method == "POST":
        cadastrarProfissional()
    return render_template('cadastro.html', tipo='profissional')


def cadastrarPaciente():
    #pega os dados do paciente do formulário na route  
    nome = request.form.get("nome")
    dataNasc = request.form.get("data_nascimento")
    endereco = request.form.get("endereco")
    telefone = request.form.get("telefone")
    #cria o objeto paciente
    paciente = Paciente(nome, dataNasc, endereco, telefone)
    print(f"Paciente: {paciente.nome}, Data de Nascimento: {paciente.dataNasc}, Endereço: {paciente.endereco}, Telefone: {paciente.telefone}")
    #cadastra o paciente no banco de dados
   # try:
   #     registrarPaciente(paciente.nome, paciente.dataNasc, paciente.endereco, paciente.telefone)
   #     print(f"Paciente {paciente.nome} cadastrado com sucesso!")
   # except Exception as e:
   #     print(f"Erro ao cadastrar paciente: {e}")

def cadastrarProfissional():
    nome = request.form.get("nome")
    email = request.form.get("email")
    telefone = request.form.get("telefone")
    cargo = request.form.get("cargo")
    crm = request.form.get("crm")
    profissional = Profissional(nome, email, telefone, cargo, crm)
    try:
        registrarProfissional(profissional.nome, profissional.email, profissional.telefone, profissional.cargo, profissional.crm)
        print(f"Profissional {profissional.nome} cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar profissional: {e}")

def cadastrarConsulta():
    # TODO Pegar lista de pacientes (podendo pesquisar)
    # TODO Filtrar profissionais da área selecionada para atender
    # TODO Pegar lista de profissionais que poderão atender
    # TODO Inserir o motivo da consulta
    # TODO Pegar data e hora da consulta que estejam disponiveis para o profissional

    pass

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

def verificarPaciente():
    nome = request.form.get("nome")
    consultaPaciente(nome)

def verificarProfissional():
    nome = request.form.get("nome")
    consultaProfissional(nome)


def verificarProntuario():
    nome = request.form.get("nome")
#    consultaProntuario(nome)
