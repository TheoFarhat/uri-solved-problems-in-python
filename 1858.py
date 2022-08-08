n = int(input())

lista = list(map(int, input().split()))
lista1 = lista.copy()
lista1.sort()

x = lista.index(lista1[0])

print(x+1)