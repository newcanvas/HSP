--10.4.1. Перепишите задание 8.3.2 через синтаксис JOIN.
SELECT DISTINCT p.ProductName, od.UnitPrice
FROM Northwnd_old.dbo.Products p JOIN Northwnd_old.dbo.[Order Details] od
ON p.ProductID = od.ProductID
WHERE od.UnitPrice < 20;

--10.4.2. Имеется запрос. Проверьте этот запрос с вариантом FULL JOIN -- за счёт чего выдача получилась объёмнее? Почему значения NULL встречаются в обоих полях набора?
/* 
Так как CustomerID компании может присутствовать в одной таблице, но отсутствовать в другой, при INNER JOIN такие записи будут исключены. Если же сделать FULL JOIN, то попадут все записи без исключения
*/

--10.4.3. Подумайте, как с помощью предложения WHERE превратить запрос CROSS JOIN в INNER JOIN.
/* 
Его можно превратить, если указать связь по ключу в условии WHERE.
*/

--10.4.4. Перепишите данный запрос в INNER JOIN.
SELECT Products.ProductName, [Order Details].UnitPrice
FROM Products JOIN [Order Details]
ON Products.ProductID = [Order Details].ProductID;
