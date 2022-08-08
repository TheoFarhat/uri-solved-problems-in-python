n = int(input())

fibs = [0,1]

while len(fibs) < n:
    fibs.append(fibs[-1] + fibs[-2])

for i in range(n):
    if i == n - 1:
        print(fibs[i],end= "\n")
    else:
        print(fibs[i],end= " ")


