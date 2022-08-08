n = int(input())
lista = []
repetidos = []
lista2 = []

while len(lista) < n:
    valor = int(input())
    lista.append(valor)
    lista.sort()
    
for k in lista:
    if k not in lista2:
        repetidos.append(lista.count(k))
        lista2.append(k)


for j, h in zip(lista2,repetidos):

    print(f"{j} aparece {h} vez(es)")
    


    