--12.3.1. Добавьте нового пользователя в таблицу Employees.
INSERT INTO Employees (LastName, FirstName, Title, TitleOfCourtesy)
VALUES ('Petrov', 'Vasya', 'Salesman', 'Mr')

--12.3.2. Свяжите этого нового пользователя с какой-либо территорией с помощью таблицы EmployeeTerritories (многие-ко-многим).
INSERT INTO EmployeeTerritories(EmployeeID, TerritoryID)
VALUES (11, '01581'), (11, '06897'), (11, '02184');

--12.3.3. Попробуйте добавить новую запись в таблицу заказов Orders. Возникнут ли какие-либо конфликты?
INSERT INTO Orders(CustomerID, EmployeeID)
VALUES ('VINET', 11);
-- Конфликтов не возникло.
