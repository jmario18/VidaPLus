from connection import connection
import mysql.connector
from model.Prontuarios import Prontuario

def registrarProntuario(prontuario : Prontuario):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO Prontuario (idPaciente, peso, altura, observacoes) VALUES (%s, %s, %s, %s)"
        valores = (prontuario.idPaciente, prontuario.peso, prontuario.altura, prontuario.observacoes)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Prontuário cadastrado com sucesso!")
    except mysql.connector.Error as erro:
        print(f"Erro ao cadastrar prontuário: {erro}")
    finally:
        cursor.close()
        conexao.close()

def verificaProntuario(idPaciente):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "SELECT * FROM Prontuario WHERE idPaciente = %s"
        cursor.execute(sql, (idPaciente,))
        resultado = cursor.fetchone()
        if resultado:
            prontuario = Prontuario(resultado[0], resultado[1],resultado[2],resultado[3])
            return prontuario
        return 'Não tem'
    finally:
        cursor.close()
        conexao.close()

def registraAlergias(idPaciente, penicilina, amoxilina,ibuprofeno,dipirona,extra1,extra2,extra3):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO alergias (idPaciente, penicilina, amoxicilina, ibuprofeno, dipirona, extra1, extra2, extra3) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (idPaciente, penicilina, amoxilina,ibuprofeno,dipirona,extra1,extra2,extra3)
        cursor.execute(sql, valores)
        conexao.commit()
    except mysql.connector.Error as erro:
        print(f"Erro ao cadastrar prontuário: {erro}")
    finally:
        cursor.close()
        conexao.close()

def verificaAlergias(idPaciente):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "SELECT * FROM alergias WHERE idPaciente = %s"
        cursor.execute(sql, (idPaciente,))
        resultado = cursor.fetchone()
        if resultado:
            alergias = {
                'penicilina': resultado[1],
                'amoxicilina': resultado[2],
                'ibuprofeno': resultado[3],
                'dipirona': resultado[4],
                'extra1': resultado[5],
                'extra2': resultado[6],
                'extra3': resultado[7]
            }
            return alergias
        return None
    finally:
        cursor.close()
        conexao.close()

def registraCondicoes(idPaciente, prAlta, diabetes, asma, eplepsia, hiv, gastrite, extra1, extra2, extra3):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO condicoes (idPaciente, pressaoAlta, diabetes, asma, eplepsia, hiv, gastrite, extra1, extra2, extra3) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (idPaciente, prAlta, diabetes, asma, eplepsia, hiv, gastrite,extra1,extra2,extra3)
        cursor.execute(sql, valores)
        conexao.commit()
    except mysql.connector.Error as erro:
        print(f"Erro ao cadastrar prontuário: {erro}")
    finally:
        cursor.close()
        conexao.close()
    pass

def verificaCondicoes(idPaciente):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "SELECT * FROM condicoes WHERE idPaciente = %s"
        cursor.execute(sql, (idPaciente,))
        resultado = cursor.fetchone()
        if resultado:
            alergias = {
                'Pressão Alta': resultado[1],
                'Diabetes': resultado[2],
                'Asma': resultado[3],
                'Epilepsia': resultado[4],
                'HIV': resultado[5],
                'Gastrite': resultado[6],
                'extra1': resultado[7],
                'extra2': resultado[8],
                'extra3': resultado[9]
            }
            return alergias
        return None
    finally:
        cursor.close()
        conexao.close()

def gerarProntuario():
    # TODO Disponível para profissionais.
    # TODO Gerar prontuário do paciente
    pass