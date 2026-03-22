import math

a1 = 1.0
a2 = 1.0

def f(a1, b1):
    k = 5
    for i in range(k):
        anext = (math.sqrt(b1) + (math.sqrt(a1))* 0.5)*0.5
        bnext = 1.5 * math.sqrt(b1) + 0.5 * (a1) ** 2
        print(f"a{i + 2}: {anext}")
        print(f"b{i + 2}: {bnext}")
        a1 = anext
        b1 = anext

def p(a1, b1, i):
    print(f"a{i}: {a1}")
    print(f"b{i}: {b1}")
    if i > 4:
        return
    anext = (math.sqrt(b1) + (math.sqrt(a1))* 0.5)*0.5
    bnext = 1.5 * math.sqrt(b1) + 0.5 * (a1) ** 2
    p(anext, bnext, i + 1)



print(f(1.0, 1.0))
print(p(1.0, 1.0, 1))