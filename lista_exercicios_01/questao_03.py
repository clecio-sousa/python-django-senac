deposito_inicial = float(input("Digite o valor do deposito inicial: "))
tx_juros = float(input("Digite o valor da taxa de juros: "))

mes = 1
rendimento = 0
while(mes <= 24):
    deposito_inicial = deposito_inicial + (deposito_inicial*(tx_juros/100))
    mes +=1
    rendimento = (deposito_inicial*(tx_juros/100)) + rendimento
    print(f"{deposito_inicial:.2f}")
print(f"{rendimento:.2f}")