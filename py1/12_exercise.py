#Рефлексия
'''
3.1.
Не догадалась применить конструкцию with open() as, из-за чего код цикла создания файлов раздулся.
Логика наполнения аналогична эталонной.

3.2.
Вообще неправильно подошла к решению задачи, потому что упустила необходимость включить путь в функцию.
И пока что далеко не сразу в голову приходит вариант написать функцию для использования в функции.
Нужно больше в этом практиковаться. Эталонное решение хоть и не сразу, но разобрала и поняла.

3.3.
Тут тоже не использовала конструкцию with open() as, видимо, не до конца ее поняла, нужно перечитать теорию.
Можно было избавиться от переменной, как в эталонном решении. Также обработала вероятно некорректные значения через assert вместо except.
'''
#Решение задач
#4.1.
import os
def ReturnNameList(dir_path, file_extention, b_flag):
    files_list = []
    dirs_list = []
    final_list = []

    x = os.listdir(dir_path)
    for i in x:
        if i.split(sep='.')[-1] == file_extention:
            files_list.append(i)
        if i.split(sep='.')[-1] == i:
            dirs_list.append(i)
        orig_dirs_list = dirs_list
    if b_flag == True:
        orig_dirs_list = dirs_list.copy()
        for dir in orig_dirs_list:
            new_dir_path = dir_path + '/' + dir
            x = os.listdir(new_dir_path)
            for i in x:
                if i.split(sep='.')[-1] == file_extention:
                    files_list.append(i)
                if i.split(sep='.')[-1] == i:
                    dirs_list.append(i)
    final_list.append(files_list)
    final_list.append(dirs_list)
    return final_list

#4.2.
import os

def DeleteDir(path):
    for root, dirs, files in os.walk(path):
        if dirs != []:
            return False
        else:
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
    os.rmdir(path)
    return True

#4.3.
#Изучила статью, из нее же взяла listdir() для первого задания.

