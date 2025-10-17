

class Leito:
    def __init__(self, numero, tipo, idUnidade, paciente=None, observacoes=None, id=None, status="disponivel"):
        self.id = id
        self.numero = numero
        self.tipo = tipo
        self.idUnidade = idUnidade
        self.status = status
        self.observacoes = observacoes
        self.paciente = paciente