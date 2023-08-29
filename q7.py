class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.saude = 50
        self.idade = 0
    
    def alterarNome(self, novo_nome):
        self.nome = novo_nome
    
    def alterarFome(self, valor):
        self.fome = valor
    
    def alterarSaude(self, valor):
        self.saude = valor
    
    def alterarIdade(self, valor):
        self.idade = valor
    
    def retornarNome(self):
        return self.nome
    
    def retornarFome(self):
        return self.fome
    
    def retornarSaude(self):
        return self.saude
    
    def retornarIdade(self):
        return self.idade
    
    def calcularHumor(self):
        return (self.fome + self.saude) / 2


bichinho = BichinhoVirtual("Fofinho")
print("Nome:", bichinho.retornarNome())
print("Fome:", bichinho.retornarFome())
print("Saúde:", bichinho.retornarSaude())
print("Idade:", bichinho.retornarIdade())
bichinho.alterarFome(20)
bichinho.alterarSaude(80)
print("Humor:", bichinho.calcularHumor())
