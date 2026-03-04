def naiti(x):
    p = 0
    limit = int(x ** 0.5)
    for i in range(1, limit + 1, 2):
        if x % i == 0:
            p += 1
            para = x // i
            if para != i and para % 2 != 0:
                p += 1
        if p > 5:
            return False
    if p == 5:
        return x
    else:
        return False   
def f():
    for i in range(40000, 50001):
        k = naiti(i)
        if k:
            print(k)

f()