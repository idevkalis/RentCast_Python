CREATE TABLE tblCategoryType (
    pkCategoryTypeId INT PRIMARY KEY IDENTITY(1,1),
    CategoryTypeName VARCHAR(100) NOT NULL
);
GO

-- Insert values for each CategoryType (By Bedroom, By Property, By History)
INSERT INTO tblCategoryType (CategoryTypeName)
VALUES ('By Bedroom'), ('By Property'), ('By History');
GO

CREATE TABLE tblSalesData (
    pkSalesDataId INT PRIMARY KEY IDENTITY(1,1),
    fkCategoryTypeId INT,  -- Foreign key to tblCategoryType
    ZipCode VARCHAR(10) NOT NULL,
    avgDaysOnMarket DECIMAL(18, 2),
    avgPrice DECIMAL(18, 2),
    avgPricePerSquareFoot DECIMAL(18, 2),
    avgSquareFootage DECIMAL(18, 2),
    Date DATE NOT NULL,
    MaxDaysOnMarket DECIMAL(18, 2),
    MaxPrice DECIMAL(18, 2),
    MaxPricePerSquareFoot DECIMAL(18, 2),
    MaxSquareFootage DECIMAL(18, 2),
    MedianDaysOnMarket DECIMAL(18, 2),
    MedianPrice DECIMAL(18, 2),
    MedianPricePerSqFt DECIMAL(18, 2),
    MedianSquareFootage DECIMAL(18, 2),
    MinDaysOnMarket DECIMAL(18, 2),
    MinPrice DECIMAL(18, 2),
    MinPricePerSquareFoot DECIMAL(18, 2),
    MinSquareFootage DECIMAL(18, 2),
    NewListings INT,
    TotalListings INT,
    FOREIGN KEY (fkCategoryTypeId) REFERENCES tblCategoryType (pkCategoryTypeId)
);
GO



