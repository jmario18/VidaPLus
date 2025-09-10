

class Administrador:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def alterar_senha(self, nova_senha):
        self.senha = nova_senha

    def __str__(self):
        return f"Administrador: {self.nome}"