def tri(x):
    """
    >>> tri(0)
    ''
    >>> tri(5)
    '12'
    >>> tri(9)
    '100'
    """
    t = ''
    while x > 0:
        t += str(x % 3)
        x //= 3
        t = t[::-1]
    return t

def f():
    """
    >>> f()
    3
    """
    x = 9 ** 8 + 3 ** 5 - 9
    s = tri(x)
    print(s.count('2'))

if __name__ == "__main__":
    import doctest
    doctest.testmod()