def p(l):
    result = 0
    l1 = [l]
    while l1:
        pos = l1.pop()

        for i in pos:
            if isinstance(i, list):
                l1.append(i)
            else:
                result += i
    return result


def f(l):
    result = 0
    for i in l:
        if isinstance(i, list):
            result += f(i)
        else:
            result += i
    return result




print(f([1, [2, [3, 4, [5]]]]))
print(p([1, [2, [3, 4, [5]]]]))


