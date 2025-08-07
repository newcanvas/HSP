from random import randint

def FindValue(N):
    final = []
    keys = []
    dictionary = {}
    
    for key in range(100):
        keys.append(randint(1,10))
        dictionary[keys[key]] = 0
    
    for i in keys:
        dictionary[i]+=1 

    for i in dictionary:
        if dictionary.get(i) == N:
            final.append(i)
    return final
