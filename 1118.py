x = 1 
y = 1
nv = 1

while 0 <= x <= 10 and nv == 1:
    x = float(input())
    while x > 10 or x < 0:
        print("nota invalida")
        x = float(input())

    y = float(input())
    while y > 10 or y < 0:
        print("nota invalida")
        y = float(input())

    media = (x + y) / 2
    print(f"media = {media:.2f}")

    print("novo calculo (1-sim 2-nao)")

    nv = int(input())
    while nv != 1 and nv != 2: 
        print("novo calculo (1-sim 2-nao)")
        nv = int(input())

