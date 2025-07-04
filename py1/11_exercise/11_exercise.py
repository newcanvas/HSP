#Рефлексия
#Изучила assertListEqual и pytest. Также внимательно изучила код тестов, мои хоть и рабочие, но гораздо менее изобрательные.

#3.1.
from random import randint
name_file = 1
for i in range(10):
    fo = open(str(name_file)+'.txt', 'wt')
    name_file += 1
    for i in range(3):
        rand_int = randint(1, 100)
        fo.write(str(rand_int)+"\n") 
    fo.close()

#3.2.
from random import randint
def OpenAndSum(n1,n2):
    try:  
        summ = 0
        fi1 = open(str(n1)+'.txt', 'rt')
        fi2 = open(str(n2)+'.txt', 'rt')
        for s in fi1:
            summ+=int(s)
        for s in fi2:
            summ+=int(s)
    except ValueError:
        print(f"Внутри файлов что-то кроме чисел")
    except Exception:
        print(f"Один из файлов поврежден, нужно разбираться")
    finally:
        fi1.close()
        fi2.close()
    return n1, n2, summ

n1 = randint(1,10)
n2 = randint(1,10)
while n1 == n2:
   n2 = randint(1,10)
print(OpenAndSum(n1,n2))

#3.3.
class Cat:

    def __init__(self, cat_name, cat_weight, cat_fq):
        self.name = cat_name
        self.weight = cat_weight
        self.fq = cat_fq

fi = open('barsik.txt', 'rt')
cats = []
for s in fi:
    str_split = s.split(sep=None)
    my_cat = Cat(str_split[0], str_split[1], str_split[2])
    assert float(str_split[1]) < 21.0
    assert int(str_split[2]) > 40 and int(str_split[2]) < 200
    cats.append(my_cat)
fi.close()
