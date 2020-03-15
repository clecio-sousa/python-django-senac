class Conta:
    def __init__(self, clientes, numero, saldo, operacoes = [] ): # metodo init inicializa o objeto

        self.numero = numero
        self.saldo = saldo
        self.clientes = clientes        
        self.operacoes = operacoes

    def depositar(self, valor):
        self.saldo += valor

        self.operacoes.append(f"Deposito: {valor}")    

    def sacar(self, valor):

        if(self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            return True
        self.operacoes.append([f"Saque: {valor}"])   
    

    def extrato(self):
        print(f"numero: {self.numero} \nSaldo: {self.saldo}")



