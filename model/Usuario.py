from flask_login import UserMixin


class Usuario(UserMixin):
    def __init__(self,id, login, senha, email,  tipoUsuario, isAdmin=False, idProfissional= None, idPaciente = None):
        self.id = id
        self.login = login
        self.senha = senha
        self.email = email
        self.tipoUsuario = tipoUsuario
        self.isAdmin = isAdmin
        self.idProfissional = idProfissional
        self.idPaciente = idPaciente