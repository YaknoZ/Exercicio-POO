class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
    
    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome
    
    def deposito(self, valor):
        self.saldo += valor
    
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")


conta = ContaCorrente(12345, "João da Silva")
print("Saldo inicial:", conta.saldo)
conta.deposito(500)
print("Novo saldo após depósito:", conta.saldo)
conta.saque(300)
print("Saldo após saque:", conta.saldo)
