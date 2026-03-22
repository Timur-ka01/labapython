def f():
    k = open("17_25356.txt", "r")
    limit = 4
    for i in k:
        if len(i) > limit:
            i = i[:limit]

        words = i.split()
        result = "".join(map(lambda word: word[::-1], words))
        yield result


generator = f()
for i in generator:
    print(i)