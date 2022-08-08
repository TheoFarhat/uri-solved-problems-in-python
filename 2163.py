l, c = map(int, input().split())

matriz = []
valores = []

for lin in range(l):
    valores = list(map(int, input().split()))
    matriz.append(valores)
    valores = []
cont = 0

for i in range(1, l - 1):
    for j in range(1, c - 1):
        if matriz[i][j] == 42:
            if matriz[i-1][j-1] == 7 and matriz[i-1][j] == 7 and matriz[i-1][j+1] == 7 and matriz[i][j-1] == 7 and matriz[i][j+1] == 7 and matriz[i+1][j-1] == 7 and matriz[i+1][j] == 7 and matriz[i+1][j+1] == 7:
                print(i+1,j+1)
                cont = 1
if cont == 0:
    print(0,0)


