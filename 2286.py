r = int(input())
v = 0
while r != 0:
    v = v + 1
    print(f"Teste {v}")
    nome1 = input()
    nome2 = input()
    jogadas = 0
    while jogadas < r:
        linha = input()
        n = linha.split()
        a = int(n[0])
        b = int(n[1])
        ponto = a + b
        if ponto % 2 == 0:
            print(nome1)
        else:
            print(nome2)
        jogadas += 1


    r = int(input())
    print("")

