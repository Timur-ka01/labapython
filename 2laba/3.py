def f():
    """
    >>> f()  # doctest: +NORMALIZE_WHITESPACE
    [(452025, 150678), (452028, 113011), (452029, 23810), (452034, 226019), (452036, 17412)]
    """
    result = []
    n = 452022
    
    while len(result) < 5:
        for d in range(2, int(n**0.5) + 1):
            if n % d == 0:
                M = d + n // d
                if M % 7 == 3:
                    result.append((n, M))
                    break  # добавить break
        n += 1
        
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()