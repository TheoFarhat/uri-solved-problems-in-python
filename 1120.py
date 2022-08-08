line = input().split()

while line[0] != "0" and line[1] != "0":
    x = line[1].replace(line[0],"")
    if x == "":
        print(0)
    else:  
        print(int(x))

    line = input().split()


