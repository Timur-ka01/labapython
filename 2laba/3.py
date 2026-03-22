def f():
    result = []
    n = 452022
    
    while len(result) < 5:
        for d in range(2, int(n**0.5) + 1):
            if n % d == 0:
                M = d + n // d
                if M % 7 == 3:
                    result.append((n, M))
        n += 1
        
    return result


print(f())