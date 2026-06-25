-- 5.4.1. Cписок сотрудников по дате рождения, начиная с самых молодых, и по стране.
SELECT *
FROM Northwnd_old.dbo.Employees
ORDER BY BirthDate DESC, Country;

-- 5.4.2. Исключите из предыдущего набора те записи, в которых поле Region равно NULL.
SELECT *
FROM Northwnd_old.dbo.Employees
WHERE Region IS NOT NULL
ORDER BY BirthDate DESC, Country;

-- 5.4.3. Найдите среднюю, минимальную и максимальную цены по полю UnitPrice из таблицы Order Details.
SELECT 
	AVG(UnitPrice)
	,MIN(UnitPrice)
	,MAX(UnitPrice)
FROM Northwnd_old.dbo.[Order Details];

-- 5.4.4. Количество уникальных городов в списке пользователей.
SELECT COUNT(DISTINCT City)
FROM Northwnd_old.dbo.Customers;
