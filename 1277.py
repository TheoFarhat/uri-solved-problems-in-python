n = int(input())

for _ in range(n):
    r = int(input())
    reprovados = [] 
    nomes = list(map(str, input().split()))
    freq = list(map(str, input().split()))

    for i, j in zip(freq,nomes):
        achar_m = i.count("M")
        presenca = i.count("P")
        if achar_m == 0:
          calculo = (presenca * 100) / len(i) 
        else:
            calculo = (presenca * 100) / (len(i)-achar_m)

    
        if calculo < 75:
            reprovados.append(j)

    msg = " ".join(reprovados)
    msg.rstrip()
    print(msg)
    