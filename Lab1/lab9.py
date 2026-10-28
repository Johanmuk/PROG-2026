def check(a):
    if len(a) == 0:
        print("ничего не введено")
        return False
    for item in a:
        if type(item) not in [int, float]:
            return False
    return True

def sift_down(a, start, end):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        if child + 1 <= end and a[child] < a[child + 1]:
            child = child + 1
        if a[root] < a[child]:
            a[root], a[child] = a[child], a[root]
            root = child
        else:
            return

def sort_heap(a):
    if check(a) == False:
        print("введены не числа")
        return

    n = len(a)
    for start in range((n - 2) // 2, -1, -1):
        sift_down(a, start, n - 1)

    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        sift_down(a, 0, end - 1)

try:
    a = [float(t) for t in input("Ввод: ").split()]
    sort_heap(a)
    print("Итог:", a)
except ValueError:
    print("не числа")
