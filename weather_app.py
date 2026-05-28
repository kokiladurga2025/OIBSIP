import requests

city = input("Enter city name: ")

url = "https://wttr.in/" + city + "?format=j1"

data = requests.get(url).json()

temperature = data["current_condition"][0]["temp_C"]
humidity = data["current_condition"][0]["humidity"]
condition = data["current_condition"][0]["weatherDesc"][0]["value"]

print("Temperature:", temperature, "°C")
print("Humidity:", humidity, "%")
print("Condition:", condition)
