x = 1
y = 1
lista = []
while x > 0 and y > 0:
    x,y = map(int, input().split())
    if x > 0 and y > 0:    
        m = max(x, y)
        n = min(x, y)
        c = 0
        for i in range(n, m+1):
            lista.append(i)
            c += i
            print(i,end= " ") 
        print(f"Sum={c}")

