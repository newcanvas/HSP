--11.5.1. Отберите с помощью LEFT JOIN все записи из таблицы Customers, для которых FK-ключ таблицы Orders пустой.
SELECT *
FROM Customers c LEFT JOIN Orders o
ON c.CustomerID = o.CustomerID
WHERE o.CustomerID IS NULL;

--11.5.2. Выведите конкретную информацию по всем пользователям Customers и поставщикам Suppliers -- имя контактной персоны, город и страну, а также идентификацию группы (пользователь или поставщик).
SELECT ContactName, City, Country, 'Customer' AS GroupID
FROM Customers
UNION 
SELECT ContactName, City, Country, 'Supplier' AS GroupID
FROM Suppliers;
