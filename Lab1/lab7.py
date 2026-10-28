def check(a):
    if len(a) == 0:
        print("ничего не введено")
        return False
    for item in a:
        if type(item) not in [int, float]:
            return False
    return True

def sort_shell(a):
    if check(a) == False:
        print("введены не числа")
        return

    n = len(a)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            key = a[i]
            j = i - gap
            while j >= 0 and a[j] > key:
                a[j + gap] = a[j]
                j = j - gap
            a[j + gap] = key
        gap = gap // 2

try:
    a = [float(t) for t in input("Ввод: ").split()]
    sort_shell(a)
    print("Итог:", a)
except ValueError:
    print("не числа")
