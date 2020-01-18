"""n = 1
soma = 0
while n <=10:
    x = int(input("Digite o %d numero: " %n))
    soma +=x
    n +=1
print("Soma: %d" %soma)"""

soma = 0
n = 0

while True:
    x = int(input("Digite o numero (0 sai): "))
    if x ==0:
        break
    else:
        n +=1
        soma +=x
print("Media: %5.2f" %(soma/n))