n = int(input())

matriz = []

for lin in range(n+1):
    matriz.append(list(map(int, input().split())))

a = 0
for i in range(n):
    for j in range(n):
        if matriz[i][j] == 1:
            a += 1 
        if matriz[i][j+1] == 1:
            a += 1 
        if matriz[i+1][j] == 1:
            a += 1 
        if matriz[i+1][j+1] == 1:
            a += 1

       
        if a >= 2:
            print(f"S", end="")
        else:
            print(f"U", end="")
        
        a = 0
    print()