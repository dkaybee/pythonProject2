#first import the module needed

import requests
import secret

base_url = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{base_url}?appid={secret.api_key}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    print(200)
else:
    print("error")

# Convert response to Json (.json needed to work with our data)
data = response.json()

#We use slicing and indexing to find the various climatic conditions
temperature= round(data['main']['temp']-273.15,2)

humidity=data['main']['humidity']

rain=data['weather'][0]['description']
name_of_city = data['name']

print (f'The temperature in {name_of_city} is {temperature} degrees')
print(f'The humidity in {name_of_city} is {humidity}')
