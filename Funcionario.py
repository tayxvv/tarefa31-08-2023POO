class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def getNome(self):
        return self.nome
    
    def getSalario(self):
        return self.salario
    
    def aumentarSalario(self, percentual):
        self.salario += self.salario * (percentual / 100)
        return self.salario
    