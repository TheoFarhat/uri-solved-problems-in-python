code = [1,2,3,4,5]
preco = [4.00,4.50,5.00,2.00,1.50]

linha = list(map(int, input().split()))
escolha = linha[0]
quantos = linha[1]

if escolha == code[0]:
    pagar = preco[0] * quantos
    print(f"Total: R$ {pagar:.2f}")
if escolha == code[1]:
    pagar = preco[1] * quantos
    print(f"Total: R$ {pagar:.2f}")
if escolha == code[2]:
    pagar = preco[2] * quantos
    print(f"Total: R$ {pagar:.2f}")
if escolha == code[3]:
    pagar = preco[3] * quantos
    print(f"Total: R$ {pagar:.2f}")
if escolha == code[4]:
    pagar = preco[4] * quantos
    print(f"Total: R$ {pagar:.2f}")
