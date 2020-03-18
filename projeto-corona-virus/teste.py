from hospital import Hospital
# noinspection PyUnresolvedReferences
from sintomas import Paciente

paciente_1 = Hospital()
paciente_sintomas = Paciente()

opcao = 0
while (True):

    print("\n||||| BEM VINDO AO HOSPITAL PYTHON |||||"
          "\n\n\t\t1 - CADASTRAR PACIENTE"
          "\n\t\t2 - SAIR")

    opcao = int(input("DIGITE UMA OPCAO :"))

    if opcao == 2:
        break

    else:
        if (opcao == 1):
            paciente_1.cadastrar_pacientes()
            paciente_sintomas.listar_sintomas_gripe()



