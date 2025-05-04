# main.py
from db_connection import DatabaseConnection
from RentCast import RentCast


def process_market_data(db):
    rentcast = RentCast()

    # Fetch market statistics
    marketStatistics = rentcast.get_market_statistics(
        zipCode="60616",
        dataType="Sale",
        historyRange="2"
    )

    if marketStatistics:
        zip_code = marketStatistics.get("zipCode")
        sale_data = marketStatistics.get("saleData", {})
        last_updated_date = sale_data.get('lastUpdatedDate')  # Get the last updated date

        # Dynamically set CategoryTypeID based on the data in the JSON
        if 'dataByBedrooms' in sale_data:
            CategoryTypeID = 1  # CategoryTypeID for 'By Bedroom'
            data_by_type = sale_data.get("dataByBedrooms", [])
        elif 'dataByPropertyType' in sale_data:
            CategoryTypeID = 2  # CategoryTypeID for 'By Property'
            data_by_type = sale_data.get("dataByPropertyType", [])
        else:
            print("⚠️ No valid category type found in the data.")
            return  # Exit the function if no valid category type is found

        # Process the data for each property type
        for propertyTypeData in data_by_type:
            avgDaysOnMarket = propertyTypeData.get('averageDaysOnMarket')
            avgPrice = propertyTypeData.get('averagePrice')
            avgPricePerSquareFoot = propertyTypeData.get('averagePricePerSquareFoot')
            avgSquareFootage = propertyTypeData.get('averageSquareFootage')
            MedianPrice = propertyTypeData.get('medianPrice')
            MedianPricePerSqFt = propertyTypeData.get('medianPricePerSquareFoot')
            MaxDaysOnMarket = propertyTypeData.get('maxDaysOnMarket')
            MaxPrice = propertyTypeData.get('maxPrice')
            MaxPricePerSquareFoot = propertyTypeData.get('maxPricePerSquareFoot')
            MaxSquareFootage = propertyTypeData.get('maxSquareFootage')
            MedianDaysOnMarket = propertyTypeData.get('medianDaysOnMarket')
            MedianSquareFootage = propertyTypeData.get('medianSquareFootage')
            MinDaysOnMarket = propertyTypeData.get('minDaysOnMarket')
            MinPrice = propertyTypeData.get('minPrice')
            MinPricePerSquareFoot = propertyTypeData.get('minPricePerSquareFoot')
            MinSquareFootage = propertyTypeData.get('minSquareFootage')
            NewListings = propertyTypeData.get('newListings')
            TotalListings = propertyTypeData.get('totalListings')

            # Skip if any required field is missing
            if None in [
                avgDaysOnMarket, avgPrice, avgPricePerSquareFoot, avgSquareFootage,
                MedianPrice, MedianPricePerSqFt, MaxDaysOnMarket, MaxPrice,
                MaxPricePerSquareFoot, MaxSquareFootage, MedianDaysOnMarket,
                MedianSquareFootage, MinDaysOnMarket, MinPrice, MinPricePerSquareFoot,
                MinSquareFootage, NewListings, TotalListings
            ]:
                print(f"⚠️ Skipping record due to missing data: {propertyTypeData}")
                continue

            # Call the insert_salesData function
            db.insert_salesData(
                CategoryTypeID,  # Foreign Key referring to Category Type
                zip_code,
                avgDaysOnMarket,
                avgPrice,
                avgPricePerSquareFoot,
                avgSquareFootage,
                last_updated_date,
                MaxDaysOnMarket,
                MaxPrice,
                MaxPricePerSquareFoot,
                MaxSquareFootage,
                MedianDaysOnMarket,
                MedianPrice,
                MedianPricePerSqFt,
                MedianSquareFootage,
                MinDaysOnMarket,
                MinPrice,
                MinPricePerSquareFoot,
                MinSquareFootage,
                NewListings,
                TotalListings
            )

            print(
                f"✅ Inserted data for property type: {propertyTypeData.get('propertyType')} — Zip: {zip_code}, Avg Price: {avgPrice}")


def main():
    db = DatabaseConnection()
    conn = db.connect()

    if conn:
        try:
            with conn.cursor() as cursor:
                process_market_data(db)
        except Exception as e:
            print("❌ Failed to process market data:", e)
        finally:
            conn.close()

if __name__ == "__main__":
    main()
