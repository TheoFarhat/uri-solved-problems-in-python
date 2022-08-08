l, c, m, n = map(int, input().split())
matriz = []
for lis in range(l):
    linha = list(map(int, input().split()))
    matriz.append(linha)


max_lote = 0 

for lin in range(m, l+1, m):
    for col in range(n,c + 1, n):
        lote_atual = 0
        for linlote in range(lin-m,lin):
            for collote in range(col-n,col):
                lote_atual += matriz[linlote][collote]

        if lote_atual >= max_lote:
            max_lote = lote_atual  

print(max_lote)

