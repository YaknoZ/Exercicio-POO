class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def mudarLado(self, novo_lado):
        self.lado = novo_lado
    
    def retornarLado(self):
        return self.lado
    
    def calcularArea(self):
        return self.lado ** 2

quadrado = Quadrado(5)
print("Lado:", quadrado.retornarLado())
print("Área:", quadrado.calcularArea())
quadrado.mudarLado(8)
print("Novo lado:", quadrado.retornarLado())
