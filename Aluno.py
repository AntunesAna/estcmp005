from Person import Person

class Aluno(Person):
	def __init__(self):
		Person.__init__(self)
		self.curso = None
		self.turno = "matutino"
		self.periodo = 6
		
	def set_curso(self, curso):
		self.curso = curso
		
	def set_turno(self, turno):
		self.turno = turno
		
	def set_periodo(self, periodo):
		self.periodo = periodo
		
	def descricaoAluno(self):
		print("Curso: ", self.curso, "\Turno:", self.turno, "\nPeríodo: ", self.periodo)
