class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def imprimir(self):
        print("Coordenadas:", self.x, ",", self.y)

class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura
    
    def encontrarCentro(self):
        centro_x = self.ponto_inicial.x + self.largura / 2
        centro_y = self.ponto_inicial.y + self.altura / 2
        return Ponto(centro_x, centro_y)


ponto_inicial = Ponto(1, 2)
retangulo = Retangulo(ponto_inicial, 5, 3)
centro = retangulo.encontrarCentro()
centro.imprimir()
