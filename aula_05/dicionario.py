estoque = {
        "manga" : 1.15,
        "feijao" : 13.50,
        "arroz" : 2.70
        }



print(estoque["feijao"])
estoque["arroz"] = 12.70
estoque.update({"macarrao":2.5})#adiciona novos valores
estoque["morango"] = 10.5#adiciona novos valores
del estoque["manga"] #deleta o indice manga
print(estoque)


for produto in estoque:
    total = 0
    total = total + estoque[produto]
    print(produto, "=",estoque[produto])
print(total)
