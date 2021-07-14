class Person:
	def __init__(self):
		self.nome = "Lucas da Silva"
		self.cpf = "05687563575"
		
	def set_nome(self, novo_nome):
		self.nome = novo_nome
		
	def set_cpf(self, novo_cpf):
		self.cpf = novo_cpf
		
	def descricaoPessoa(self):
		print("Nome: ", self.nome, "CPF:", self.cpf)
