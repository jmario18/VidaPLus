import mysql.connector

from model.Paciente import Paciente

def criar_conexao():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="J0@omarioBull4",
        database="vidaPlus"
    )
def registrarPaciente(nome, dataNasc, cpf, endereco, telefone):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO Paciente (nome, dataNasc, cpf, endereco, telefone) VALUES (%s, %s, %s, %s, %s)"
        valores = (nome, dataNasc, cpf, endereco, telefone)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Paciente registrado com sucesso!")
    except mysql.connector.Error as erro:
        print(f"Erro ao registrar paciente: {erro}")
    finally:
        cursor.close()
        conexao.close()

def consultaPaciente(nome):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "SELECT * FROM paciente WHERE nome = %s"
        cursor.execute(sql, (nome,))
        resultado = cursor.fetchone()
        if resultado:
            paciente = Paciente(resultado[1], resultado[2], resultado[3], resultado[4], resultado[5])
            paciente.id = resultado[0]
            print("Paciente encontrado:")
            return paciente
        else:
            print("Paciente não encontrado.")
    except mysql.connector.Error as erro:
        print(f"Erro ao consultar paciente: {erro}")
    finally:
        cursor.close()
        conexao.close()

def registrarProfissional(nome, email, dataNasc, crm, telefone, cargo):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO Profissional (nome, email, dataNasc, crm, telefone, cargo) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (nome, email, dataNasc, crm, telefone, cargo)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Profissional registrado com sucesso!")
    except mysql.connector.Error as erro:
        print(f"Erro ao registrar profissional: {erro}")
    finally:
        cursor.close()
        conexao.close()

def consultaProfissional(nome):
    conexao = criar_conexao()
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

def registrarLocal(nome):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO Unidade (nome) VALUES (%s)"
        valores = (nome,)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Unidade registrada com sucesso!")
    except mysql.connector.Error as erro:
        print(f"Erro ao registrar unidade: {erro}")
    finally:
        cursor.close()
        conexao.close()

def registrarLeito(unidadeId, numero):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO Leito (numero, idUnidade) VALUES (%s, %s)"
        valores = (numero, unidadeId)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Leito registrado com sucesso!")
    except mysql.connector.Error as erro:
        print(f"Erro ao registrar leito: {erro}")
    finally:
        cursor.close()
        conexao.close()

def registrarConsulta(pacienteId, profissionalId, data, hora, motivo, observacoes):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    data = f"{data} {hora}"
    try:
        sql = "INSERT INTO consulta (pacienteId, profissionalId, dataConsulta, motivo, observacoes) VALUES (%s, %s, %s, %s, %s)"
        valores = (pacienteId, profissionalId, data, motivo, observacoes)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Consulta registrada com sucesso!")
    except mysql.connector.Error as erro:
        print(f"Erro ao registrar consulta: {erro}")
    finally:
        cursor.close()
        conexao.close()


def verificaDisponibilidade(profissionalId, data):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "SELECT * FROM consulta WHERE profissionalId = %s AND dataConsulta = %s"
        cursor.execute(sql, (profissionalId, data))
        resultados = cursor.fetchall()
        print('Resultados da verificação de disponibilidade:')
        print(resultados)
        for resultado in resultados:
            print('Comparando datas:')
            print(f'{resultado[4]}')
            if str(resultado[4]) == f'{data}:00':
                print("Profissional ocupado na data e hora informadas.")
                return False

        print(data)
        print("Profissional disponível na data e hora informadas.")
        return True
    except mysql.connector.Error as erro:
        print(f"Erro ao verificar disponibilidade: {erro}")
    finally:
        cursor.close()
        conexao.close()

    pass
# TODO consultaProntuário

if __name__ == "__main__":
    try:
        conexao = criar_conexao()
        if conexao.is_connected():
            print("Conexão bem-sucedida ao MySQL!")
        conexao.close()
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL:")