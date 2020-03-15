from conta import Conta
from cliente import Cliente
from banco import Banco

cliente_1 = Cliente("Clecio", "123-4567")
cliente_2 = Cliente("Maria", "789-4561")

conta_1 = Conta([cliente_1], "120-1", 1000)
conta_2 = Conta([cliente_1, cliente_2],  "140-6", 100)

conta_1.sacar(50)
conta_2.sacar(20)


print("Saldo da conta 1:", conta_1.saldo)
print("Saldo da conta 2:",  conta_2.saldo)

