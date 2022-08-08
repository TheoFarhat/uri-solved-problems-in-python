n = int(input())

if 0 <= n <= 9:
    print(n)

elif n == 10:
    print("A")

elif n == 11:
    print("B")

elif n == 12:
    print("C")

elif n == 13:
    print("D")

elif n == 14:
    print("E")

elif n == 15:
    print("F")

elif n == 16:
    print("10")    

if n > 16:

    lista = []
    while n >= 1:
        n1 = n // 16
        n2 = n % 16
        lista.append(n2)
        n = n // 16

    resposta = []
    
    for i in range(len(lista)):
        if 0 <= lista[i] <= 9:
            resposta.append(lista[i])

        elif lista[i] == 10:
            resposta.append("A")
            
        elif lista[i] == 11:
            resposta.append("B")

        elif lista[i] == 12:
            resposta.append("C")

        elif lista[i] == 13:
            resposta.append("D")

        elif lista[i] == 14:
            resposta.append("E")

        elif lista[i] == 15:
            resposta.append("F")

        elif lista[i] == 16:
            resposta.append("10")
    resposta.reverse()      
    for j in range(len(resposta)-1):
        print(resposta[j],end= "")
    print(resposta[-1])    