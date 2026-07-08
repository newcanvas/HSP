CREATE INDEX idxTerritoryIDAndRegionID ON Territories (TerritoryID, RegionID);

CREATE CLUSTERED INDEX idxTerritoryID ON Territories (TerritoryID);
