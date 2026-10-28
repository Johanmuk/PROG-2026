b = "()[({}())]"

while True:
    a = input("Введите строку: ")

    correct = True
    pairs = {")": "(", "]": "[", "}": "{"}

    stack = [] 
    for i in a:
        if i in "({[":
            stack.append(i)
        if i in ")}]":
            if len(stack) == 0:
                correct = False
                break
            elif stack.pop() != pairs[i]:
                correct = False
                break

    if len(stack) > 0:
        correct = False
    if correct:
        print("Строка существует")
    else:
        print("Строка не существует")