t1 = "00h00"
t2 = "00h10"
t3 = "00h30"
t4 = "01h00"
t5 = "01h10"


soma1 = 0
soma2 = 0
soma3 = 0
soma4 = 0
soma5 = 0

l = [[1, "jose","00h00"],
     [2, "maria","00h10"],
     [3, "ivan","00h30"],
     [4, "deny","00h00"],
     [5, "vitor","01h00"],
     [6, "emanuel","00h10"],
     [7, "diogo","01h00"],
     [8, "railson","00h00"],
     [9, "ruan","01h00"],
     [10, "marcio","01h10"],
     [11, "ana","00h00"],
     [12, "mane","01h10"]]


for x in l:
    if(x[2] == t1):
        soma1 = soma1 + 1    
        
    elif(x[2]== t2):
        soma2 +=1
        
    
    elif(x[2] ==t3):
        soma3 +=1
        
    
    elif(x[2] ==t4):
        soma4 +=1
        
    
    elif(x[2] ==t5):
        soma5 +=1
        
    
    else:
        print("horario invalido")

print(t1,"---",soma1,"\n",
      t2,"---",soma2,"\n",
      t3,"---",soma3,"\n",
      t4,"---",soma4,"\n",
      t5,"---",soma5)





