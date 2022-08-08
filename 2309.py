r = int(input())
cont = 0
truco = [4, 5, 6, 7, 12, 11, 13, 1, 2, 3]
vr = 0
vr1 = 0
while cont < r:
    adalberto = []
    bernardete = []
    cont += 1
    a1,a2,a3,b1,b2,b3 = map(int, input().split())
    lista = [a1,a2,a3]
    lista2 = [b1,b2,b3]
    for i in lista:
        r1 = truco.index(i)
        adalberto.append(r1)
    for j in lista2:
        r_1 = truco.index(j)
        bernardete.append(r_1)
    for k in range(3):
        if adalberto[k] > bernardete[k]:
            adalberto.append(1)
        elif adalberto[k] < bernardete[k]:
            bernardete.append(1)
        elif adalberto[k] == bernardete[k]:
            adalberto.append(1)
    
    va = len(adalberto)
    vb = len(bernardete)

    if va > vb:
        vr += 1
    if va < vb:
        vr1 += 1
print(vr, vr1)
