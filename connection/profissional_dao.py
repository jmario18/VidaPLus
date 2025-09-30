import mysql.connector
from connection import connection
from model.Profissional import Profissional


def registrarProfissional(profissional :Profissional):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO Profissional (nome, email, dataNasc, crm, telefone, cargo) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (profissional.nome, profissional.email, profissional.dataNasc, profissional.crm, profissional.telefone, profissional.cargo)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Profissional registrado com sucesso!")
    except mysql.connector.Error as erro:
        print(f"Erro ao registrar profissional: {erro}")
    finally:
        cursor.close()
        conexao.close()

def consultaProfissional(nome):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "SELECT * FROM profissional WHERE nome = %s"
        cursor.execute(sql, (nome,))
        resultado = cursor.fetchone()
        if resultado:
            print("Profissional encontrado:")
            print(f"Nome: {resultado[1]}")
            print(f"Cargo: {resultado[2]}")
            print(f"Email: {resultado[3]}")
            print(f"Telefone: {resultado[4]}")
        else:
            print("Profissional não encontrado.")
    except mysql.connector.Error as erro:
        print(f"Erro ao consultar profissional: {erro}")
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

def buscarProfissionalPorId(id):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "SELECT * FROM profissional WHERE id = %s"
        cursor.execute(sql, (id,))
        resultado = cursor.fetchone()
        if resultado:
            profissional = {
                'id': resultado[0],
                'nome': resultado[1],
                'cargo': resultado[2] if len(resultado) > 2 else '',
                'email': resultado[3] if len(resultado) > 3 else '',
                'telefone': resultado[4] if len(resultado) > 4 else '',
                'crm': resultado[5] if len(resultado) > 5 else ''
            }
            return profissional
        return None
    finally:
        cursor.close()
        conexao.close()