n = int(input())

for _ in range(n):
    dieta = str(input())
    cafe = str(input())
    almoco = str(input())
    letras_faltando = ""
    x = 0
    cafe_almoco = cafe + almoco


    for k in range(len(cafe_almoco)):
        if cafe_almoco[k] not in dieta:
            x += 1

    if x >= 1:
        print("CHEATER")

    else:
        for i in range(len(dieta)):
            if dieta[i] not in cafe_almoco:
                letras_faltando += dieta[i]
            
        letras_faltando = "".join(sorted(letras_faltando))

        print(letras_faltando)
