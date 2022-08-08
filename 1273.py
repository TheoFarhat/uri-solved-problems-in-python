n = int(input())
if n == 0:
    exit
else:
    while n != 0:
        maior = 0
        lista_nomes = []
        for _ in range(n):
            nome = str(input())
            lista_nomes.append(nome)
            if len(nome) > maior:
                maior = len(nome)

        for i in lista_nomes:
            espaco = maior - len(i)
            nova_palavra = ""

            for k in range(espaco):
                nova_palavra += " "

            nova_palavra += i

            print(nova_palavra.rstrip())

        n = int(input())
        if n != 0:
            print()