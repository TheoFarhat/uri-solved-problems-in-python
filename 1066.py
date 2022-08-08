r = 0
cont = 0
n = 5
impar = []
par = []
positivo = []
negativo = []

while cont < 5:
    r = int(input())
    if r % 2 == 0 or r == 0:
        par.append(r)
        if r > 0:
            positivo.append(r)
        
        elif r < 0:
            negativo.append(r)
    if r % 2 != 0:
        impar.append(r)
        if r > 0:
            positivo.append(r)
        
        elif r < 0:
            negativo.append(r)
        
    
    cont += 1
    
print(f"{len(par)} valor(es) par(es)")
print(f"{len(impar)} valor(es) impar(es)")
print(f"{len(positivo)} valor(es) positivo(s)")
print(f"{len(negativo)} valor(es) negativo(s)")
