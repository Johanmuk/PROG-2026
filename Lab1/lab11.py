def check(a):
    if len(a) == 0:
        print("ничего не введено")
        return False
    for item in a:
        if type(item) not in [int, float]:
            return False
    return True

def quick_sort(a, left, right):
    if left >= right:
        return

    pivot = a[(left + right) // 2]
    i = left
    j = right

    while i <= j:
        while a[i] < pivot:
            i = i + 1
        while a[j] > pivot:
            j = j - 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i = i + 1
            j = j - 1

    quick_sort(a, left, j)
    quick_sort(a, i, right)

def sort_quick(a):
    if check(a) == False:
        print("введены не числа")
        return
    quick_sort(a, 0, len(a) - 1)

try:
    a = [float(t) for t in input("Ввод: ").split()]
    sort_quick(a)
    print("Итог:", a)
except ValueError:
    print("не числа")
