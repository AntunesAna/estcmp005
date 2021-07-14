class Conta:
        def __init__(self, Cliente):
                self.cliente = "Maria Eduarda"
                self.numero = 0
                self.historico = Historico()
		
        def set_cliente(cliente):
                self.cliente = cliente

        def __str__(self):
                return "\nCliente: " + str(self.cliente) + "\nNumero: " + str(self.numero) + "\n\nHistórico " + str(self.historico)

class Historico:
        def __init__(self):
                self.data_abertura = "15/06/2003"
                self.transacoes = [1, 2, 3]
        def __str__(self):
                return "\nData de Abertura: " + str(self.data_abertura) + "\nTransações: " + str(self.transacoes)

class Cliente:
        def __init__(self):
                self.nome = "Maria Eduarda"
                self.cpf = "123456789"
                
        def set_nome(nome):
                self.nome = nome
                
        def set_cpf(cpf):
                self.cpf = cpf

        def __str__(self):
                return "\nNome: " + str(self.nome) + "\n CPF: " + str(self.cpf)



