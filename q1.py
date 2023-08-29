class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def trocaCor(self, nova_cor):
        self.cor = nova_cor
    
    def mostraCor(self):
        return self.cor

bola = Bola("vermelho", 20, "couro")
print("Cor da bola:", bola.mostraCor())
bola.trocaCor("azul")
print("Nova cor da bola:", bola.mostraCor())