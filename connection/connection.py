import mysql.connector

def criar_conexao():
    return mysql.connector.connect(
        host="localhost",
        user="seu_usuario",
        password="senha",
        database="seu_banco"
    )
def registrarPaciente(nome, idade, endereco, telefone):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO paciente (nome, idade, endereco, telefone) VALUES (%s, %s, %s, %s)"
        valores = (nome, idade, endereco, telefone)
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
            print("Paciente encontrado:")
            print(f"Nome: {resultado[1]}")
            print(f"Idade: {resultado[2]}")
            print(f"Endereço: {resultado[3]}")
            print(f"Telefone: {resultado[4]}")
        else:
            print("Paciente não encontrado.")
    except mysql.connector.Error as erro:
        print(f"Erro ao consultar paciente: {erro}")
    finally:
        cursor.close()
        conexao.close()

def registrarProfissional(nome, cargo, email, telefone, crm):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO profissional (nome, cargo, email, telefone, crm) VALUES (%s, %s, %s, %s, %s)"
        valores = (nome, cargo, email, telefone, crm)
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

def registrarLocal(nome, endereco, tipo):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO unidade (nome, endereco, tipo) VALUES (%s, %s, %s)"
        valores = (nome, endereco, tipo)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Unidade registrada com sucesso!")
    except mysql.connector.Error as erro:
        print(f"Erro ao registrar unidade: {erro}")
    finally:
        cursor.close()
        conexao.close()

# TODO consultaProntuário

if __name__ == "__main__":
    try:
        conexao = criar_conexao()
        if conexao.is_connected():
            print("Conexão bem-sucedida ao MySQL!")
        conexao.close()
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL:")