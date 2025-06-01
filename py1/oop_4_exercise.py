"""
Рефлексия.

Разделила условия прошлого задания на две части, надеюсь, так можно было. Иерархии составлены адекватно.
Пока что не до конца понятно, в каких случаях стоит использовать _, а в каких __ для атрибутов. Насколько понимаю, такие вопросы решаются исходя из конкретных ситуаций в проекте.

"""

#4.1.
class Shoes:

    def __init__(self, s, c):
        self.size = s
        self.color = c

    def choice(self):
        return "Вы выбрали размер " + str(self.size)
    
class Shampoo:

    def __init__(self, n, t):
        self.name = n
        self.type = t # тип волос: 1-жирные, 2-нормальные, 3-окрашенные
    
    def make_name(self):
        if self.type == 1:
            self.name = "шампунь для жирных волос"
        elif self.type == 2:
            self.name = "шампунь для нормальных волос"
        elif self.type == 3:
            self.name = "шампунь для окрашенных волос"
        return self.name
    
    def choice(self):
        return "Вы выбрали " + self.name

class Product:
    
    def __init__(self, sho: list[Shoes], sha: list[Shampoo]):
        self.shoes = sho
        self.shampoo = sha

shoes = [Shoes(43, "Черный"), Shoes(36, "Красный")]
shampoo = [Shampoo("шампунь", 2), Shampoo("шампунь", 1)]
product = Product(shoes, shampoo)
print(product.shampoo[1].choice())
print(product.shoes[1].choice())

class Breakfast:

    def __init__(self, ic, e):
        self.is_dessert = ic # был ли съеден десерт
        self.egg = e # способ приготовления яиц: 1-глазунья, 2-вареные, 3-омлет
        self.kalories = 500

    def calorie_count(self):
        if self.is_dessert:
            self.kalories += 300
        if self.egg == 1 or self.egg == 3:
            self.kalories += 150
        elif self.egg == 2:
            self.kalories += 100
        return self.kalories
    
class Dinner:

    def __init__(self, s):
        self.second = s # 1-макароны, 2-пюре
        self.kalories = 500
        
    def calorie_count(self):
        if self.second == 1:
            self.kalories *= 2
        elif self.second == 2:
            self.kalories *= 2.5
        return self.kalories

class Meal:

    def __init__(self, breakfast: list[Breakfast], dinner: list[Dinner]):
        self.breakfast = breakfast
        self.dinner = dinner 

breakfast = [Breakfast(True, 1), Breakfast(False, 2)]
dinner = [Dinner(1), Dinner(2)]
meal = Meal(breakfast, dinner)
print(meal.breakfast[0].calorie_count())
print(meal.dinner[0].calorie_count())

#4.2.
"""
Полиморфизм первого типа подразумевает, что функция с одним и тем же названием будет переопределена: переделана под запросы определенного класса.
Когда эта функция будет вызываться по своему одному и тому же названию, будут происходить разные операции, в зависимости от класса.
Второй тип полиморфизма подразумевает, что с разными классами произойдет одна и та же операция. Необходимо учесть, чтобы операция была действительно универсальной и не вызвала конфликт.

"""

#4.3.
import random

class Animal:
    def foo(self):
        pass

class Cat(Animal):
    def foo(self):
        print("Кошка мурлычет")

class Bird(Animal):
    def foo(self):
        print("Птица поет")

def random_animal(ams: list[Animal]):
    ams = []
    for i in range(500):
        coin_toss = random.randint(1,2)
        if coin_toss == 1:
            animal = Cat()
            ams.append(animal)
        else:
            animal = Bird()
            ams.append(animal)
    return ams
    
barsik = Cat()
galka = Bird()
ams = [barsik, galka]
x = random_animal(ams)

for i in range(len(x)):
    print(x[i].foo())

#В выводе мы получаем строку с сообщением из метода foo, соответствующей классу, и None, так как в foo отсутствует return.

