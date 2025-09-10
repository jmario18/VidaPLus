from model.Paciente import Paciente
from model.Profissional import Profissional
from connection.connection import *

def cadastrarPaciente():
    #pega os dados do paciente
    nome = input("Digite o nome do paciente: ")
    idade = input("Digite a idade do paciente: ")
    endereco = input("Digite o endereço do paciente: ")
    telefone = input("Digite o telefone do paciente: ")
    #cria o objeto paciente
    paciente = Paciente(nome, idade, endereco, telefone)
    #cadastra o paciente no banco de dados
    try:
        registrarPaciente(paciente.nome, paciente.idade, paciente.endereco, paciente.telefone)
        print(f"Paciente {paciente.nome} cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar paciente: {e}")

def cadastrarProfissional():
    nome = input("Digite o nome do Profissional")
    email = input("Digite o email do Profissional")
    telefone = input("Digite o telefone do Profissional")
    cargo = input("Digite o cargo do Profissional")
    crm = input("Digite o CRM do Profissional")
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
    nome = input("Digite o nome da unidade: ")
    endereco = input("Digite o endereço da unidade: ")
    tipo = input("Digite o tipo da unidade: ")
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
    nome = input("Digite o nome do paciente: ")
    consultaPaciente(nome)

def verificarProfissional():
    nome = input("Digite o nome do profissional: ")
    consultaProfissional(nome)


def verificarProntuario():
    nome = input("Digite o nome do paciente: ")
#    consultaProntuario(nome)
