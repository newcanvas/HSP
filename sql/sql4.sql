-- 6.3.1. Агрегация таблицы Contacts по полю ContactType.
SELECT 
    ContactType
    ,COUNT(*) AS count_all
FROM Northwnd_old.dbo.Contacts
GROUP BY ContactType;

-- 6.3.2. Средние цены товаров (UnitPrice) в каждой из категорий (CategoryId) таблицы Products, отсортированные по возрастанию.
SELECT 
	CategoryID
	,AVG(UnitPrice) AS avg_price
FROM Northwnd_old.dbo.Products
GROUP BY CategoryID
ORDER BY avg_price;
