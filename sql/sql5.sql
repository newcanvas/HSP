--7.3.1. Вычислимое поле таблицы Order Details, в котором укажите значение поля Discount, выраженное в процентах.
SELECT ROUND(Discount * 100, 0) AS discount_percent
FROM Northwnd_old.dbo.[Order Details];

--7.3.2. Выведите все поля таблицы Order Details, для которых количество единиц товара на складе больше 40.
SELECT *
FROM Northwnd_old.dbo.[Order Details]
WHERE ProductID IN (
	SELECT DISTINCT ProductID 
	FROM Northwnd_old.dbo.Products
	WHERE UnitsInStock > 40);

--7.3.3. Расширьте предыдущий запрос проверкой, чтобы стоимость товара (поле Freight таблицы Orders) было не менее 50.
SELECT *
FROM Northwnd_old.dbo.[Order Details]
WHERE ProductID IN (
	SELECT DISTINCT ProductID 
	FROM Northwnd_old.dbo.Products
	WHERE UnitsInStock > 40)
AND OrderID IN (
    SELECT DISTINCT OrderID
    FROM Northwnd_old.dbo.Orders
    WHERE Freight >= 50);
