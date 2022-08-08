lista = []

for i in range(100):
    n = int(input())
    lista.append(n)

lista1 = sorted(lista)
indice = len(lista1) - 1
ultimo = lista1[indice]
print(ultimo)

for j in range (len(lista)):
    if lista[j] == ultimo:
        print((lista.index(lista[j]))+1)