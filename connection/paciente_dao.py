import mysql.connector
from connection import connection
from model.Paciente import Paciente

def registrarPaciente(paciente :Paciente):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO Paciente (nome, dataNasc, cpf, endereco, telefone, email) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (paciente.nome, paciente.dataNasc, paciente.cpf, paciente.endereco, paciente.telefone, paciente.email)
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

def alterarPaciente(paciente :Paciente):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "UPDATE Paciente SET nome = %s, dataNasc = %s, cpf = %s, endereco = %s, telefone = %s, email = %s WHERE pacienteId = %s"
        valores = (paciente.nome, paciente.dataNasc, paciente.cpf, paciente.endereco, paciente.telefone, paciente.email, paciente.id)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Paciente alterado com sucesso!")
        return True
    except mysql.connector.Error as erro:
        print(f"Erro ao alterar paciente: {erro}")
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

def buscarPacienteCPF(cpf):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "SELECT pacienteId FROM paciente WHERE cpf LIKE %s"
        cursor.execute(sql, (f"%{cpf}%",))
        resultados = cursor.fetchall()
        tup = resultados[0]
        idP = tup[0]
        return idP
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
            paciente = Paciente(id=resultado[0], nome=resultado[1], dataNasc=resultado[2], cpf=resultado[3], endereco=resultado[4], telefone=resultado[5], email=resultado[6])
            return paciente
        return None
    finally:
        cursor.close()
        conexao.close()