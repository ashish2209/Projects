import requests

api_address = 'http://api.openweathermap.org/data/2.5/weather?q=Kanpur&appid=3ec8dcfab29b15cc8c2c217a767f4a6c'
json_data = requests.get(api_address).json()

def temp():
    temperature = round(json_data["main"]["temp"]-273,1)
    return temperature
def des():
    description = json_data["weather"][0]["description"]
    return description
print(temp())
print(des())