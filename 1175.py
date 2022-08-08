cont = 0
lista = []
while cont < 20:
    cont += 1
    n = int(input())
    lista.append(n)



for i in range((len(lista))//2):
    
    lista[i], lista[19-i] = lista[19-i], lista[i]
   
        
for j in range(20):
    print(f"N[{j}] = {lista[j]}")