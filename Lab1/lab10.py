def check(a):
    if len(a) == 0:
        print("ничего не введено")
        return False
    for item in a:
        if type(item) not in [int, float]:
            return False
    return True

def merge(a, b):
    result = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i = i + 1
        else:
            result.append(b[j])
            j = j + 1
    while i < len(a):
        result.append(a[i])
        i = i + 1
    while j < len(b):
        result.append(b[j])
        j = j + 1
    return result

def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)

def sort_merge(a):
    if check(a) == False:
        print("введены не числа")
        return a
    return merge_sort(a)

try:
    a = [float(t) for t in input("Ввод: ").split()]
    a = sort_merge(a)
    print("Итог:", a)
except ValueError:
    print("не числа")
