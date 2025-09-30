


class Profissional:


    def __init__(self, nome, cargo, email, telefone, crm, dataNasc):
        self.id = None
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cargo = cargo
        self.crm = crm
        self.dataNasc = dataNasc

    def __str__(self):
        return f"{self.cargo}: {self.nome}"