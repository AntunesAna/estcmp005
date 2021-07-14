from Pessoa import Pessoa

class Empregado(Pessoa):
    def __init__(self, salario_empregado, nome_empregado, setor_empregado):
        self.salario = salario_empregado
        self.nome = nome_empregado
        self.setor = setor_empregado

    def descricao(self):
        print("Salario: ", self.salario, "\nSetor: ", self.setor)
