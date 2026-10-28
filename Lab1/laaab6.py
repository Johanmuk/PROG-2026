while True:
    s = input("Ввод: ")

    try:
        a = [float(x) for x in s.replace(",", ".").split()]
    except ValueError:
        print("введены не числа")
        continue

    if len(a) == 0:
        print("пусто")
        continue

    n = len(a)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]

    print("Итог:", *a)