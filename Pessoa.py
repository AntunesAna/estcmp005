class Pessoa():

    def __init__(self, nome, idade, residencia):
        self.nome = nome
        self.idade = idade
        self.residencia = residencia

    def descricao(self):
        print("Nome: ", self.nome, "\Idade:", self.idade, "\nlugar de residencia: ", self.residencia)

