linha = input()
n = linha.split()
a = int(n[0])
b = int(n[1])
c = int(n[2])
d = int(n[3])


if a <= 24 and b <= 60 and c <= 24 and d <= 60:
    if c > a and d >= b:
        h = c - a
        m = d - b 
        if h <= 24 and m < 60:
            print(f"O JOGO DUROU {h:.0f} HORA(S) E {m:.0f} MINUTO(S)")       
    elif c > a and d < b:
        h = (c - a) - 1
        m = 60  + (d - b)  
        if h <= 24 and m < 60:
            print(f"O JOGO DUROU {h:.0f} HORA(S) E {m:.0f} MINUTO(S)")   
        
    elif c < a and d > b:
        h = (24 - a) + c
        m = d - b 
        if h <= 24 and m < 60:
            print(f"O JOGO DUROU {h:.0f} HORA(S) E {m:.0f} MINUTO(S)")   
            
    elif c <= a and d < b:
        h = ((24 - a) + c) - 1
        m = 60  + (d - b)  
        if h <= 24 and m < 60:
            print(f"O JOGO DUROU {h:.0f} HORA(S) E {m:.0f} MINUTO(S)")   

    elif c == a and d > b:
        h = c - a
        m = d - b
        if h <= 24 and m < 60:
            print(f"O JOGO DUROU {h:.0f} HORA(S) E {m:.0f} MINUTO(S)")   
    
    
    elif c == a and d == b:
            print(f"O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
            
