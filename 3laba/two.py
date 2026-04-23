import math

def f(a1, b1):
    k = 4
    print(f"a1: {a1}")
    print(f"b1: {b1}")
    for i in range(k):
        anext = (math.sqrt(b1) + (math.sqrt(a1)) * 0.5) * 0.5
        bnext = 1.5 * math.sqrt(b1) + 0.5 * (a1) ** 2
        print(f"a{i + 2}: {anext}")
        print(f"b{i + 2}: {bnext}")
        a1 = anext
        b1 = bnext
    return a1, b1

def p(a1, b1, i):
    print(f"a{i}: {a1}")
    print(f"b{i}: {b1}")
    if i > 4:
        return a1, b1
    anext = (math.sqrt(b1) + (math.sqrt(a1)) * 0.5) * 0.5
    bnext = 1.5 * math.sqrt(b1) + 0.5 * (a1) ** 2
    return p(anext, bnext, i + 1)

if __name__ == "__main__":
    print(f(1.0, 1.0))
    print(p(1.0, 1.0, 1))