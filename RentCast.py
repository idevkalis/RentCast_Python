import pandas as pd
import requests
import json

class RentCast:
    def __init__(self):
        self.api_key = self.get_api_token()

    def get_api_token(self):
        # Read API key from CSV
        df = pd.read_csv(r"C:\Users\danie\OneDrive\Desktop\RentCast\rentcast_api_keys.csv")
        api_key = df.loc[df['API'] == 'x-api', 'KEY'].iloc[0]
        api_key = "3722b03c8961444eb3bd843e6bc1f859"
        return api_key

    # def get_property_list(self, city="", state="", property_type=""):
    #     base_url = "https://api.rentcast.io/v1/properties"
    #     query_params = []
    #
    #     if city:
    #         query_params.append(f"city={city}")
    #     if state:
    #         query_params.append(f"state={state}")
    #     if property_type:
    #         query_params.append(f"propertyType={property_type}")
    #
    #     # Combine query params
    #     url = f"{base_url}?{'&'.join(query_params)}" if query_params else base_url
    #
    #     headers = {
    #         "X-Api-Key": self.api_key,
    #         "accept": "application/json"
    #     }
    #
    #     response = requests.get(url, headers=headers)
    #
    #     if response.status_code == 200:
    #         data = response.json()
    #         # Optional: print formatted data
    #         # print(json.dumps(data, indent=4))
    #         return data  # ✅ Return list of properties
    #     else:
    #         print("❌ Request failed:", response.status_code)
    #         print(response.text)
    #         return None  # ✅ Not "nothing"

    def get_market_statistics(self, zipCode="", dataType="", historyRange=""):
        base_url = "https://api.rentcast.io/v1/markets"
        query_params = []

        if zipCode:
            query_params.append(f"zipCode={zipCode}")
        if dataType:
            query_params.append(f"dataType={dataType}")
        if historyRange:
            query_params.append(f"historyRange={historyRange}")

        # Combine query params
        url = f"{base_url}?{'&'.join(query_params)}" if query_params else base_url

        headers = {
            "X-Api-Key": self.api_key,
            "accept": "application/json"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data  # ✅ Return list of market statistics
        else:
            print("❌ Request failed:", response.status_code)
            print(response.text)
            return None  # ✅ Not "nothing"
