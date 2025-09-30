import mysql.connector
from connection import connection
from model.Paciente import Paciente

def registrarPaciente(paciente :Paciente):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO Paciente (nome, dataNasc, cpf, endereco, telefone) VALUES (%s, %s, %s, %s, %s)"
        valores = (paciente.nome, paciente.dataNasc, paciente.cpf, paciente.endereco, paciente.telefone)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Paciente registrado com sucesso!")
        return True
    except mysql.connector.Error as erro:
        print(f"Erro ao registrar paciente: {erro}")
        return False
    finally:
        cursor.close()
        conexao.close()

def buscarPacientes(nome):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    if nome == "": nome = "%"  # Buscar todos os pacientes se o nome estiver vazio
    try:
        sql = "SELECT * FROM paciente WHERE nome LIKE %s"
        cursor.execute(sql, (f"%{nome}%",))
        resultados = cursor.fetchall()
        pacientes = []
        for resultado in resultados:
            paciente = {
                'id': resultado[0],
                'nome': resultado[1],
                'dataNasc': resultado[2] if len(resultado) > 2 else '',
                'cpf': resultado[3] if len(resultado) > 3 else '',
                'endereco': resultado[4] if len(resultado) > 4 else '',
                'telefone': resultado[5] if len(resultado) > 5 else ''
            }
            pacientes.append(paciente)
        return pacientes
    finally:
        cursor.close()
        conexao.close()


def buscarPacientePorId(id):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "SELECT * FROM paciente WHERE pacienteId = %s"
        cursor.execute(sql, (id,))
        resultado = cursor.fetchone()
        if resultado:
            paciente = {
                'id': resultado[0],
                'nome': resultado[1],
                'dataNasc': resultado[2] if len(resultado) > 2 else '',
                'cpf': resultado[3] if len(resultado) > 3 else '',
                'endereco': resultado[4] if len(resultado) > 4 else '',
                'telefone': resultado[5] if len(resultado) > 5 else ''
            }
            return paciente
        return None
    finally:
        cursor.close()
        conexao.close()