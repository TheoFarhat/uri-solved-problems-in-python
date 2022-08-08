n = int(input())

for _ in range(n):
    x = []
    frase = str(input())
    frase = frase.replace(" ","")
    frase = frase.replace(",","")

    for i in range(len(frase)):
        for k in range(97,123):
            if frase[i] == chr(k) and frase[i] not in x:
                x.append(frase[i])
   
    soma = len(x)
    
    

    if 13 <= soma < 26:
        print("frase quase completa")
    
    elif soma < 13:
        print("frase mal elaborada")

    elif soma == 26:
        print("frase completa")
