from conta import Conta
minha_conta = Conta('123-4', 'Clecio', 120.0, '1000.0')
"""conta.deposita(20.0)
conta.saca(100)
print(conta.extrato())"""

minha_conta.saldo = 3000
consegui = minha_conta.saca(2000)
if(consegui):
    print("consegui sacar")
    print(f"Saldo: {minha_conta.saldo}")

else:
    print("nao consegui sacar")

