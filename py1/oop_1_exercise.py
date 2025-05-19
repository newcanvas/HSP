# 1.1.
# Программа для отслеживания сна малыша. Класс: сон. Атрибуты: время начала, время конца, длительность, тип (дневной/ночной), место, поза.
# Приложение для ВПН. Класс: подключение. Атрибуты: страна, протокол шифрования, лимит трафика.

# 1.2.
# В jrpg Persona 4 могли быть использованы следующие классы:
class Persona: # Боевая персона
    name = "Mara" # Имя персоны
    arcana = "Tower" # Аркан
    min_level = 62 # Минимальный уровень протагониста для призыва персоны
    current_level = 63 # Текущий уровень персоны
    start_skills = ["Agidyne", "Blight"]  # Набор заклинаний по умолчанию
    can_be_found = False  # Можно ли получить персону в подземелье

class SocialLink: # Сюжетное ответвление для установления отношений с персонажем
    name = "Yukiko Amagi"  # Имя персонажа
    arcana = "Priestess" # Аркан
    current_level = 4 # Текущий уровень отношений
    is_plot = False  # Является ли линк дефолтным по сюжету
    is_romance = True  # Можно ли заромансить персонажа
    perks = ["Fan Assault"]  # Список улучшений, получаемых в ходе развития связи

class Dungeon:  # Подземелье
    name = "Steamy Bathhouse" # Название подземелья
    floors = 11 # Количество этажей
    start_date = "2011-12-05"  # Первый день доступа в данж по игровому времени
    deadline = "2011-4-06"  # Дедлайн прохождения данжа по игровому времени
    shadows = ["Autonomic Basalt", "Monopolizing Cupid", "Pursuing Pesce", "Nizam Beast"]  # Враги
    treasure = ["Kintabi Gusoku", "Talisman", "Fire Suppressor"]  # Предметы, которые могут выпасти в сундуках
    is_obligatory = True  # Является ли данж обязательным для продвижения по основному сюжету

personas = []
for i in range(2):
    persona = Persona()
    personas.append(persona)
personas[0].name = "Trumpeter"
personas[0].arcana = "Judgement"
personas[0].min_level = 67
personas[0].current_level = 70
personas[0].start_skills = ["Megidola", "Ziodyne", "Electric Amp"]
personas[0].can_be_found = False

print(personas[0].name, personas[1].name)

dungeons = []
for i in range(2):
    dungeon = Dungeon()
    dungeons.append(dungeon)
dungeons[0].name = "Yukiko's Castle"
dungeons[0].floors = 8
dungeons[0].start_date = "2011-17-04"
dungeons[0].deadline = "2011-29-04"
dungeons[0].shadows = ["Lying Hablerie", "Calm Pesce", "Trance Twins"]
dungeons[0].treasure = ["Gentleman's Tux", "Wing Strap", "Ice Vow"]
dungeons[0].is_obligatory = True

print(dungeons[0].name,
dungeons[0].floors,
dungeons[0].start_date,
dungeons[0].deadline,
dungeons[0].shadows,
dungeons[0].is_obligatory)

# 1.3. 
my_persona = Persona()
current_skills = my_persona.start_skills

if my_persona.current_level == 63:
    current_skills.append("Power Charge")  # На 63 уровне открывается заклинание "Power Charge"
print(current_skills)
print(my_persona.start_skills)
# В итоге такой программы изменится список my_persona.start_skills, который должен остаться неизменным. Исправить проблему можно с помощью создания полной копии на 30й строке: my_persona.start_skills.copy().

    




