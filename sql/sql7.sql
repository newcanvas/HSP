--9.4.1. Найдите все пары из разных (уникальных) заказчиков (Customers), для которых не задан регион (поле Region).

SELECT DISTINCT t1.ContactName, t2.ContactName
FROM Northwnd_old.dbo.Customers t1, Northwnd_old.dbo.Customers t2 
WHERE t1.ContactName <> t2.ContactName
AND t1.Region IS NULL;

--9.4.2. Найдите вложенным запросом список заказов (Orders), в котором у заказчиков (Customers) регион не пуст (поле Region)
SELECT *
FROM Orders t1
WHERE EXISTS
(SELECT * FROM Northwnd_old.dbo.Customers t2
WHERE t2.Region IS NULL
AND t1.CustomerID = t2.CustomerID);

--9.4.3. Найдите все заказы (таблица Orders), цена за доставку товара которых (Freight) превышает цену любого товара (поле UnitPrice, таблица Products).
SELECT *
FROM Orders t1
WHERE t1.Freight > ANY
(SELECT UnitPrice FROM Northwnd_old.dbo.Products t2);
