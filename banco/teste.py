from conta import Conta
from cliente import Cliente
from banco import Banco
from time import sleep

cliente_1 = Cliente("Clecio Sousa", "1234-5678", "789-0", "789456-8")
cliente_2 = Cliente("Maria de Jesus", "8974-8956", "854-9", "485269-7")
conta1 = Conta(cliente_1.nome, "789-0", 100)
conta2 = Conta(cliente_2.nome, "125-8", 0)

opcao = 0
while True:

    print("\n||||| BEM VINDO AO BANCO PYTHON |||||"
          "\n\n\t\t1 - CONSULTAR DADOS DA CONTA"
          "\n\t\t2 - SACAR"
          "\n\t\t3 - DEPOSITAR"
          "\n\t\t4 - TRANSFERIR"
          "\n\t\t5 - EXTRATO"
          "\n\t\t6 - HISTORICO"
          "\n\t\t7 - SAIR")
    opcao = int(input("\n\n\tQUAL A SUA OPÇÃO: "))

    if opcao == 7:
        break
    else:
        if opcao == 1:
            print("---MEUS DADOS BANCARIOS---")
            cliente_1.resumo()
            sleep(3)

        elif opcao == 2:

            conta1.sacar()
            sleep(3)

        elif opcao == 3:
            conta1.depositar()
            sleep(3)

        elif opcao == 4:

            conta1.transferir(conta2)


            print(f"SALDO CONTA 1: {conta1.saldo}")
            print(f"SALDO CONTA 2: {conta2.saldo}")
            sleep(3)
        elif opcao == 5:
            conta1.extrato()
            conta2.extrato()

        elif opcao == 6:
            conta1.operacoes






