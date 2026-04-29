def read_and_truncate_lines(filename, limit=4):
    with open(filename, "r") as k:
        for i in k:
            i = i.rstrip('\n')  # убираем символ новой строки
            if len(i) > limit:
                i = i[:limit]
            yield i


def reverse_word(word):
    return word[::-1]


def process_generator(generator):
    for line in generator:
        words = line.split()
        result = "".join(map(reverse_word, words))
        yield result
