import mysql.connector
from connection import connection

class Paciente:
    def __init__(self, nome, dataNasc, endereco, cpf, telefone):
        self.id = None
        self.nome = nome
        self.dataNasc = dataNasc
        self.endereco = endereco
        self.telefone = telefone
        self.cpf = cpf

    def __str__(self):
        return f"Paciente: {self.nome}"
    

    #funcoes ligadas ao paciente
    def registrarPaciente(nome, dataNasc, cpf, endereco, telefone):
        conexao = connection.criar_conexao()
        cursor = conexao.cursor()
        try:
            sql = "INSERT INTO Paciente (nome, dataNasc, cpf, endereco, telefone) VALUES (%s, %s, %s, %s, %s)"
            valores = (nome, dataNasc, cpf, endereco, telefone)
            cursor.execute(sql, valores)
            conexao.commit()
            print("Paciente registrado com sucesso!")
        except mysql.connector.Error as erro:
            print(f"Erro ao registrar paciente: {erro}")
        finally:
            cursor.close()
            conexao.close()

