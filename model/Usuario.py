class Usuario:
    def __init__(self, login, senha, email, isAdmin=False):
        self.login = login
        self.senha = senha
        self.email = email
        self.isAdmin = isAdmin