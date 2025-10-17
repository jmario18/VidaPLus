import mysql.connector
from connection import connection
from model.Local import Unidade

def registrarLocal(local : Unidade):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO locais (nome, endereco, tipo) VALUES (%s, %s, %s)"
        valores = (local.nome,local.endereco, local.tipo)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Unidade registrada com sucesso!")
    except mysql.connector.Error as erro:
        print(f"Erro ao registrar unidade: {erro}")
    finally:
        cursor.close()
        conexao.close()

def registrarSuprimentosLocal(idLocal):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO suprimentos (unidadeId, soro, gaze, alcool, medicamento) VALUES (%s, 0, 0, 0, 0)"
        cursor.execute(sql, (idLocal,))
        conexao.commit()
    except mysql.connector.Error as erro:
        return f"Erro ao registrar unidade: {erro}"
    finally:
        cursor.close()
        conexao.close()


def buscarLocais(nome):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    if nome == "": nome = "%"  # Buscar todos os locais se o nome estiver vazio
    try:
        sql = "SELECT * FROM locais WHERE nome LIKE %s"
        cursor.execute(sql, (f"%{nome}%",))
        resultados = cursor.fetchall()
        locais = []
        for resultado in resultados:
            local = {
                'id': resultado[0],
                'nome': resultado[1],
                'endereco': resultado[2],
                'tipo':resultado[3]
            }
            locais.append(local)
        return locais
    finally:
        cursor.close()
        conexao.close()

def buscarLocalId(id):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "SELECT nome FROM locais WHERE localId = %s"
        cursor.execute(sql, (id,))
        resultado = cursor.fetchone()
        return resultado
    finally:
        cursor.close()
        conexao.close()

def suprimentosLocal(id):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "SELECT * FROM suprimentos WHERE unidadeId = %s"
        cursor.execute(sql, (id,))
        resultado = cursor.fetchone()
        print(f'resultado agorinha memo: id={id} // {resultado}')
        if resultado:
            suprimentos = {
                'id':resultado[0],
                'soro': resultado[1],
                'gaze': resultado[2],
                'alcool': resultado[3],
                'medicamento':resultado[4]
            }
            return suprimentos
        else:
            return "Não tem"
    finally:
        cursor.close()
        conexao.close()

def atualizarSuprimentosLocal(id, soro, gaze, alcool, medicamento):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "UPDATE suprimentos SET soro = %s, gaze = %s, alcool = %s, medicamento = %s WHERE unidadeId = %s"
        cursor.execute(sql, (soro, gaze, alcool, medicamento,id,))
        conexao.commit()
    finally:
        cursor.close()
        conexao.close()