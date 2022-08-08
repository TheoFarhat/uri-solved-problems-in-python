lista = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
n = int(input())
cont = 0
while cont < n:
    cont += 1
    _ = str(input())
    letras = list(_)
    k = int(input())
    var = 26 - k 
    for i in range(len(letras)):
        letra = letras[i]
        t = lista.index(letra)+var
        if t > 25:
             letras[i] = lista[abs(t-26)]
        else:
            letras[i] = lista[t]
           
    for k in letras:
        print(k,end= "")
    print()