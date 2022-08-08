linha = input()
n = linha.split()
a = int(n[0])
b = int(n[1])


if b % a == 0 or a % b == 0:
    print("Sao Multiplos")
    if b == 0 or a == 0:
        print("Sao Multiplos")
    if b == 1 or a == 1:
        print("Sao Multiplos")
    if b == -1 or a == -1:
        print("Sao Multiplos")

else:
    print("Nao sao Multiplos")