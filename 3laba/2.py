import math

a1 = 1.0
a2 = 1.0

<<<<<<< HEAD
def f(a1, b1, k):
    for i in range(1, k):
=======
def f(a1, b1):
    k = 4
    print(f"a{1}: {a1}")
    print(f"b{1}: {b1}")
    for i in range(k):
>>>>>>> 971e8e6f93bc0ccc3d2798cd0f5b2c5f3ce67675
        anext = (math.sqrt(b1) + (math.sqrt(a1))* 0.5)*0.5
        bnext = 1.5 * math.sqrt(b1) + 0.5 * (a1) ** 2
        a1 = anext
        b1 = bnext
<<<<<<< HEAD
    return a1, b1
=======
>>>>>>> 971e8e6f93bc0ccc3d2798cd0f5b2c5f3ce67675

def p(a1, b1, k):
    if k == 1:
        return a1, b1
    anext = (math.sqrt(b1) + (math.sqrt(a1))* 0.5)*0.5
    bnext = 1.5 * math.sqrt(b1) + 0.5 * (a1) ** 2
    return p(anext, bnext, k - 1)



<<<<<<< HEAD
print(f"k{f(1.0, 1.0, 7)}")
print(f"k{p(1.0, 1.0, 7)}")
=======
print(f(1.0, 1.0))
print(p(1.0, 1.0, 1))
>>>>>>> 971e8e6f93bc0ccc3d2798cd0f5b2c5f3ce67675
