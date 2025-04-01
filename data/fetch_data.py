import requests

def get_air_quality(city):
    url = f"https://api.openaq.org/v2/latest?city={city}&country=DE"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not fetch data"}
