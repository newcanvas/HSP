#Рефлексия
'''
3.1.
Логика решения соответствует эталонной, только вынесла создание нового имени в отдельную переменную.

3.2.
Логика решения соответствует эталонной, за исключением разницы в использовании переменных.
'''

#Решение
#1.
from random import randint

keys = []
values = []
dictionary = {}
value = 'a'
for key in range(100):
    keys.append(key)
    values.append(value)
    value+='a'

for i in range(len(keys)):
    a = randint(0,99)
    dictionary[keys[i]] = values[a]

for i in range(len(dictionary)):
    x = dictionary.get(i)
    print(x)
    dictionary.pop(i)

#2.
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
        if dictionary.get(i) >= N:
            final.append(i)
    return final
