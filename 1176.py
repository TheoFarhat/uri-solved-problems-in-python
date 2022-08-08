n = int(input())
cont = 0


while cont < n:
    lista =[0,1]
    cont += 1
    f = int(input())
    
    for i in range(f-1):
        x = lista[i] + lista[i+1]
        lista.append(x)

    if f == 0:  
        print(f"Fib({f}) = 0")
        
    else:
        print(f"Fib({f}) = {lista[-1]}")