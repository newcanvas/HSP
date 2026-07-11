1.
SELECT t1.*, t2.* FROM Dwarves t1, Squads t2
WHERE t1.squad_id IS NOT NULL
AND t1.squad_id = t2.squad_id

2.
SELECT * FROM Dwarves
WHERE  profession = 'miner'
AND squad_id IS NULL

3.
SELECT * FROM Tasks
WHERE status = 'pending'

4.
SELECT owner_id, COUNT(DISTINCT item_id)
FROM Items
WHERE owner_id IS NOT NULL
GROUP BY owner_id

5.
SELECT s.squad_id, s.name, COUNT(DISCTINCT d.dwarf_id)
FROM Squads s FULL JOIN Dwarves d
ON d.squad_id = s.squad_id
GROUP BY s.squad_id, s.name

6.
SELECT profession, COUNT(DISCTINCT dwarf_id) AS dwarf_count
WHERE dwarf_id IN (SELECT assigned_to FROM Tasks WHERE status IN ("pending", "in_progress"))
ORDER BY dwarf_count DESC

7.
SELECT it.type, AVG(d.age)
FROM Items it JOIN Dwarves d
ON it.owner_id = d.dwarf_id
GROUP BY it.type

8. 
SELECT dwarf_id
FROM Dwarves
WHERE (dwarf_id NOT IN (SELECT owner_id  FROM Items))
AND (age > (SELECT AVG(age) FROM  Dwarves))
