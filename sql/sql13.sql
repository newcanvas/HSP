CREATE TABLE Territories ( 
    TerritoryID nvarchar(20) NOT NULL, 
    TerritoryDescription nchar(20) NOT NULL,
    RegionID int NOT NULL ); 

INSERT INTO Region(RegionID, RegionDescription)
VALUES(5, 'Russia');

INSERT INTO Territories(TerritoryID, TerritoryDescription, RegionID)
VALUES('747474', 'Chelyabinsk', 5), ('777777', 'Moscow', 5), ('989898', 'Piter', 5);
