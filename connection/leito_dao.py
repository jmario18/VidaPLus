import mysql.connector
from connection import connection
from model.Leito import Leito

def registrarLeito(leito :Leito):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    print(leito.idUnidade)
    try:
        sql = "INSERT INTO Leito (numero, idUnidade,tipo, statusLeito) VALUES (%s, %s, %s, %s)"
        valores = (leito.numero, leito.idUnidade, leito.tipo, leito.status)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Leito registrado com sucesso!")
    except mysql.connector.Error as erro:
        print(f"Erro ao registrar leito: {erro}")
    finally:
        cursor.close()
        conexao.close()

def buscarLeitos(numero):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    if numero == "": numero = "%"  # Buscar todos os leitos se o número estiver vazio
    try:
        sql = "SELECT * FROM Leito WHERE numero LIKE %s"
        cursor.execute(sql, (f"%{numero}%",))
        resultados = cursor.fetchall()
        leitos = []
        for resultado in resultados:
            leito = {
                'id': resultado[0],
                'numero': resultado[1],
                'unidadeId': resultado[2],
                'tipo':resultado[3],
                'statusLeito':resultado[4],
                'observacoes':resultado[5],
                'idPaciente':resultado[6]
            }
            leitos.append(leito)
        return leitos
    finally:
        cursor.close()
        conexao.close()

def buscarLeitoPorId(id):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "SELECT * FROM Leito WHERE id LIKE %s"
        cursor.execute(sql, (id,))
        resultado = cursor.fetchone()
        if resultado:
            leito = {
                'id': resultado[0],
                'numero': resultado[1],
                'unidadeId': resultado[2],
                'tipo':resultado[3],
                'statusLeito':resultado[4],
                'observacoes':resultado[5],
                'idPaciente':resultado[6]
            }
            return leito
        return None
    finally:
        cursor.close()
        conexao.close()

def buscarLeitoPorUnidade(id):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "SELECT * FROM Leito WHERE idUnidade = %s"
        cursor.execute(sql, (id,))
        resultados = cursor.fetchall()
        leitos = []
        print(id)
        for resultado in resultados:
            leito = {
                'id': resultado[0],
                'numero': resultado[1],
                'unidadeId': resultado[2],
                'tipo':resultado[3],
                'statusLeito':resultado[4],
                'observacoes':resultado[5],
                'idPaciente':resultado[6]
            }
            leitos.append(leito)
        return leitos
    finally:
        cursor.close()
        conexao.close()

def colocarPaciente(idLeito, idPaciente):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    
    try:
        sql = "UPDATE Leito SET idPaciente = %s WHERE id = %s"
        valores = (int(idPaciente), idLeito)
        cursor.execute(sql, valores)
        conexao.commit()
    except mysql.connector.Error as erro:
        print(f"Erro ao registrar leito: {erro}")
    finally:
        cursor.close()
        conexao.close()

def leitoDisponivel(idLeito):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    
    try:
        sql = "UPDATE Leito SET statusLeito = 'indisponivel' WHERE id = %s"
        cursor.execute(sql, (idLeito,))
        conexao.commit()
    except mysql.connector.Error as erro:
        print(f"Erro ao registrar leito: {erro}")
    finally:
        cursor.close()
        conexao.close()

def atualizarObs(idLeito, obs):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    
    try:
        sql = "UPDATE Leito SET observacoes = %s WHERE id = %s"
        cursor.execute(sql, (obs, idLeito))
        conexao.commit()
    except mysql.connector.Error as erro:
        print(f"Erro ao registrar leito: {erro}")
    finally:
        cursor.close()
        conexao.close()


def removerPaciente(idLeito):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "UPDATE Leito SET idPaciente = NULL WHERE id = %s"
        cursor.execute(sql, (idLeito,))
        conexao.commit()
    except mysql.connector.Error as erro:
        print(f"Erro ao registrar leito: {erro}")
    finally:
        cursor.close()
        conexao.close()

def leitoIndisponivel(idLeito):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    
    try:
        sql = "UPDATE Leito SET statusLeito = 'disponivel' WHERE id = %s"
        cursor.execute(sql, (idLeito,))
        conexao.commit()
    except mysql.connector.Error as erro:
        print(f"Erro ao registrar leito: {erro}")
    finally:
        cursor.close()
        conexao.close()

def apagaObs(idLeito):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    
    try:
        sql = "UPDATE Leito SET observacoes = NULL WHERE id = %s"
        cursor.execute(sql, (idLeito,))
        conexao.commit()
    except mysql.connector.Error as erro:
        print(f"Erro ao registrar leito: {erro}")
    finally:
        cursor.close()
        conexao.close()