# db_connection.py
import configparser
import pyodbc

class DatabaseConnection:
    def __init__(self, config_path='db_config.ini'):
        config = configparser.ConfigParser()
        config.read(config_path)

        self.conn_str = (
            f'DRIVER={{{config["sqlserver"]["driver"]}}};'
            f'SERVER={config["sqlserver"]["server"]};'
            f'DATABASE={config["sqlserver"]["database"]};'
            f'Trusted_Connection=yes;'
        )

    def connect(self):
        try:
            conn = pyodbc.connect(self.conn_str)
            return conn
        except Exception as e:
            print("❌ Failed to connect to SQL Server:", e)
            return None

    def insert_salesData(self, fkCategoryTypeId, ZipCode, avgDaysOnMarket, avgPrice, avgPricePerSquareFoot,
                         avgSquareFootage, Date, MaxDaysOnMarket, MaxPrice, MaxPricePerSquareFoot, MaxSquareFootage,
                         MedianDaysOnMarket, MedianPrice, MedianPricePerSqFt, MedianSquareFootage, MinDaysOnMarket,
                         MinPrice, MinPricePerSquareFoot, MinSquareFootage, NewListings, TotalListings):
        conn = self.connect()
        if not conn:
            return
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO tblSalesData (fkCategoryTypeId, ZipCode, avgDaysOnMarket, avgPrice, avgPricePerSquareFoot, avgSquareFootage, Date, MaxDaysOnMarket, MaxPrice, MaxPricePerSquareFoot, MaxSquareFootage, MedianDaysOnMarket, MedianPrice, MedianPricePerSqFt, MedianSquareFootage, MinDaysOnMarket, MinPrice, MinPricePerSquareFoot, MinSquareFootage, NewListings, TotalListings) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (fkCategoryTypeId, ZipCode, avgDaysOnMarket, avgPrice, avgPricePerSquareFoot, avgSquareFootage, Date,
                 MaxDaysOnMarket, MaxPrice, MaxPricePerSquareFoot, MaxSquareFootage, MedianDaysOnMarket, MedianPrice,
                 MedianPricePerSqFt, MedianSquareFootage, MinDaysOnMarket, MinPrice, MinPricePerSquareFoot,
                 MinSquareFootage, NewListings, TotalListings)
            )
            conn.commit()
            print("✅ Sales data inserted.")
        except Exception as e:
            print("❌ Error inserting sales data:", e)
        finally:
            conn.close()


