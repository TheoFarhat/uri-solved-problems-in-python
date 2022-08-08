j, r = map(int, input().split())
rodadas = list(map(int, input().split()))
pontuacoes = [0] * j 

for i in range(0, j*r, j):
    for k in range(j):
        pontuacoes[k] += rodadas[k+i]

maior_pontuacao = max(pontuacoes)
vencedores = []

for l in range(j):
    if pontuacoes[l] == maior_pontuacao:
        vencedores.append(l+1)

print(max(vencedores))