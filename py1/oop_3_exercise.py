"""Рефлексия.

Очень интересная тема, я с этими конструкциями сталкивалась ежедневно на работе и только сейчас поняла по сущности, что это было.
В моей программе методы и конструктор составлены адекватно. В эталонном примере было полезно увидеть как атрибуты задаются через условия.

"""

# Решение:

# 5.1.
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

    def ObtainPersona(self):
        self.is_obtained = True
    
    def GetCurrentLevel(self):
        return self.__current_level
        
    def GetMinLevel(self):
        return self.__min_level
        
    def GetSkills(self):
        return self.__skills

Mara_persona = Persona("Mara", "Tower", 62, 63, ["Agidyne", "Blight"])

if Mara_persona.GetCurrentLevel() >= Mara_persona.GetMinLevel():
    Mara_persona.ObtainPersona()

if Mara_persona.is_obtained:
    Mara_persona.LevelUp(2)
    Mara_persona.NewSkill("Power Charge")
    
print(Mara_persona.GetSkills())

class SocialLink: # Сюжетное ответвление для установления отношений с персонажем
    
    def __init__(self, sl_name, sl_arcana, sl_current_level, sl_current_date, sl_deadline):
        self.__name = sl_name  # Имя персонажа
        self.__arcana = sl_arcana # Аркан
        self.__current_level = sl_current_level # Текущий уровень отношений
        self.__current_date = sl_current_date  # Текущая дата по игровому времени
        self.__deadline = sl_deadline  # Дедлайн прохождения сюжета по игровому времени
        self.__is_finished = False # Завершен ли сюжет

    def FinishSL(self):
        self.__is_finished = True

    def FailSL(self):
        self.__current_level = 0

    def ProgressSL(self):
        self.__current_level += 1
        
    def GetCurrentDate(self):
        return self.__current_date

    def GetDeadline(self):
        return self.__deadline
        
    def GetCurrentLevel(self):
        return self.__current_level

Yukiko = SocialLink("Yukiko Amagi", "Priestess", 4, "2011-4-07", "2011-4-06")

if Yukiko.GetCurrentDate() > Yukiko.GetDeadline():
    Yukiko.FailSL()
    print(f"Текущий уровень отношений: {Yukiko.GetCurrentLevel()}")
    print("Время на прохождение сюжета вышло.")
elif  Yukiko.GetCurrentLevel() == 10:
    Yukiko.FinishSL()
    print("Сюжет пройден.")
else: 
    Yukiko.ProgressSL()

# 5.2.
# Иерархия: продукт - обувь/шампунь.
    
class Product:
    
    def __init__(self, n, p, a):
        self.name = n
        self.price = p
        self.amount = a

    def discount(self, d):
        if d > self.price:
            return 'Скидка не может быть больше стоимости товара.'
        self.price -= d

class Shoes(Product):

    def __init__(self, s, c, n, p, a):
        super().__init__(n, p, a)
        self.size = s
        self.color = c
    
    def change_color(self, new_color):
        self.color = new_color

    def size_choice(self):
        return "Вы выбрали размер " + str(self.size)
    
class Shampoo(Product):

    def __init__(self, t, n, p, a):
        super().__init__(n, p, a)
        self.type = t # тип волос: 1-жирные, 2-нормальные, 3-окрашенные
        
    def final_price(self):
        if self.type == 1:
            self.price *= 0.1
        elif self.type == 2:
            self.price *= 0.2
        elif self.type == 3:
            self.price *= 0.3
        return self.price
    
    def make_name(self):
        if self.type == 1:
            self.name = "Шампунь для жирных волос"
        elif self.type == 2:
            self.name = "Шампунь для нормальных волос"
        elif self.type == 2:
            self.name = "Шампунь для окрашенных волос"
        return self.name
    
# Иерархия: прием пищи - завтрак/обед.

class Meal:

    def __init__(self, t, k):
        self.time = t
        self.kalories = k

class Breakfast(Meal):

    def __init__(self, ic, e, t, k):
        super().__init__(t, k)
        self.is_dessert = ic # был ли съеден десерт
        self.egg = e # способ приготовления яиц: 1-глазунья, 2-вареные, 3-омлет

    def calorie_count(self):
        if self.is_dessert:
            self.kalories += 300
        if self.egg == 1 or self.egg == 3:
            self.kalories += 150
        elif self.egg == 2:
            self.kalories += 100
        return self.kalories
    
    def is_sweet_tooth(self):
        if self.is_dessert:
            return "Сладкоежка."
        else:
            return "Следит за здоровьем."
    
class Dinner(Meal):

    def __init__(self, s, bl, t, k, p):
        super().__init__(t, k)
        self.is_business_lunch = bl # был ли сделан заказ из меню бизнес-ланча
        self.price = p 
        self.second = s # 1-макароны, 2-пюре
        self.kotlety = "У нас сейчас котлеты."
        
    def second_type(self):    
        if self.second == 1:
            self.kotlety += " С макарошками."
        elif self.second == 2:
            self.kotlety += " С пюрешкой."
        return self.kotlety
    
    def business_lunch(self, discount_perc):
        if self.time >= 12 and self.time <= 15 and self.is_business_lunch:
            self.price *= 1 - discount_perc
        return self.price


    

            








