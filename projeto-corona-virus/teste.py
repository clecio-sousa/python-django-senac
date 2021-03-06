from hospital import Hospital
from time import sleep

#tabela c/cores
red = "\033[1;31m"
green = "\033[0;32m"
reset = "\033[0;0m"

paciente = Hospital()

while (True):

    print("\n\t|| CENTRO DE DIAGNOSTICO PARA COVID - 19 ||"
          "\n\n\t\t1 - CADASTRAR PACIENTE"
          "\n\t\t2 - LISTAR PACIENTES INFECTADOS"
          "\n\t\t3 - LISTAR PACIENTES GERAL"
          "\n\t\t4 - SAIR")

    opcao = int(input("\n\t\tDIGITE UMA OPCAO :"))

    if (opcao == 4):
        print(green, "Saindo do sistema...", reset)
        sleep(2)
        break
    else:
        if (opcao == 1):
            while (True):
                print("\n\t\tCADASTRO DO PACIENTE")
                print("\t ", "_" * 25)
                paciente.cadastrar_pacientes()
                paciente.diagnostico()
                paciente.resultado()

                print("\n N - NOVO PACIENTE"
                      "\t\tS - SAIR")
                sair = input("OPÇÃO:")
                if sair == 's':
                    break
                elif sair == 'n':
                    continue

        elif (opcao == 2):
            paciente.listar_pacientes_infectados()

        elif (opcao == 3):
            paciente.listar_pacientes_geral()

        else:
            print(red, "Digite uma opção válida", reset)


