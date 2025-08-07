from random import randint

def FindValue(N):
    final = []
    keys = []
    dictionary = {}

    for key in range(100):
        num = randint(1,10)
        if num in keys:
            dictionary[num] += 1
            keys.append(num)
            if dictionary[num] == N:
                final.append(num)
            if dictionary[num] > N:
                final.remove(num)
                dictionary[num] = -1000
            continue
        keys.append(num)
        dictionary[num] = 1
    return final
