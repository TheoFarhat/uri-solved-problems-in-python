x0, y0, x1, y1 = map(int, input().split())
x2, y2, x3, y3 = map(int, input().split())

if x0 <= x2 <= x1 or x2 <= x1 <= x3 or x1 <= x3 <= x2 or x2 <= x0 <= x3:
    if y0 <= y2 <= y1 or y2 <= y1 <= y3 or y1 <= y3 <= y2 or y2 <= y0 <= y3:

        print("1")
else:
    print("0")





