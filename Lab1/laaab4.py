def check(a):
    if len(a) == 0:
        print("ничего не введено")
        return False
    for item in a:
        if type(item) not in [int, float]:
            return False
    return True

def sort1(a):
    if check(a) == False:
        print("введены не числа")
        return

    n = len(a)
    swaped = 0
    gap = n
    while gap > 1 or swaped:
        swaped = 0
        gap = int(gap / 1.247)
        if gap < 1:
            gap = 1
        for i in range(n - gap):
            if a[i] > a[i+gap]:
                a[i], a[i+gap] = a[i+gap], a[i]
                swaped = 1

try:
    a = [float(t) for t in input("Ввод: ").split()]
    sort1(a)
    print("итог: ", a)
except ValueError:
    print("не числа")
