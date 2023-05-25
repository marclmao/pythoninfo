import requests

api_key = input("Enter OpenWeatherMap API Key: ")

city = input("Enter the city name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temperature_kelvin = data["main"]["temp"]
    temperature_celsius = temperature_kelvin - 273.15
    print("Weather Information for", city)
    print("Temperature:", temperature_celsius, "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Weather:", data["weather"][0]["description"])
else:
    print("you prolly misspelled it lol heres ur error code ", response.status_code)

ipify_api = input("Ipify API Key: ")
url = f"https://geo.ipify.org/api/v2/country?apiKey={ipify_api}ipAddress="  # ipify api

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Network Info: ", data)
else:
    print("Error Code", response.status_code)

