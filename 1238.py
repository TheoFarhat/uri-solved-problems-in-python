n = int(input())

for _ in range(n):
    a, b = map(str, input().split())
    x = ""
    nov_str = ""
    if len(a) >= len(b):
        for i, j in zip(range(len(a)),range(len(b))):
            x += a[i]+b[j]
        
        for k in range(len(a)):
            if k > (len(b)-1):
                nov_str += a[k]
        print(f"{x+nov_str}")

    

    elif len(a) < len(b):
        for i, j in zip(range(len(a)),range(len(b))):
            x += a[i]+b[j]
        
        for k in range(len(b)):
            if k > (len(a)-1):
                nov_str += b[k]
        print(f"{x+nov_str}")

    

