#Рефлексия
'''
4.1.
Не до конца еще перестроилась с базового курса на то, что можно использовать методы, явно не упомянутые в теории. Поэтому хоть и прочитала про endswith(), сделала выбор в пользу split().
Зачем-то опять сделала b_flag == True, сейчас, перечитывая код, понимаю, что это бессмысленно. Еще нужно будет освоить extend.

4.2.
Не догадалась использовать в решении функцию из первого задания, но в целом логика схожа с эталонной.
'''

#Решение
from zipfile import ZipFile
import os

def MakeZip(name, ext):
    with ZipFile(name) as oldzip:
        mode = 'w'
        zip = oldzip.namelist()
        for i in zip:
            if i.endswith(ext):
                with ZipFile('test.zip') as oldzip:
                    oldzip.extract(i)
                with ZipFile('new.zip', mode) as newzip:  
                    mode = 'a'
                    newzip.write(i)
                    os.remove(i)


