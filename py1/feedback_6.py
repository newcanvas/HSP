def FindValue(values, N):
    final = set()
    dictionary = {}
    for num in values:
        if dictionary.get(num, None):
            dictionary[num] += 1
        else:
            dictionary[num] = 1

        if dictionary[num] == N:
            final.add(num)
        if dictionary[num] > N:
            final.discard(num)

    return list(final)
