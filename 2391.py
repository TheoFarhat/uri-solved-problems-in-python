n = int(input())
partes = 1
dif1 = []
j = 0
lista = list(map(int,input().split()))

for i in range(len(lista)-1):
  dif = (lista[i+1] - lista[i])
  dif1.append(dif)

while j < (len(dif1)-1):
  if dif1[j+1] != dif1[j]:
    partes += 1
    j += 2
  else:
    j += 1

print(partes)