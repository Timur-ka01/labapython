def f():
    k = open("17_25356.txt", "r")
    limit = 4
    for i in k:
        if len(i) > limit:
            i = i[:limit]

       
        yield i


generator = f()

def p(word):
    return word[::-1]

for i in generator:
    words = i.split()
    result = "".join(map(p, words))
    print(i)
