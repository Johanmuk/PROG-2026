def check(a):
    if len(a) == 0:
        print("ничего не введено")
        return False
    for item in a:
        if type(item) != int:
            return False
    return True

def radix_pass(a):
    if len(a) == 0:
        return a

    maximum = max(a)
    exp = 1
    while maximum // exp > 0:
        buckets = []
        for i in range(10):
            buckets.append([])

        for x in a:
            digit = (x // exp) % 10
            buckets[digit].append(x)

        a = []
        for bucket in buckets:
            for x in bucket:
                a.append(x)

        exp = exp * 10

    return a

def sort_radix(a):
    if check(a) == False:
        print("нужны целые числа")
        return

    neg = []
    pos = []
    for x in a:
        if x < 0:
            neg.append(-x)
        else:
            pos.append(x)

    pos = radix_pass(pos)
    neg = radix_pass(neg)
    neg.reverse()

    result = []
    for x in neg:
        result.append(-x)
    result = result + pos
    a[:] = result

try:
    a = [int(t) for t in input("Ввод: ").split()]
    sort_radix(a)
    print("Итог:", a)
except ValueError:
    print("нужны целые числа")
