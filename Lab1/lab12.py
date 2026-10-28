import os
import shutil
import tempfile

RUN_SIZE = 3


def check(a):
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


def write_run(f, run):
    f.write(" ".join(str(x) for x in run) + "\n")


def read_run(f):
    line = f.readline()
    if line == "":
        return None
    return [float(x) for x in line.split()]


def make_runs(a):
    runs = []
    for i in range(0, len(a), RUN_SIZE):
        part = a[i:i + RUN_SIZE]
        part.sort()
        runs.append(part)
    return runs


def fibonacci_distribution(n):
    x = 1
    y = 1
    while x + y < n:
        x, y = x + y, x
    return x, y


def merge_phase(fs, counts, target, s1, s2):
    m = min(counts[s1], counts[s2])
    for _ in range(m):
        run1 = read_run(fs[s1])
        run2 = read_run(fs[s2])
        write_run(fs[target], merge(run1, run2))
    counts[s1] = counts[s1] - m
    counts[s2] = counts[s2] - m
    counts[target] = counts[target] + m


def external_sort(a):
    runs = make_runs(a)
    if len(runs) == 1:
        return runs[0]

    x, y = fibonacci_distribution(len(runs))
    dummies = x + y - len(runs)
    for _ in range(dummies):
        runs.append([])

    folder = "."
    names = []
    for i in range(3):
        names.append(os.path.join(folder, "f" + str(i + 1) + ".txt"))

    fs = []
    try:
        with open(names[0], "w") as f:
            for run in runs[:x]:
                write_run(f, run)
        with open(names[1], "w") as f:
            for run in runs[x:]:
                write_run(f, run)

        fs = [open(names[0], "r"), open(names[1], "r"), open(names[2], "w")]
        counts = [x, y, 0]

        while sum(counts) > 1:
            target = counts.index(0)
            sources = []
            for i in range(3):
                if i != target:
                    sources.append(i)
            s1 = sources[0]
            s2 = sources[1]

            merge_phase(fs, counts, target, s1, s2)

            fs[target].close()
            fs[target] = open(names[target], "r")

            if counts[s1] == 0:
                empty = s1
            else:
                empty = s2
            fs[empty].close()
            fs[empty] = open(names[empty], "w")

        final = counts.index(1)
        result = []
        while True:
            run = read_run(fs[final])
            if run is None:
                break
            result = result + run
        return result
    finally:
        for f in fs:
            f.close()


try:
    a = [float(t) for t in input("Ввод: ").split()]
    if len(a) == 0:
        print("ничего не введено")
    elif check(a) == False:
        print("введены не числа")
    else:
        a = external_sort(a)
        print("Итог:", a)
except ValueError:
    print("не числа")