--13.3.1. Увеличьте скидку (Discount) в таблице Order Details до 20% (0.20) для тех единиц товара, которых на складе хранится больше 50 (поле Quantity). 
UPDATE [Order Details]
SET Discount = 0.20
WHERE Quantity > 50 
AND Discount < 0.20

--13.3.2. В таблице Contacts измените все контактные данные, ранее приходившиеся на Berlin (поле City) и Germany (поле Country), соответственно на Piter и Russia. 
UPDATE Contacts
SET City = 'Piter', Country = 'Russia'
WHERE City = 'Berlin' AND Country = 'Germany'

--13.3.3. Добавьте и затем удалите несколько записей в таблице Shippers. По какому критерию вы удаляли свежие записи?
INSERT INTO Shippers(CompanyName)
VALUES('Roga i Kopyta'), ('New Firm'), ('OOO Perevozki');

DELETE FROM Shippers
WHERE ShipperID > 3;
