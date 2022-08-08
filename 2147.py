n = int(input())

for i in range(n):
    gal = str(input())

    r = gal.count("e")
    soma = r / 100

    if r == 1:
        print(f"{0.09}")
    
    else:
        print(f"{0.08+soma:.2f}")