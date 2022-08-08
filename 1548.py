r = int(input())
cont = 0

while cont < r:
    cont += 1
    n = int(input())
    lista = list(map(int, input().split()))
    valor = 0
    copia = lista.copy()
    lista.sort(reverse = True)
    
    
    
    for j in range(len(lista)):
            
        if copia[j] != lista[j]:
            valor += 1
                    
    print(len(lista) - valor)