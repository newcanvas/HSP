# Рефлексия:
# 1.2. Классы составлены достаточно адекватно и подробно, сравнивая с эталонными. Можно было тоже придумать пример взаимодействия с этими данными.

# Решение:
class Persona: # Боевая персона
   
    def __init__(self, persona_name, persona_arcana, persona_min_level, persona_current_level, persona_skills):
        self.name = persona_name # Имя персоны
        self.arcana = persona_arcana # Аркан
        self.min_level = persona_min_level # Минимальный уровень протагониста для призыва персоны
        self.current_level = persona_current_level # Текущий уровень персоны
        self.skills = persona_skills  # Набор заклинаний
        self.is_obtained = False # Есть ли данная персона в арсенале протагониста

    def NewSkill(self, new_skill):
        self.skills.append(new_skill)

    def LevelUp(self, levels):
        self.current_level += levels

    def ObtainPersona(self):
        self.is_obtained = True

Mara_persona = Persona("Mara", "Tower", 62, 63, ["Agidyne", "Blight"])

if Mara_persona.current_level >= Mara_persona.min_level:
    Mara_persona.ObtainPersona()

if Mara_persona.is_obtained:
    Mara_persona.LevelUp(2)
    Mara_persona.NewSkill("Power Charge")
    
print(Mara_persona.skills)

class SocialLink: # Сюжетное ответвление для установления отношений с персонажем
    
    def __init__(self, sl_name, sl_arcana, sl_current_level, sl_current_date, sl_deadline):
        self.name = sl_name  # Имя персонажа
        self.arcana = sl_arcana # Аркан
        self.current_level = sl_current_level # Текущий уровень отношений
        self.current_date = sl_current_date  # Текущая дата по игровому времени
        self.deadline = sl_deadline  # Дедлайн прохождения сюжета по игровому времени
        self.is_finished = False # Завершен ли сюжет

    def FinishSL(self):
        self.is_finished = True

    def FailSL(self):
        self.current_level = 0

    def ProgressSL(self):
        self.current_level += 1

Yukiko = SocialLink("Yukiko Amagi", "Priestess", 4, "2011-4-07", "2011-4-06")

if Yukiko.current_date > Yukiko.deadline:
    Yukiko.FailSL()
    print(f"Текущий уровень отношений: {Yukiko.current_level}")
    print("Время на прохождение сюжета вышло.")
elif  Yukiko.current_level == 10:
    Yukiko.FinishSL()
    print("Сюжет пройден.")
else: 
    Yukiko.ProgressSL()


