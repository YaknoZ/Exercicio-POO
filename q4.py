class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self):
        if self.idade < 21:
            self.altura += 0.5
        self.idade += 1
    
    def engordar(self, aumento_peso):
        self.peso += aumento_peso
    
    def emagrecer(self, reducao_peso):
        self.peso -= reducao_peso
    
    def crescer(self, aumento_altura):
        self.altura += aumento_altura


pessoa = Pessoa("João", 18, 70, 170)
pessoa.envelhecer()
print("Idade:", pessoa.idade)
print("Altura:", pessoa.altura)
pessoa.engordar(5)
print("Peso:", pessoa.peso)
