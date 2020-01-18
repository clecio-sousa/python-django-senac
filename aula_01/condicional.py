tipo_relacao = input("Digite o tipo de relacao:")
qtde_kwh = float(input("Digite a quantidade de Kwh consumida:"))


if(tipo_relacao=="R" or tipo_relacao=="r"):
    
    if (qtde_kwh > 0 and qtde_kwh <500):        
        total= qtde_kwh * 0.4
        print(f"Total a pagar:R${total}")
        
    else:
        total= qtde_kwh * 0.65
        print(f"Total a pagar:R${total}")

elif(tipo_relacao == "C"):
    
    if(qtde_kwh >0 and qtde_kwh<1000):
        
        total= qtde_kwh * 0.55
        print(f"Total a pagar:R${total}")
    else:
        total= qtde_kwh * 0.6
        print(f"Total a pagar:R${total}")

elif(tipo_relacao == "I"):
    
    if(qtde_kwh > 0 and qtde_kwh <5000):
        
        total= qtde_kwh * 0.55
        print(f"Total a pagar:R${total}")
    else:
        total= qtde_kwh * 0.6
        print(f"Total a pagar:R${total}")
            
    