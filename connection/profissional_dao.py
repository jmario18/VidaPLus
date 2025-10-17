import mysql.connector
from connection import connection
from model.Profissional import Profissional


def registrarProfissional(profissional :Profissional):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO Profissional (nome, email, dataNasc, crm, telefone, cargo, cpf) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        valores = (profissional.nome, profissional.email, profissional.dataNasc, profissional.crm, profissional.telefone, profissional.cargo, profissional.cpf)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Profissional registrado com sucesso!")
    except mysql.connector.Error as erro:
        print(f"Erro ao registrar profissional: {erro}")
    finally:
        cursor.close()
        conexao.close()

def alterarProfissional(profissional :Profissional):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "UPDATE Profissional SET nome = %s, email = %s, dataNasc = %s, crm = %s, telefone = %s, cargo = %s WHERE profissionalId = %s"
        valores = (profissional.nome, profissional.email, profissional.dataNasc, profissional.crm, profissional.telefone, profissional.cargo, profissional.id)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Profissional alterado com sucesso!")
        return True
    except mysql.connector.Error as erro:
        print(f"Erro ao alterar profissional: {erro}")
        return False
    finally:
        cursor.close()
        conexao.close()

def buscarProfissionais(nome):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    if nome == "": nome = "%"  # Buscar todos os profissionais se o nome estiver vazio
    try:
        sql = "SELECT * FROM profissional WHERE nome LIKE %s"
        cursor.execute(sql, (f"%{nome}%",))
        resultados = cursor.fetchall()
        profissionais = []
        for resultado in resultados:
            profissional = {
                'id': resultado[0],
                'nome': resultado[1],
                'email': resultado[2] if len(resultado) > 2 else '',
                'dataNasc': resultado[3] if len(resultado) > 3 else '',
                'crm': resultado[4] if len(resultado) > 4 else '',
                'telefone': resultado[5] if len(resultado) > 5 else '',
                'cargo': resultado[6] if len(resultado) > 6 else ''
            }
            profissionais.append(profissional)
        return profissionais
    finally:
        cursor.close()
        conexao.close()

def buscarProfissionalCPF(cpf):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "SELECT profissionalId FROM profissional WHERE cpf LIKE %s"
        cursor.execute(sql, (f"%{cpf}%",))
        resultados = cursor.fetchall()
        idP = resultados[0]
        p = idP[0]
        return p
    finally:
        cursor.close()
        conexao.close()

def buscarProfissionalPorId(id):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "SELECT * FROM profissional WHERE profissionalId = %s"
        cursor.execute(sql, (id,))
        resultado = cursor.fetchone()
        if resultado:
            profissional = {
                'id': resultado[0],
                'nome': resultado[1],
                'cargo': resultado[6] if len(resultado) > 2 else '',
                'email': resultado[2] if len(resultado) > 3 else '',
                'telefone': resultado[5] if len(resultado) > 4 else '',
                'crm': resultado[4] if len(resultado) > 5 else '',
                'dataNasc':resultado[3] if len(resultado)> 6 else'',
                'cpf':resultado[7] if len(resultado) > 7 else''
            }
            return profissional
        return None
    finally:
        cursor.close()
        conexao.close()

def verificaDisponibilidade(profissionalId, data):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "SELECT * FROM consulta WHERE profissionalId = %s AND dataConsulta = %s"
        cursor.execute(sql, (profissionalId, data))
        resultados = cursor.fetchall()

        for resultado in resultados:

            if str(resultado[4]) == f'{data}:00':
                print("Profissional ocupado na data e hora informadas.")
                return False


        print("Profissional disponível na data e hora informadas.")
        return True
    except mysql.connector.Error as erro:
        print(f"Erro ao verificar disponibilidade: {erro}")
    finally:
        cursor.close()
        conexao.close()
