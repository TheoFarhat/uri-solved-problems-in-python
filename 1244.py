n = int(input())

for _ in range(n):
    frase = list(map(str, input().split()))

    for j in range(len(frase)-1):
        for i in range(len(frase)-1):
            if len(frase[i]) < len(frase[i+1]):
                frase[i], frase[i+1] = frase[i+1], frase[i]
     
    for k in range(len(frase)):
        print(frase[k], end = '')
        if k != len(frase)-1:
            print(' ', end = '')
    print()