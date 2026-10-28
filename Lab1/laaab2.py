def parse(s):
    tokens = []
    i = 0
    expect_operand = True

    while i < len(s):
        ch = s[i]
        if ch == " ":
            i += 1
            continue

        if expect_operand:
            sign = 1
            if ch == "-":
                sign = -1
                i += 1
                if i >= len(s):
                    raise ValueError("После минуса ничего нет")
                ch = s[i]

            if ch == "(" and sign == 1:
                tokens.append("(")
                i += 1
            elif ch.isdigit():
                j = i
                while j < len(s) and (s[j].isdigit() or s[j] == "."):
                    j += 1
                try:
                    value = float(s[i:j])
                except ValueError:
                    raise ValueError("Неверная запись числа: " + s[i:j])
                tokens.append(sign * value)
                i = j
                expect_operand = False
            elif ch == "(":
                raise ValueError("Минус перед скобкой не поддерживается, пишите (0-...)")
            else:
                raise ValueError("Здесь должно быть число или '(', а найдено '" + ch + "'")
        else:
            if ch in "+-*/":
                tokens.append(ch)
                i += 1
                expect_operand = True
            elif ch == ")":
                tokens.append(")")
                i += 1
            else:
                raise ValueError("Здесь должна быть операция или ')', а найдено '" + ch + "'")

    if expect_operand:
        raise ValueError("Выражение закончилось раньше времени")
    return tokens


def apply(nums, ops):
    op = ops.pop()
    b = nums.pop()
    a = nums.pop()
    if op == "+":
        nums.append(a + b)
    elif op == "-":
        nums.append(a - b)
    elif op == "*":
        nums.append(a * b)
    elif op == "/":
        if b == 0:
            raise ValueError("Деление на ноль")
        nums.append(a / b)


def calculate(tokens):
    prior = {"+": 1, "-": 1, "*": 2, "/": 2}
    nums = []
    ops = []

    for t in tokens:
        if isinstance(t, float):
            nums.append(t)
        elif t == "(":
            ops.append(t)
        elif t == ")":
            while len(ops) > 0 and ops[-1] != "(":
                apply(nums, ops)
            if len(ops) == 0:
                raise ValueError("Лишняя закрывающая скобка")
            ops.pop()
        else:
            while len(ops) > 0 and ops[-1] != "(" and prior[ops[-1]] >= prior[t]:
                apply(nums, ops)
            ops.append(t)

    while len(ops) > 0:
        if ops[-1] == "(":
            raise ValueError("Есть незакрытая скобка")
        apply(nums, ops)

    return nums[0]


while True:
    s = input("Введите выражение  ").strip()
    if s == "выход":
        break
    try:
        if not s.endswith("="):
            raise ValueError("Выражение должно заканчиваться знаком '='")
        tokens = parse(s[:-1])
        result = round(calculate(tokens), 10)
        if result == int(result):
            result = int(result)
        print("Результат:", result)
    except ValueError as e:
        print("Ошибка:", e)