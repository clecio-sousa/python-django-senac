class Cliente:
    def __init__(self, nome, telefone, agencia, numero):
        self.nome = nome
        self.telefone = telefone
        self.agencia = agencia
        self.numero = numero


    def resumo(self):

        print(f"Nome: {self.nome}"
              f"\nTelefone: {self.telefone}"
              f"\nAgencia: {self.agencia}"
              f"\nNumero da conta: {self.numero}")

        

