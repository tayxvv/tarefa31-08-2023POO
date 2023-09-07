class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudarLado(self, lado):
        self.lado = lado

    def retornarLado(self):
        return self.lado
    
    def calcularArea(self):
        return self.lado * self.lado