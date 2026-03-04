def tri(x):
    t = ''
    while x > 0:
        t += str(x%3)
        x //= 3
        t = t[::-1]
    return t
        
def f():
    x = 9 ** 8 + 3 ** 5 - 9
    s = tri(x)
    print(s.count('2'))


f()