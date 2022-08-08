c, p, q= map(int, input().split())

papel = c * q

if papel <= p:
    print("S")
else:
    print("N")