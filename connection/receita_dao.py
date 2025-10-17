from connection import connection
import mysql.connector
from model.Receita import Receita

def registrarReceita(receita :Receita):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO Receita (id, descricao, data_emissao, id_paciente) VALUES (%s, %s, %s, %s)"
        valores = (receita.idConsulta, receita.descricao, receita.data_emissao, receita.idPaciente)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Receita registrada com sucesso!")
    except mysql.connector.Error as erro:
        print(f"Erro ao registrar receita: {erro}")
        raise
    finally:
        cursor.close()
        conexao.close()

def acessarReceitas(id):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "SELECT * FROM Receita where id_paciente = %s"
        cursor.execute(sql, (id,))
        resultado = cursor.fetchall()
        receitas = []
        for resultado in resultado:
            receita = {
                'id': resultado[0],
                'descricao': resultado[1],
                'data_emissao': resultado[2],
            }
            receitas.append(receita)
        return receitas
    except mysql.connector.Error as erro:
        print(f"Erro ao acessar receita: {erro}")
        raise
    finally:
        cursor.close()
        conexao.close()

def buscarReceita(id):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "SELECT * FROM Receita where id = %s"
        cursor.execute(sql, (id,))
        resultado = cursor.fetchone()
        if resultado:
            receita = Receita(resultado[0], resultado[1], resultado[2], resultado[3])
        return receita
    except mysql.connector.Error as erro:
        print(f"Erro ao acessar receita: {erro}")
        raise
    finally:
        cursor.close()
        conexao.close()