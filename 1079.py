n = int(input())
cont = 0

while cont < n:
    a,b,c  = map(float, input().split())
    
    average = (2*a + 3*b +5*c) / 10
    print(f"{average:.1f}")
    cont += 1
    