# db_connection.py
import configparser
import pyodbc

class DatabaseConnection:
    def __init__(self, config_path='db_config.ini'):
        config = configparser.ConfigParser()
        config.read(config_path)
        config.read(config_path)

        self.conn_str = (
            f'DRIVER={{{config["sqlserver"]["driver"]}}};'
            f'SERVER={config["sqlserver"]["server"]};'
            f'DATABASE={config["sqlserver"]["database"]};'
            f'UID={config["sqlserver"]["username"]};'
            f'PWD={config["sqlserver"]["password"]}'
        )

    def connect(self):
        try:
            conn = pyodbc.connect(self.conn_str)
            return conn
        except Exception as e:
            print("❌ Failed to connect to SQL Server:", e)
            return None

    # def insert_house(self, address, sqft, estimate, price):
    #     conn = self.connect()
    #     if not conn:
    #         return
    #     try:
    #         cursor = conn.cursor()
    #         cursor.execute(
    #             "INSERT INTO tblHouse (Address, sqft, Zestimate, Price) VALUES (?, ?, ?, ?)",
    #             (address, sqft, estimate, price)
    #         )
    #         conn.commit()
    #         print("✅ House inserted.")
    #     except Exception as e:
    #         print("❌ Error inserting house:", e)
    #     finally:
    #         conn.close()

    def insert_marketData(self, address, sqft, estimate, price):
        conn = self.connect()
        if not conn:
            return
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO tblHouse (Address, sqft, Zestimate, Price) VALUES (?, ?, ?, ?)",
                (address, sqft, estimate, price)
            )
            conn.commit()
            print("✅ House inserted.")
        except Exception as e:
            print("❌ Error inserting house:", e)
        finally:
            conn.close()

