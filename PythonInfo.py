import requests

api_key = "enter openweathermap api key"  # put yo api key in here

city = input("Enter the city name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Weather Information for", city)
    print("Temperature:", data["main"]["temp"], "K")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Weather:", data["weather"][0]["description"])
else:
    print("Error:", response.status_code)

url = "ipify api key"  # ipify api (remove ip when you copy from website)

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Network Info ", data)
else:
    print("fuck it didnt work this is the error code", response.status_code)

