/* 
Categories и Products: один-ко-многим по полю CategoryID
Contacts не имеет связей
Customers и Orders: один-ко-многим по полю CustomerID и таблице Customer
Employees и Territories: один-ко-многим через таблицу EmployeeTerritories
Orders и Products: многие-ко-многим через таблицу Order Details, поскольку один заказ может содержать несколько товаров, и один товар может быть в нескольких заказах.
Orders и Employees: один-ко-многим по полю EmployeeID
Suppliers и Products: один-ко-многим по полю SupplierID
Territories и Region: : один-ко-многим по полю RegionID
Shippers и Orders: один-ко-многим по полю ShipperID
*/
