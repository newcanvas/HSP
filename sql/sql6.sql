--8.3.1. Сформируйте список названий товаров с указанием для каждого из них соответствующей категории.
SELECT p.ProductName, c.CategoryID 
FROM Northwnd_old.dbo.Products p, Northwnd_old.dbo.Categories c
WHERE p.CategoryID = c.CategoryID;

--8.3.2. Организуйте эквисоединение, которое выводит цену и названия тех товаров, для которых цена за единицу (UnitPrice) в таблице Order Details меньше 20.
SELECT DISTINCT p.ProductName, od.UnitPrice
FROM Northwnd_old.dbo.Products p, Northwnd_old.dbo.[Order Details] od
WHERE p.ProductID = od.ProductID
AND od.UnitPrice < 20;

--8.3.3. Добавьте к предыдущему запросу третью таблицу Categories, и выведите в дополнение к названию товара его категорию.
SELECT DISTINCT p.ProductName, od.UnitPrice, c.CategoryID
FROM Northwnd_old.dbo.Products p, Northwnd_old.dbo.[Order Details] od, Northwnd_old.dbo.Categories c
WHERE p.ProductID = od.ProductID
AND od.UnitPrice < 20
AND p.CategoryID = c.CategoryID;
