from math import ceil
palavra_nova = []

n = int(input())

for _ in range(n):
    palavra = str(input())
    palavra_1 = ''
   
    for c in (palavra):
        if c.isalpha():
            palavra_1 += chr(ord(c)+3)
        else:
            palavra_1 += c
    
    palavra_2 = palavra_1[::-1]

    s = ceil(len(palavra_2)/2) 
    palavra_3 = palavra_2[-s:]
    palinha = ''
    for k in(palavra_3):
        palinha += chr(ord(k) - 1)
    

    oi = palavra_2.replace(palavra_3, palinha)
    
    print(oi)