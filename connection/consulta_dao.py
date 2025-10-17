import mysql.connector
from connection import connection
import random
from model.Consulta import Consulta

def registrarConsultaOnline(pacienteId, profissionalId, data, hora, motivo, observacoes):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    data = f"{data} {hora}"
    chave = random.randint(1,999999)
    try:
        sql = "INSERT INTO consulta (pacienteId, profissionalId, dataConsulta, motivo, observacoes, chave, statusConsulta) VALUES (%s, %s, %s, %s, %s, %s, 'Pendente')"
        valores = (pacienteId, profissionalId, data, motivo, observacoes, chave)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Consulta registrada com sucesso!")
    except mysql.connector.Error as erro:
        print(f"Erro ao registrar consulta:{profissionalId} , {erro}")
    finally:
        cursor.close()
        conexao.close()

def registrarConsulta(pacienteId, profissionalId, data, hora, motivo, observacoes, local):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    data = f"{data} {hora}" 
    print(f'local = {local}')
    try:
        sql = "INSERT INTO consulta (pacienteId, profissionalId, dataConsulta, motivo, observacoes, idLocal, statusConsulta) VALUES (%s, %s, %s, %s, %s, %s, 'Pendente')"
        valores = (pacienteId, profissionalId, data, motivo, observacoes, local)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Consulta registrada com sucesso!")
    except mysql.connector.Error as erro:
        print(f"Erro ao registrar consulta:{profissionalId} , {erro}")
    finally:
        cursor.close()
        conexao.close()

def registrarDiagnostico(idConsulta, diagnostico):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    print(idConsulta)
    print(diagnostico)
    try:
        sql = "UPDATE Consulta SET diagnostico = %s WHERE consultaId = %s"
        valores = (diagnostico, idConsulta)
        cursor.execute(sql, valores)
        conexao.commit()
        return True
    except mysql.connector.Error as erro:
        print(f"Erro ao alterar paciente: {erro}")
        return False
    finally:
        cursor.close()
        conexao.close()

def alterarStatus(id):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()

    try:
        sql = " UPDATE Consulta SET statusConsulta = 'Finalizada' where consultaId = %s"
        cursor.execute(sql, (id,))
        conexao.commit()
        return True
    except mysql.connector.Error as erro:
        print(f"Erro ao alterar paciente: {erro}")
        return False
    finally:
        cursor.close()
        conexao.close()


def buscarConsulta(pacienteId):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = """
        SELECT c.consultaId, p.nome, c.dataConsulta, c.motivo, c.observacoes, c.chave, c.diagnostico, c.statusConsulta, l.nome AS nomeLocal
        FROM consulta c
        JOIN paciente p ON c.pacienteId = p.pacienteId
        LEFT JOIN locais l ON c.idLocal = l.localId
        WHERE c.pacienteId = %s AND c.dataConsulta >= CURDATE() AND c.statusConsulta = 'Pendente'
        ORDER BY c.dataConsulta ASC
        """
        valores = (pacienteId)
        cursor.execute(sql, (valores,))
        resultado = cursor.fetchall()
        consultas = []
        for resultado in resultado:
            consulta = {
                'id': resultado[0],
                'pacienteNome': resultado[1],
                'dataConsulta': resultado[2],
                'motivo': resultado[3],
                'observacoes': resultado[4],
                'chave': resultado[5],
                'diagnosico': resultado[6],
                'local' : resultado[8],
                'status': resultado[7]
            }
            consultas.append(consulta)
        return consultas
    except mysql.connector.Error as erro:
        print(f"Erro ao registrar consulta: {erro}")
    finally:
        cursor.close()
        conexao.close()

def buscarConsultaAntigas(pacienteId):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = """
        SELECT c.consultaId, p.nome, c.dataConsulta, c.motivo, c.observacoes, c.chave, c.diagnostico, c.statusConsulta, l.nome AS nomeLocal
        FROM consulta c
        JOIN paciente p ON c.pacienteId = p.pacienteId
        LEFT JOIN locais l ON c.idLocal = l.localId
        WHERE c.pacienteId = %s AND c.statusConsulta = 'Finalizada'
        ORDER BY c.dataConsulta ASC
        """
        valores = (pacienteId)
        cursor.execute(sql, (valores,))
        resultado = cursor.fetchall()
        consultas = []
        for resultado in resultado:
            consulta = {
                'id': resultado[0],
                'pacienteNome': resultado[1],
                'dataConsulta': resultado[2],
                'motivo': resultado[3],
                'observacoes': resultado[4],
                'chave': resultado[5],
                'diagnosico': resultado[6],
                'local' : resultado[8],
                'status': resultado[7]
            }
            consultas.append(consulta)
        return consultas
    except mysql.connector.Error as erro:
        print(f"Erro ao registrar consulta: {erro}")
    finally:
        cursor.close()
        conexao.close()        

def buscarConsultaProfissionalData(profissionalId, data=None):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    print(f'data1 = {data}')
    try:
        if data != None:
            sql = """
                SELECT c.consultaId, p.nome, c.dataConsulta, c.motivo, c.observacoes, c.chave, c.diagnostico, c.statusConsulta, l.nome AS nomeLocal
                FROM consulta c
                JOIN paciente p ON c.pacienteId = p.pacienteId
                LEFT JOIN locais l ON c.idLocal = l.localId
                WHERE c.profissionalId = %s AND DATE(c.dataConsulta) = %s and c.statusConsulta = 'Pendente'
                ORDER BY c.dataConsulta ASC
            """
            cursor.execute(sql, (profissionalId, data))
        else:
            sql = """
                SELECT c.consultaId, p.nome, c.dataConsulta, c.motivo, c.observacoes, c.chave, c.diagnostico, c.statusConsulta, l.nome AS nomeLocal
                FROM consulta c
                JOIN paciente p ON c.pacienteId = p.pacienteId
                LEFT JOIN locais l ON c.idLocal = l.localId
                WHERE c.profissionalId = %s AND DATE(c.dataConsulta) >= curdate() and c.statusConsulta = 'Pendente'
                ORDER BY c.dataConsulta ASC
            """
            cursor.execute(sql, (profissionalId,))
        resultados = cursor.fetchall()
        consultas = []
        for resultado in resultados:
            consulta = {
                'id': resultado[0],
                'pacienteNome': resultado[1],
                'dataConsulta': resultado[2],
                'motivo': resultado[3],
                'observacoes': resultado[4],
                'chave': resultado[5],
                'diagnosico': resultado[6],
                'local' : resultado[8],
                'status': resultado[7]
            }
            consultas.append(consulta)
        print(consultas)
        return consultas
    finally:
        cursor.close()
        conexao.close()

def buscarConsultaPorId(consultaId):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "SELECT * FROM consulta WHERE consultaId = %s"
        cursor.execute(sql, (consultaId,))
        resultado = cursor.fetchone()
        if resultado:
            consulta = Consulta( resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[5])
            return consulta
        return None
    finally:
        cursor.close()
        conexao.close()

def buscarConsultaPorChave(chave):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "SELECT * FROM consulta WHERE chave = %s"
        cursor.execute(sql, (chave,))
        resultado = cursor.fetchone()
        if resultado:
            consulta = Consulta( resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[5])
            return consulta
        return None
    finally:
        cursor.close()
        conexao.close()