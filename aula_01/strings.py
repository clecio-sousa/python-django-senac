qtde_km = float(input("Digite a quantidade de Km rodados: "))
qtde_dia = int(input("Digite a quantidade de dias: "))

total = (qtde_km * 0.15) + (qtde_dia * 60)
print(f"R${total}")