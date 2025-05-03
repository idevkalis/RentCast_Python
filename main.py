from db_connection import DatabaseConnection
from RentCast import RentCast

# Create database connection instance
db = DatabaseConnection()

# Test DB connection
conn = db.connect()
if conn:
    cursor = conn.cursor()
    cursor.execute("SELECT GETDATE()")
    print("Current SQL Server time:", cursor.fetchone()[0])
    conn.close()

# Create RentCast instance
rentcast = RentCast()

# Get property data
# properties = rentcast.get_property_list(city="Chicago", state="IL", property_type="SingleFamily")
#
# # Insert properties into database
# for prop in properties:
#     address = prop.get("addressLine1", "Unknown Address")
#     db.insert_house(address, 100, 412000.00, 912000.00)

# Get property data
marketStatistics = rentcast.get_market_statistics(zipCode="60616", dataType="Sale", historyRange="60")

# Insert properties into database
for marketData in marketStatistics:
    address = marketData.get("addressLine1", "Unknown Address")
    db.insert_marketData(address, 100, 412000.00, 912000.00)
