y = int(input())
cont = 0
nc = []
nr = []
ns = []
c = []
r = []
s = []

while cont < y:
    linha = input()
    n = linha.split()
    a = int(n[0])
    b = str(n[1])

    if b == "C":
        nc.append(a)
    
    elif b == "R":
        nr.append(a)
    
    elif b == "S":
        ns.append(a)

    cont = cont + 1

    
    

tc = sum(nc)
tr = sum(nr)
ts = sum(ns)
tt = tc + tr + ts
print(f"Total: {tt} cobaias")
print(f"Total de coelhos: {tc}")
print(f"Total de ratos: {tr}")
print(f"Total de sapos: {ts}")

pc = (tc * 100) / tt
pr = (tr * 100) / tt
ps = (ts * 100) / tt
print(f"Percentual de coelhos: {pc:.2f} %")
print(f"Percentual de ratos: {pr:.2f} %")
print(f"Percentual de sapos: {ps:.2f} %")