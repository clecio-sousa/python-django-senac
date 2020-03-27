class Hospital:
    def __init__(self):

        self.nome= ''
        self.idade = 0
        self.nome_tabela_geral = ""
        self.idade_tabela_geral = ""
        self.resultado_diagnostico_tabela_geral = ""
        self.idade_risco = ''
        self.sexo = ''
        self.lista_pacientes = []
        self.resposta = ''
        self.febre_alta = ''
        self.temp_febre = ''
        self.tosse_seca = ''
        self.diarreia = ''
        self.dificuldade_respirar = ''
        self.coriza = ''
        self.lista_resultado = []
        self.lista_pacientes_infectados = []


    # Cadastro de pacientes com sintomas
    def cadastrar_pacientes(self):

        self.nome = input("\nNOME DO PACIENTE: ")
        self.idade = int(input("IDADE DO PACIENTE: "))
        if(self.idade >= 60):
            self.idade_risco = "Paciente faz parte do grupo de risco"
        self.sexo = input("SEXO DO PACIENTE: ")


    # Diagnostico do paciente
    def diagnostico(self):

        print("\n\t\t\t\tSINTOMAS")
        print("\t ", "_" * 25)
        print("\n0 - NÃO"
              "\t\t1 - SIM")

        self.resultado_diagnostico =0

        self.febre_alta = int(input("\n1.Febre alta: "))
        if(self.febre_alta == 1):
            self.temp_febre = int(input("1.1 Qual a temperatura da febre: "))
            if(self.temp_febre >=39):
                self.febre_alta = "Febre igual ou acima de 39º"
            self.resultado_diagnostico += 1
        self.lista_resultado.append(f"febre alta : {self.febre_alta}")

        self.tosse_seca = int(input("2.Tosse seca: "))
        if(self.tosse_seca == 1):
            self.resultado_diagnostico += 1
        self.lista_resultado.append(f"tosse seca: {self.tosse_seca}")

        self.diarreia = int(input("3.Diarreia: "))
        if (self.diarreia == 1):
            self.resultado_diagnostico += 1
        self.lista_resultado.append(f"Diarreia: {self.diarreia}")

        self.dificuldade_respirar = int(input("4.Dificuldade p/respirar: "))
        if (self.dificuldade_respirar == 1):
            self.resultado_diagnostico += 1
        self.lista_resultado.append(f"dificuldade p/ respirar: {self.dificuldade_respirar}")

        self.coriza = int(input("5.Coriza/congestão nasal: "))
        if (self.coriza == 1):
            self.resultado_diagnostico += 1
        self.lista_resultado.append(f"Coriza/congestão nasal: {self.coriza}")


    def resultado(self):

        if self.resultado_diagnostico >= 4 and self.temp_febre >= 39 and self.dificuldade_respirar == 1:
            self.resultado_diagnostico = "Positivo"
            self.lista_pacientes_infectados.append("%-15s %-15d %s" % (self.nome, self.idade, self.resultado_diagnostico))
            print(red, f"PACIENTE É SUSPEITO PARA COVID - 19", reset)

        else:
            self.resultado_diagnostico = "Negativo"
            print(green, "PACIENTE NÃO É SUSPEITO PARA COVID - 19", reset)

        self.lista_pacientes.append("%-15s %-15d %s" % (self.nome, self.idade, self.resultado_diagnostico))

    # Listagem geral de pacientes
    def listar_pacientes_geral(self):
        self.nome_tabela_geral = "NOME"
        self.idade_tabela_geral = "IDADE"
        self.resultado_diagnostico_tabela_geral = "RESULTADO"

        print("LISTA DE PACIENTES GERAL")
        print("%-15s %-15s %s" % (self.nome_tabela_geral, self.idade_tabela_geral, self.resultado_diagnostico_tabela_geral))

        for index, paciente in enumerate(self.lista_pacientes):
            print(index + 1, paciente)

    def listar_pacientes_infectados(self):
        self.nome_tabela_infectado = "NOME"
        self.idade_tabela_infectado = "IDADE"
        self.resultado_diagnostico_tabela_infectado = "RESULTADO"

        print("\nLISTA DE PACIENTES INFECTADOS")
        print("%-15s %-15s %s" % (self.nome_tabela_infectado, self.idade_tabela_infectado, self.resultado_diagnostico_tabela_infectado))

        for index, paciente in enumerate(self.lista_pacientes_infectados):
            print(index + 1, paciente)

#tabela c/cores
red = "\033[1;31m"
blue = "\033[1;34m"
green = "\033[0;32m"
reset = "\033[0;0m"


