x1,y1,x2,y2 = map(int, input().split())

while x1 != 0 and y1 != 0 and x2 != 0 and y2 != 0:
    if x1 == x2 and y1 == y2:
        print(0)
    
    elif (x1 == x2 and y1 != y2) or (y1 == y2 and x1 != x2):
        print(1)
    
    elif abs(x2 - x1) == abs(y2-y1):
        print(1)
        
    else:
        print(2)
    
    x1,y1,x2,y2 = map(int, input().split())