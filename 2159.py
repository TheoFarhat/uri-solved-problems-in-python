from math import log

def formula(n):
    f = n / log(n)
    return f

n = float(input())

p = formula(n)
q = formula(n) * 1.25506

print(f"{p:.1f} {q:.1f}")