


class Profissional:


    def __init__(self, nome, cargo, email, telefone, crm, dataNasc, cpf, id=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cargo = cargo
        self.crm = crm
        self.dataNasc = dataNasc
        self.cpf = cpf

    def __str__(self):
        return f"{self.cargo}: {self.nome}"