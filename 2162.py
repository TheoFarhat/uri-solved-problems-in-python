n = int(input())

lista = list(map(int, input().split()))

verificador = 1

if n == 2 and lista[0] == lista[1]:
    
    verificador = 0

else:
    for i in range(1, n-1):
    
        if not(lista[i-1] > lista[i] < lista[i+1] or lista[i-1] < lista[i] > lista[i+1]):
            verificador = 0
    
print(verificador)        