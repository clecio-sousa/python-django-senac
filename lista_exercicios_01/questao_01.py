valor_casa = float(input("Digite o valor da casa: "))
valor_salario = float(input("Digite o salario: "))
qtde_meses = int(input("Em quantos meses quer quitar a casa: "))

sal_reduzido = (valor_salario*0.3)
valor_prestacao = valor_casa/qtde_meses

print("||CALCULO DA NEGOCIAÇÃO||")

if(valor_prestacao > sal_reduzido):
    print(f"VALOR DA PRESTAÇÃO - R${valor_prestacao:.2f}||| 30% DO SALARIO- R${sal_reduzido:.2f}")
    print("EMPRESTIMO NÃO APROVADO: VALOR DA PRESTAÇÃO É SUPERIOR A 30% DO SALARIO")

else:
    print(f"VALOR DA PRESTAÇÃO - R${valor_prestacao:.2f}||| 30% DO SALARIO- R${sal_reduzido:.2f}")
    print("EMPRESTIMO APROVADO")

