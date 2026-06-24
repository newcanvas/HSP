-- 4.3.1. Все пользователи, фамилия контактной персоны которых начинается с C.
SELECT *
FROM Northwnd_old.dbo.Customers
WHERE ContactName LIKE 'C%';

--4.3.2. Все заказы, плата за перевозку груза у которых лежит в диапазоне от 100 до 200, а страна-поставщик -- либо USA, либо France.
SELECT *
FROM Northwnd_old.dbo.Orders
WHERE (Freight BETWEEN 100 AND 200) AND ShipCountry IN ('USA', 'France');

--4.3.3. Отфильтруйте таблицу EmployeeTerritories так, чтобы значение связующего поля TerritoryID находилось в промежутке от 6897 до 31000.
SELECT *
FROM Northwnd_old.dbo.EmployeeTerritories
WHERE TerritoryID BETWEEN 6897 AND 31000;
