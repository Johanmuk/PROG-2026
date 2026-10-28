def check(x_str):
    if len(x_str) == 0:
        print("ничего не введено")
        return False
    if not x_str.isdigit():
        print("нужно ввести целое положительное число")
        return False
    return True
a = input("Введите x: ").strip()

if check(a):
    x = int(a)
    result = []
    p3 = 1
    while p3 <= x:
        p5 = p3
        while p5 <= x:
            p7 = p5
            while p7 <= x:
                result.append(p7)
                p7 *= 7
            p5 *= 5
        p3 *= 3
    result.sort()
    print(*result)
