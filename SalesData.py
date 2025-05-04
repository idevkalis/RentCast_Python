from collections import defaultdict

class SalesData:
    def insert_marketStatsSalesData(self, sale_data, zip_code, db):
        grouped_by_date = defaultdict(lambda: {"bedrooms": [], "propertyTypes": []})

        # Iterate over 'history' inside sale_data
        history = sale_data.get("history", {})
        for date_str, history_data in history.items():
            # Handle dataByBedrooms
            for item in history_data.get("dataByBedrooms", []):
                grouped_by_date[date_str]["bedrooms"].append((item.get("propertyType", "Unknown"), item))

            # Handle dataByPropertyType
            for item in history_data.get("dataByPropertyType", []):
                grouped_by_date[date_str]["propertyTypes"].append((item.get("propertyType", "Unknown"), item))

        # Process each date group
        for date_str, categories in grouped_by_date.items():
            date = f"{date_str}-01"

            # Handle both bedrooms and propertyTypes categories
            for category_label, CategoryTypeID in [("bedrooms", 1), ("propertyTypes", 2)]:
                for property_type, stats in categories[category_label]:
                    self.insert_marketStatSalesData(stats, CategoryTypeID, zip_code, date, db)

    def insert_marketStatSalesData(self, stats, CategoryTypeID, zip_code, date, db):
        # Determine the category value based on CategoryTypeID
        if CategoryTypeID == 1:
            CategoryValue = stats.get('bedrooms', None)
        elif CategoryTypeID == 2:
            CategoryValue = stats.get('propertyType', None)
        else:
            CategoryValue = None  # Fallback if CategoryTypeID is unexpected

        # Extract stats with fallback to None
        avgDaysOnMarket = stats.get('averageDaysOnMarket')
        avgPrice = stats.get('averagePrice')
        avgPricePerSquareFoot = stats.get('averagePricePerSquareFoot')
        avgSquareFootage = stats.get('averageSquareFootage')
        MedianPrice = stats.get('medianPrice')
        MedianPricePerSqFt = stats.get('medianPricePerSquareFoot')
        MaxDaysOnMarket = stats.get('maxDaysOnMarket')
        MaxPrice = stats.get('maxPrice')
        MaxPricePerSquareFoot = stats.get('maxPricePerSquareFoot')
        MaxSquareFootage = stats.get('maxSquareFootage')
        MedianDaysOnMarket = stats.get('medianDaysOnMarket')
        MedianSquareFootage = stats.get('medianSquareFootage')
        MinDaysOnMarket = stats.get('minDaysOnMarket')
        MinPrice = stats.get('minPrice')
        MinPricePerSquareFoot = stats.get('minPricePerSquareFoot')
        MinSquareFootage = stats.get('minSquareFootage')
        NewListings = stats.get('newListings')
        TotalListings = stats.get('totalListings')

        # Insert into the database
        db.insert_salesData(
            CategoryTypeID,
            CategoryValue,
            zip_code,
            avgDaysOnMarket,
            avgPrice,
            avgPricePerSquareFoot,
            avgSquareFootage,
            date,
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

        print(f"✅ Inserted data for Zip: {zip_code}, Category: {CategoryTypeID}, Date: {date}")
