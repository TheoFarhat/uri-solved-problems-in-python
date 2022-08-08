def main():
    try:
        while True:
            n = int(input())
            lista = list(map(int, input().split()))
        
            velo = max(lista)

            if velo < 10:
                print(1)

            elif 10 < velo < 20:
                print(2)
            
            elif velo >= 20:
                print(3)

    except EOFError:
        pass

if __name__ == "__main__":
    main()