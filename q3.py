class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
    
    def mudarLados(self, novo_ladoA, novo_ladoB):
        self.ladoA = novo_ladoA
        self.ladoB = novo_ladoB
    
    def retornarLados(self):
        return self.ladoA, self.ladoB
    
    def calcularArea(self):
        return self.ladoA * self.ladoB
    
    def calcularPerimetro(self):
        return 2 * (self.ladoA + self.ladoB)

# Exemplo de uso
retangulo = Retangulo(4, 6)
print("Lados:", retangulo.retornarLados())
print("Área:", retangulo.calcularArea())
print("Perímetro:", retangulo.calcularPerimetro())
retangulo.mudarLados(5, 7)
print("Novos lados:", retangulo.retornarLados())
