import mysql.connector

def criar_conexao():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="J0@omarioBull4",
        database="vidaPlus"
    )

if __name__ == "__main__":
    try:
        conexao = criar_conexao()
        if conexao.is_connected():
            print("Conexão bem-sucedida ao MySQL!")
        conexao.close()
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL:")