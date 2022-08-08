_ = int(input())
cont = 0

while cont < _:
    cont += 1
    frase = list(str(input().lower()))
    num = {}
    for i in frase:
        if i.isalpha() and i not in num:
            num[i] = frase.count(i)
        
    num_ordenados = sorted(num.items(), key=lambda x: (-x[1],x[0]))
    maior = num_ordenados[0][1]
    resultado = ""
    for c in num_ordenados:
        if c[1] == maior:
            resultado += c[0]
        
        
    print(resultado)


