-- 3.9.1. Запрос, формирующий полный список товаров (Products) и выводящий название товара и количество единиц на складе.

SELECT ProductName, UnitsInStock
FROM Northwnd_old.dbo.Products;

-- 3.9.2. Запрос, формирующий список товаров (Products) и выводящий название товара и цену для тех товаров, которые дешевле 20.
SELECT ProductName, UnitPrice
FROM Northwnd_old.dbo.Products
WHERE (UnitPrice < 20);

-- 3.9.3. Список заказов, у которых плата за доставку груза (Freight) лежит в диапазоне от 11.7 до 98.1.
SELECT *
FROM Northwnd_old.dbo.Orders
WHERE (Freight >= 11.7) AND (Freight <= 98.1);

-- 3.9.4. Список всех сотрудников - мужчин
SELECT *
FROM Northwnd_old.dbo.Employees
WHERE (TitleOfCourtesy = 'Dr.') OR (TitleOfCourtesy = 'Mr.')

-- 3.9.5. Список всех поставщиков из Японии.
SELECT *
FROM Northwnd_old.dbo.Suppliers
WHERE (Country = 'Japan');

-- 3.9.6. Все заказы, для которых идентификатор сотрудника-исполнителя равен 2, 4 или 8.
SELECT *
FROM Northwnd_old.dbo.Orders
WHERE EmployeeID IN (2, 4, 8);

-- 3.9.7. Идентификаторы заказов и товаров из таблицы Order Details, для которых цена больше 40, а количество меньше 10.

SELECT *
FROM Northwnd_old.dbo.[Order Details]
WHERE (UnitPrice > 40) AND (Quantity < 10);
