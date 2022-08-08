n = int(input())

while n != 0:
    lista = []
    for i in range(n):
      for j in range(n):   
        a = abs(j-i)
        if j == n-1:
          print(f"{a+1:>3}")
        else:
          print(f"{a+1:>3}",end= " ")

    print()    
        
    n = int(input())  