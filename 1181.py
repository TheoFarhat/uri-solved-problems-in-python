n = int(input())

operacao = input()

if operacao == "S":
    soma  = []
    matriz = []
    valores = []

    for lin in range(12):
        for col in range(12):
            valores.append(float(input()))
        matriz.append(valores)
        valores = []
    for i in matriz[n]:
        soma.append(i)
    print(f"{sum(soma):.1f}")

elif operacao == "M":
    media = []
    matriz = []
    valores = []

    for lin in range(12):
        for col in range(12):
            valores.append(float(input()))
        matriz.append(valores)
        valores = []
    for i in matriz[n]:
        media.append(i)
    print(f"{sum(media)/12:.1f}")
