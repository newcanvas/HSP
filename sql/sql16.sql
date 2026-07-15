--1. Найдите все отряды, у которых нет лидера.
SELECT *
FROM Squads
WHERE leader_id IS NULL

--2. Получите список всех гномов старше 150 лет, у которых профессия "Warrior".
SELECT dwarf_id
FROM Dwarves
WHERE age > 150
AND profession = 'Warrior'

--3. Найдите гномов, у которых есть хотя бы один предмет типа "weapon".
SELECT dwarf_id
FROM Dwarves
WHERE dwarf_id IN (
    SELECT owner_id
    FROM Items
    WHERE type = 'weapon'
)

--4. Получите количество задач для каждого гнома, сгруппировав их по статусу.
SELECT d.dwarf_id, t.status, COUNT(t.task_id) AS task_count
FROM Tasks t LEFT JOIN Dwarves d
ON t.assigned_to = d.dwarf_id
GROUP BY t.assigned_to, t.status

--5. Найдите все задачи, которые были назначены гномам из отряда с именем "Guardians".
SELECT task_id
FROM Tasks
WHERE assigned_to IN(
    SELECT d.dwarf_id 
    FROM Dwarves d LEFT JOIN Squads s
    ON d.squad_id = s.squad_id
    WHERE s.name = 'Guardians'
)

--6. Выведите всех гномов и их ближайших родственников, указав тип родственных отношений.
SELECT d.dwarf_id, r.related_to, r.relationship
FROM Dwarves d
LEFT JOIN Relationships r ON d.dwarf_id = r.dwarf_id
AND relationship IN ('Супруг', 'Родитель')
