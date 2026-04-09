import math

a1 = 1.0
a2 = 1.0

def f(a1, b1, k):
    for i in range(1, k):
        anext = (math.sqrt(b1) + (math.sqrt(a1))* 0.5)*0.5
        bnext = 1.5 * math.sqrt(b1) + 0.5 * (a1) ** 2
        a1 = anext
        b1 = bnext
    return a1, b1

def p(a1, b1, k):
    if k == 1:
        return a1, b1
    anext = (math.sqrt(b1) + (math.sqrt(a1))* 0.5)*0.5
    bnext = 1.5 * math.sqrt(b1) + 0.5 * (a1) ** 2
    return p(anext, bnext, k - 1)



print(f"k{f(1.0, 1.0, 7)}")
print(f"k{p(1.0, 1.0, 7)}")