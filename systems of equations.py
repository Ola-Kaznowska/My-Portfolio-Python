a1 = 3
a2 = 5
b1 = -1
b2 = 1
c1 = 3
c2 = 1
w = a1*b2-a2*b1
wx = c1*b2-c2*b1
wy = a1*c2-a2*c1
if w==0 and wx==0 and wy==0:
    print("Nieskonczenie wiele rozwiazan")
else:
    if w==0 and (wx != 0 or wy != 0 ):
        print("Brak rozwiazań")
    else:
        x = wx / w
        y = wy / w
        print(f'x = {x} y = {y}')