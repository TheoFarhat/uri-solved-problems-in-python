n = int(input())

str = "Feliz nat"
str_1 = "Feliz natal!"
str_2 = "al!"
if n != 1 and n != 0:
    nova = str_2.replace("a", "a"*n,)
    print(str + nova)
else:
    print(str_1)

