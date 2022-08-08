a = 1
b = 1
ng = 1
inter = []
gremio = []
empate = []
cont = 0
while ng == 1:
    cont += 1
    a, b = map(int, input().split())
    if a > b:
        inter.append(a)
    elif b > a:
        gremio.append(b)

    elif b == a:
        empate.append(b)    
    print("Novo grenal (1-sim 2-nao)")
    ng = int(input())
    
print(f"{cont} grenais")
print(f"Inter:{len(inter)}")
print(f"Gremio:{len(gremio)}")
print(f"Empates:{len(empate)}")

if len(inter) > len(gremio):
    print("Inter venceu mais")

elif len(inter) < len(gremio):
    print("Gremio venceu mais")

elif len(inter) == len(gremio):
    print("Não houve vencedor")

