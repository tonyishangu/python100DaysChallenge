import requests

sheety_endpoint = 'https://api.sheety.co/58bb52ef8e6574e39e8d011a310c810e/flightDeals/prices'
class DataManager:
    def __init__(self):
        self.destination = {}
    def get_destinations(self):
        # use sheety api to get info from google sheets
        res = requests.get(url=sheety_endpoint)
        data = res.json()
        self.destination = data['prices']
        return self.destination


    # 6. In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)