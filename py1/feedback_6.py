from random import randint

def FindValue(N):
    keys = []
    dictionary = {}

    for key in range(100):
        num = randint(1,10)
        if num in keys:
            dictionary[num] += 1
            keys.append(num)
            continue
        keys.append(num)
        dictionary[num] = 1

    dictionary = dict(filter(lambda item: item[1] == N, dictionary.items()))
    final = list(dictionary.keys())
    return final
