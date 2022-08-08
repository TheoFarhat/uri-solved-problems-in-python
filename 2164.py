from math import sqrt as raiz

def fibo(d):
    fiba = ((((1+raiz(5))/2)**d) - (((1-raiz(5))/2))**d) / raiz(5)
    return fiba

d = float(input())

r = fibo(d)

print(f"{r:.1f}")