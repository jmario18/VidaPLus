


class Prontuario:
    def __init__(self, idPaciente, peso, altura, observacoes = None):
        self.idPaciente = idPaciente
        #self.consultas = [] Consultas com o pacienteId igual ao idPaciente aqui pega as consulats com o mesmo paciente id
        self.peso = peso
        self.altura = altura
        #self.medicamentosDiarios = [] Basicamente uma table de medicamentos, na qual o id é o mesmo do paciente, para identificalopega outra tabela dos medicamentos diarios do paciente id
        #self.alergias = [] pega outra tabela das alergias do paciente id
        #self.condicoesMedicas = [] pega outra tabela das condições medicas do paciente id

        self.observacoes = observacoes
