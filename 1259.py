n = int(input())
lista = []
pares = []
impares = []

for i in range(n):
    lista.append(int(input()))

for j in lista:
    if j % 2 == 0:
        pares.append(j)

for k in lista:
    if k % 2 != 0:
        impares.append(k)

pares.sort()
impares.sort(reverse = True)

for a in pares:
    print(a)

for b in impares:
    print(b)