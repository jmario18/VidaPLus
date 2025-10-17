
class Paciente:
    def __init__(self, nome, dataNasc, endereco, cpf, telefone, email, id=None):
        self.id = id
        self.nome = nome
        self.dataNasc = dataNasc
        self.endereco = endereco
        self.telefone = telefone
        self.cpf = cpf
        self.email = email

    def __str__(self):
        return f"Paciente: {self.nome}"
    

