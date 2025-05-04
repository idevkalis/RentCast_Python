# main.py
import MarketStatistics
from db_connection import DatabaseConnection

def main():
    db = DatabaseConnection()
    conn = db.connect()

    if conn:
        try:
            with conn.cursor() as cursor:
                MarketStatistics.insert_marketStatsByALLZipCode(db)
        except Exception as e:
            print("❌ Failed to process market data:", e)
        finally:
            conn.close()

if __name__ == "__main__":
    main()
