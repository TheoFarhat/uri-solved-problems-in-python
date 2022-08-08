linha = input()
n = linha.split()
a = int(n[0])
b = int(n[1])
c = int(n[2])

if abs(b < a) and c >= b:
    print(":)")

elif abs(b > a) and c <= b:
    print(":(")

elif abs(b > a) and abs(b-a) > abs(c-b):
    print (":(")

elif abs(b > a) and abs(b-a) <= abs(c-b):
    print(":)")

elif abs(b < a) and abs(b-a) > abs(c-b):
    print(":)")

elif abs(b < a) and abs(b-a) <= abs(c-b):
    print(":(")

elif b == a and c > b:
    print(":)")

elif b == a and c < b:
    print(":(")

elif b == a and c == b:
    print(":(")
    	
