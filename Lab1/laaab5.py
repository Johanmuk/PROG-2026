def check(a):
    if len(a) == 0:
        print("ничего не введено")
        return False
    for item in a:
        if type(item) not in [int, float]:
            return False
    return True

def sort_insertion(a):
    if check(a) == False:
        print("введены не числа")
        return

    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = key

try:
    a = [float(t) for t in input("Ввод: ").split()]
    sort_insertion(a)
    print("Итог:", a)
except ValueError:
    print("некорректный ввод")
