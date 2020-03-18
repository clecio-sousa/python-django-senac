class Paciente:

    def __init__(self):

        #SINTOMAS


    def listar_sintomas_gripe(self):
        print("_" *30)
        print("\nQUESTIONARIO P/ DIAGNOSTICO")
        print("_" * 30)
        self.febre_alta = input("Febre:")
        self.tosse_seca = input("Tosse seca: ")
        self.coriza = input("Coriza: ")
        self.dificuldade_respirar = input("Dificuldade para respirar :")
        self.dores_musculares = input("Dores musculares: ")
        self.diarreia = input("Diarreia: ")
        self.dor_garganta = input("Dor de garganta: ")
        self.dor_cabeca = input("Dor de cabeça: ")


        """print("O paciente apresenta:"
              f"\n\nFebre alta: {self.febre_alta}"
              f"\nTosse seca: {self.tosse_seca}"
              f"\nDificuldade para respirar: {self.dificuldade_respirar}"
              f"\nDores musculares: {self.dores_musculares}"
              f"\nDor de cabeça: {self.dor_cabeca}"
              f"\nCoriza/congestão nasal: {self.coriza}")"""