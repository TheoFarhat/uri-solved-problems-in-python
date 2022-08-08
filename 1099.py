r = int(input())
cont = 0

while cont < r:
    cont += 1
    x, y = map(int, input().split())
    a = min(x,y)
    b = max(x,y)
    c = 0
    for i in range(a+1,b):
        if i % 2 != 0:
            c += i
    print(c)