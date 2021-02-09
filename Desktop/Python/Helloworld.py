print("--------------------------")

print("Programa que determina quien aprueba")

def generaPares(limit):
    num=1
    #miLista=[]
    while num<limit:
        #miLista.append(num*2)
        yield num*2
        num=num+1
    #return miLista
print(generaPares(10))

print("--------------------------")
