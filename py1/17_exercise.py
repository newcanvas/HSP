#7.1.
#1.
def check_decorator(func):
    def wrapper(*args):
        if args[1] == 0:
            raise ValueError("Делитель не может быть равен нулю.")
        result = func(*args)
        return result
    return wrapper

@check_decorator
def divide(a, d):
    return a / d

#2.
def print_type(func):
    def wrapper(*args):
        for i in range(len(args)):
            types = type(args[i])
            print(f"Введен аргумент {args[i]}, типа {types}")
        result = func(*args)
        return result
    return wrapper
    
@print_type
def anyt(a, b=None, c=None):
    return a, b, c

#7.2.
class Persona: # Боевая персона
   
    def __init__(self, persona_name, persona_arcana, persona_min_level, persona_current_level, persona_skills):
        self.__name = persona_name # Имя персоны
        self.__arcana = persona_arcana # Аркан
        self.__min_level = persona_min_level # Минимальный уровень протагониста для призыва персоны
        self.__current_level = persona_current_level # Текущий уровень персоны
        self.__skills = persona_skills  # Набор заклинаний
        self.__is_obtained = False # Есть ли данная персона в арсенале протагониста

    def NewSkill(self, new_skill):
        self.__skills.append(new_skill)

    def LevelUp(self, levels):
        self.__current_level += levels

    @property
    def current_level(self):
        return self.__current_level
        
    @property
    def min_level(self):
        return self.__min_level
        
    @property
    def skills(self):
        return self.__skills
    
    @property
    def is_obtained(self):
        return self.__is_obtained

    @is_obtained.setter
    def is_obtained(self):
        self.is_obtained = True

class SocialLink: # Сюжетное ответвление для установления отношений с персонажем
    
    def __init__(self, sl_name, sl_arcana, sl_current_level, sl_current_date, sl_deadline):
        self.__name = sl_name  # Имя персонажа
        self.__arcana = sl_arcana # Аркан
        self.__current_level = sl_current_level # Текущий уровень отношений
        self.__current_date = sl_current_date  # Текущая дата по игровому времени
        self.__deadline = sl_deadline  # Дедлайн прохождения сюжета по игровому времени
        self.__is_finished = False # Завершен ли сюжет

    def ProgressSL(self):
        self.__current_level += 1
    
    @property
    def current_date(self):
        return self.__current_date

    @property
    def deadline(self):
        return self.__deadline
        
    @property
    def current_level(self):
        return self.__current_level
    
    @property
    def is_finished(self):
        return self.__is_finished
    
    @is_finished.setter
    def is_finished(self):
        self.__is_finished = True


#7.3.
'''
Статический метод принадлежит самому классу, а не его объектам. Для его вызова не требуется создание экземпляра класса.
Метод класса также принадлежит классу, но требует создания экземпляра для вызова.
'''

#7.4.
from functools import wraps

def invariant(predicate):
    def invariant_decorator(method):
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            result = method(self, *args, **kwargs)
            assert predicate(self), f"Invariant condition failed {method.__name__}"
            return result
        return wrapper
    return invariant_decorator

class SocialLink: # Сюжетное ответвление для установления отношений с персонажем
    
    def __init__(self, sl_name, sl_arcana, sl_current_date, sl_deadline, sl_current_level=None):
        self.__name = sl_name  # Имя персонажа
        self.__arcana = sl_arcana # Аркан
        self.__current_level = sl_current_level # Текущий уровень отношений
        self.__current_date = sl_current_date  # Текущая дата по игровому времени
        self.__deadline = sl_deadline  # Дедлайн прохождения сюжета по игровому времени
        self.__is_finished = False # Завершен ли сюжет
        
    @property
    def current_level(self):
        return self.__current_level

    @current_level.setter
    def current_level(self, value):
        self.__current_level = value

    @invariant(lambda self: self.__current_level >= 0)
    def level_down(self):
       self.__current_level -= 1

Yukiko = SocialLink("Yukiko Amagi", "Priestess", "2011-4-07", "2011-4-06")
Yukiko.current_level = 0
print(Yukiko.current_level)
Yukiko.level_down()

#7.5.
import os
def ReturnNameList(dir_path, file_extention, b_flag):
    assert isinstance(dir_path, str), "Path must be str"  # 5.1. 
    assert file_extention != '', "Extention cannot be empty"  # 5.3.
    assert len(dir_path) > 0, "Path cannot be empty"  # 5.4.
    assert dir_path == '"."', "Invalid path"  # 5.5. При сценарии, что искать можно только в текущей папке
    assert file_extention in ('txt', 'md', 'py'), "Invalid extention" # 5.6. При сценарии с ограничением типов файлов
    assert b_flag, "Include subdirs"  # 5.7.
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
    assert final_list is not None, "Result should not be None"  # 5.2.
    return final_list
#7.6.
'''
'ad hoc' - изначально означает по запросу. Так и тут, мы определяем список приемлемых типов и функция выполняется "по запросу" того типа, который был передан.
У функции будет уникальный функционал, в зависимости от типа.
'''
