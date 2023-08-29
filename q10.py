class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel
    
    def abastecerPorValor(self, valor):
        litros_abastecidos = valor / self.valor_litro
        self.quantidade_combustivel -= litros_abastecidos
        return litros_abastecidos
    
    def abastecerPorLitro(self, litros):
        valor_a_pagar = litros * self.valor_litro
        self.quantidade_combustivel -= litros
        return valor_a_pagar
    
    def alterarValor(self, novo_valor_litro):
        self.valor_litro = novo_valor_litro
    
    def alterarCombustivel(self, novo_tipo_combustivel):
        self.tipo_combustivel = novo_tipo_combustivel
    
    def alterarQuantidadeCombustivel(self, nova_quantidade_combustivel):
        self.quantidade_combustivel = nova_quantidade_combustivel


bomba = BombaCombustivel("Gasolina", 4.5, 1000)
litros_abastecidos = bomba.abastecerPorValor(50)
print("Litros abastecidos:", litros_abastecidos)
print("Quantidade restante:", bomba.quantidade_combustivel)
bomba.alterarValor(4.8)
print("Novo valor do litro:", bomba.valor_litro)
