from math import sqrt as raiz


def distancia(x1, y1, x2, y2):
    d = raiz(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return d


x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
r = distancia(x1, y1, x2, y2)
print(f"{r:.4f}")

