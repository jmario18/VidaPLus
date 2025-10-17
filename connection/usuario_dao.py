from connection import connection
import mysql.connector
from model.Usuario import Usuario

def login(usuario):
    try:
        conexao = connection.criar_conexao()
        cursor = conexao.cursor()
        sql = "SELECT * FROM usuario WHERE nomeUsuario = %s "
        cursor.execute(sql, (usuario,))
        usuario = cursor.fetchone()
        if usuario:
            if usuario[3] == 1:
                user = Usuario(id =usuario[0], login=usuario[1], senha=usuario[2], isAdmin=True, email=usuario[4], tipoUsuario=usuario[5])
            else:
                user = Usuario(id =usuario[0], login=usuario[1], senha=usuario[2], isAdmin=False, email=usuario[4], tipoUsuario=usuario[5])
            return user
    finally:
        cursor.close()
        conexao.close()

def alterarU(id, senha):
    try:
        conexao = connection.criar_conexao()
        cursor = conexao.cursor()
        sql = "update usuario set senha = %s where userId = %s "
        valores = (senha, id)
        print(senha)
        cursor.execute(sql, valores)
        usuario = cursor.fetchone()
        print(f'alterando usuario {senha}')
        if usuario:
            if usuario[3] == 1:
                user = Usuario(id =usuario[0], login=usuario[1], senha=usuario[2], isAdmin=True, email=usuario[4], tipoUsuario=usuario[5])
            else:
                user = Usuario(id =usuario[0], login=usuario[1], senha=usuario[2], isAdmin=False, email=usuario[4], tipoUsuario=usuario[5])
            return user
    finally:
        cursor.close()
        conexao.close()



def registrarUsuario(username, senha, email):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO Usuario (nomeUsuario, senha, email, isAdmin) VALUES (%s, %s, %s, %s, %s)"
        valores = (username, senha, email, "1")  # isAdmin definido como 1 (verdadeiro) por padrão
        cursor.execute(sql, valores)
        conexao.commit()
    except mysql.connector.Error as erro:
        print(f"Erro ao cadastrar usuário: {erro}")
    finally:
        cursor.close()
        conexao.close()

def registrarUsuarioPaciente(username, senha, email, idPaciente):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO Usuario (nomeUsuario, senha, email, isAdmin, tipoUsuario, idPaciente) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (username, senha, email, "0", "paciente", idPaciente)  # isAdmin definido como 0 (falso) por padrão
        cursor.execute(sql, valores)
        conexao.commit()
    except mysql.connector.Error as erro:
        print(f"Erro ao cadastrar usuário: {erro}")
    finally:
        cursor.close()
        conexao.close()

def registrarUsuarioProfissional(username, senha, email, id):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO Usuario (nomeUsuario, senha, email, isAdmin, tipoUsuario, idProfissional) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (username, senha, email, "0", "profissional", id)  # isAdmin definido como 0 (falso) por padrão
        cursor.execute(sql, valores)
        conexao.commit()
    except mysql.connector.Error as erro:
        print(f"Erro ao cadastrar usuário: {erro}")
    finally:
        cursor.close()
        conexao.close()

def buscarUsuarioPorId(user_id):
    conexao = connection.criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "SELECT * FROM Usuario WHERE userId = %s"
        cursor.execute(sql, (user_id,))
        resultado = cursor.fetchone()
        return resultado
    except mysql.connector.Error as erro:
        print(f"Erro ao buscar usuário por ID: {erro}")
        return None
    finally:
        cursor.close()
        conexao.close()