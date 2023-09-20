import requests
from flight_data import FlightData

teq_endpoint = 'https://api.tequila.kiwi.com/v2'
teq_api = 'wIM8zBQic4fnj0ZYEICdNm7OR19XVgnP'

class FlightSearch:
    def get_destination_code(self):
        location_endpoint = f'{teq_endpoint}/locations/query'
        headers = {'apikey': teq_api}
        query = {'term': 'city_name', 'loaction_types': 'city'}
        res = requests.get(url=teq_endpoint, headers=headers, params=query)
        results = res.json()['locations']
        code = results[0]['code']
        return code
    
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": teq_api}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(
            url=f"{teq_endpoint}/v2/search",
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data