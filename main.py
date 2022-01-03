import requests
#from pprint import pprint
from config import open_weather_token

def get_weather(city, open_weather_token):
    code_to_smile = {
      "Clear": "Clear \u00002600",
      "Clouds": "clouds \u00002601",
      "Rain": "Rainy \u00002614",
      "Snow": "Snow \u0001F328",
      "Mist": "Foggy \u0001f328"
    }
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&utils=metric"
        )
        data = r.json()
        #pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_desc = data["weather"][0]["main"]
        if weather_desc in code_to_smile:
          wd = code_to_smile[weather_desc]
        else: 
          wd = "just look around )"   

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]


        print(f"The weather in {city}:\nTemperature is {cur_weather}°C {wd},\nHumidity is {humidity}%,\nPressure is {pressure}atm,\nWind speed is {wind}.")

    except Exception as ex:
        print(ex)
        print("You have entered wrong city, please check!")


def main():
    city = input("Enter the city: ")
    get_weather(city, open_weather_token)


if __name__ == "__main__":
    main()
