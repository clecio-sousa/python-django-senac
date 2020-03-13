carrinho = { "Arroz" : [10.0, 2],
            "feijão" : [12.0, 3],
            "Macarrão" : [3.50, 4] }

nome, valor, qtde = carrinho
total = 0
for produto in enumerate(carrinho): 

    preco = valor * qtde
    total = total + preco

print(total)

