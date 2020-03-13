t = [-10,-8,0,1,2,5,-2,-4]
novaT=[]
menor = 0
maior = 0

for i in t:
    if i < menor:
        menor=1
        novaT.append(i)
  
novaT.sort

print(novaT)
        
    
    
    
    
    
    
    
"""    menor = min(t)
    maior = max(t)
    soma = sum(t)/len(t)
print(menor, maior,soma)"""
