import requests

class TemperatureProvider:
    def get_temperature(self):
        pass

class WeatherService:
    def get_temperature_in_celsius(self, city, state_code, country_code):

        # Replace with your API key
        api_key = "7b18a38410ecd84d769e56490d3a6b5e"

        # Replace with the city and state you want to get the weather for
        city = city
        state_code = state_code
        country_code = country_code

        # Make the API request
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{state_code},{country_code}&units=metric&appid={api_key}"
        response = requests.get(url)
        data = response.json()

        # Extract the temperature in Celsius
        temperature = data['main']['temp']
        print(f"The temperature in {city} is {temperature}°C")
        return temperature
class TemperatureAdapter(TemperatureProvider):
    def __init__(self, adaptee):
        self.adaptee = adaptee
    def get_temperature(self,city, state_code, country_code):
        temp_in_C = self.adaptee.get_temperature_in_celsius(city, state_code, country_code)
        temp_in_F = (temp_in_C * 9/5) + 32
        return temp_in_F


# Client code
def find_temperature(provider,city, state_code, country_code):
    temp = provider.get_temperature(city, state_code, country_code)
    return temp

ws = WeatherService()
ta = TemperatureAdapter(ws)
print(find_temperature(ta,"Patna","BR","IN"))


