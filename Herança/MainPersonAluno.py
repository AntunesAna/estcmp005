from Person import Person
from Aluno import Aluno

pessoa = Person()
alu1 = Aluno()
alu2 = Aluno()

alu1.set_nome ("José Gonçalves")
alu1.set_cpf("123456789")
alu1.set_curso ("Engenharia Mecânica")

alu2.set_nome ("Maria Magalhães")
alu2.set_cpf("987654321")
alu2.set_curso ("Engenharia Química")

alu1.descricaoPessoa()
alu1.descricaoAluno()

alu2.descricaoPessoa()
alu2.descricaoAluno()
