n = float(input())
while n > 10 or n < 0:
    print("nota invalida")
    n = float(input())
    

n1 = float(input())
while n1 > 10 or n1 < 0:
    print("nota invalida")
    n1 = float(input())

media = (n + n1) / 2
print(f"media = {media:.2f}")