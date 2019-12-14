from itertools import count

def generator():
    for el in count(1):
        result = el
        for _ in range(1, el):
            result *= _
        yield result

i = 0
for el in generator():
    if i == 15:
        break
    print(el)
    i += 1