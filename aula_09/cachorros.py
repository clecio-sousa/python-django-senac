class Cachorro:
    def __init__(self, nome, tamanho, raca):
        self.nome = nome
        self.tamanho = tamanho
        self.raca = raca
    
    def latir(self):
        print("Au au au")

nico = Cachorro('Nico', 50, 'poodle')
print(nico.nome)
print(nico.tamanho)
print(nico.raca)
nico.latir()
       