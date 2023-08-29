class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []
    
    def comer(self, alimento):
        self.bucho.append(alimento)
    
    def verBucho(self):
        return self.bucho
    
    def digerir(self):
        if len(self.bucho) > 0:
            alimento_digerido = self.bucho.pop(0)
            print(f"{alimento_digerido} foi digerido.")


macaco1 = Macaco("Curioso")
macaco2 = Macaco("Guloso")
macaco1.comer("Banana")
macaco1.comer("Maçã")
macaco2.comer("Nozes")
print("Bucho de macaco1:", macaco1.verBucho())
macaco1.digerir()
print("Bucho de macaco1 após digestão:", macaco1.verBucho())
