n = int(input())

for _ in range(n):
    frase = str(input())
    lista = list(frase.split())
    caracter = []
    
    for i in lista:
        frase_str = str(i)
        caracter.append(frase_str[0])    
        
    for k in caracter:
        print(k, end= "")
    
    print()
    
    