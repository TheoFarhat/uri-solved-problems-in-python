n = int(input())
teste = 0

for _ in range(n):
    carta = list(map(int, input().split()))
    lista = sorted(carta)
    repeticoes = []
    lista_repetidos = []
    teste += 1
    x = (f"Teste {teste}")
    pontuacao = 0
    verificar = True
    for l in range(len(lista)-1):
        if lista[l+1] == lista[l] + 1:
            verificar = True

        else:
            verificar = False
            break

    if verificar == True:
        print(x)
        pontuacao = lista[0] + 200
        print(pontuacao)
        print()

    else:


        for i in lista:
            p = lista.count(i)
            if p >= 2 and i not in lista_repetidos:
                repeticoes.append(p)
                lista_repetidos.append(i)

        if len(repeticoes) == 0:
            print(x)
            print(0)
            print()


        else:


            for j, k in zip(range(len(repeticoes)),range(len(lista_repetidos))):
                if len(repeticoes) == 1:
                    if repeticoes[j] == 3:
                        pontuacao = lista_repetidos[k] + 140
                        print(x)
                        print(pontuacao)
                        print()
                    elif repeticoes[j] == 4:
                        pontuacao = lista_repetidos[k] + 180
                        print(x)
                        print(pontuacao)
                        print()
                    elif repeticoes[j] == 2:
                        pontuacao = lista_repetidos[k]
                        print(x)
                        print(pontuacao)
                        print()
                elif len(repeticoes) == 2:
                    if repeticoes[j] == 2 and repeticoes[j+1] == 3:
                        pontuacao = lista_repetidos[k+1] + 160
                        print(x)
                        print(pontuacao)
                        print()
                        break
                    elif repeticoes[j] == 3 and repeticoes[j+1] == 2:
                        pontuacao = lista_repetidos[k] + 160
                        print(x)
                        print(pontuacao)
                        print()
                        break
                    elif repeticoes[j] == 2 and repeticoes[j+1] == 2:
                        pontuacao = (3 * lista_repetidos[k+1]) + (2 * lista_repetidos[k]) + 20
                        print(x)
                        print(pontuacao)
                        print()
                        break




