from itertools import *


def f():
    p = 0
    for i in product('ABCDXYZ', repeat = 4):
        s = ''.join(i)
        if s.count('X') == 1 and s.count('Y') == 1 and s.count('Z') == 1:
            s = s.replace('Y', 'X', 1).replace('Z', 'X', 1)
            if s[0] == 'X':
                p += 1
    print(p)

f()
