import requests

api_key = '8fba6859b698d4d6c03630b89a79efa8'

user_input = input("Enter city: ")

if user_input.lower() == "tree":
        print("totro")
        exit()

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
print(weather_data.status_code)

if weather_data.json()['cod'] == '404':
    raise ValueError("city not found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    print(f'the weather in {user_input} is: {weather}')
    print(f'the temperature in {user_input} is: {temp}F')