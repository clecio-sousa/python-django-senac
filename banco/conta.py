from cliente import Cliente
class Conta:
    def __init__(self,titular, numero, saldo): # metodo init inicializa o objeto

        self.nome = titular
        self.numero =numero
        self.saldo = saldo
        self.clientes = []
        self.operacoes = []

    def depositar(self):

        valor = float(input("Digite o valor do deposito: "))
        self.saldo += valor
        print(f"Saldo atual: {self.saldo}")
        self.operacoes.append(f"Deposito: {valor}")    

    def sacar(self):

        valor = float(input("Digite o valor do saque: "))
        if(self.saldo < valor):
            print(f"Saldo insuficiente: {self.saldo}")
        else:
            self.saldo -= valor
            print("Saque realizado com sucesso")
            print(f"Saldo atual: {self.saldo}")
            return True
        self.operacoes.append([f"Saque: {valor}"])   


    def transferir(self, destino):

        valor = float(input("Digite o valor a ser transferido: "))
        if (self.saldo < valor):

            print(f"Saldo insuficiente ---- Saldo atual: {self.saldo}")

            return False

        else:
            self.saldo -= valor

            print("TRANSFERENCIA REALIZADA COM SUCESSO")

           # print(f"Saldo atual: {self.saldo}")
            self.operacoes.append([f"Transferencia: {valor},"---f",{destino} "])

    def extrato(self):
        print(f"numero: {self.numero} \nSaldo: {self.saldo}")



