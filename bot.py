from aiogram.types import message
import requests
import datetime
from config import bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token = bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Hi, I can tell the current weather in any location. Enter The city: ")

@dp.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
      "Clear": "Clear \U00002600",
      "Clouds": "clouds \U00002601",
      "Rain": "Rainy \U00002614",
      "Snow": "Snow \U0001F328",
      "Mist": "Foggy \U0001F328"
    }
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

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

        await message.reply(f"The weather in {city}:"
        f"\n \U0001f321 Temperature is {cur_weather}°C {wd},"
        f"\n \U0001f4a7 Humidity is {humidity}%,"
        f"\n \uFE0F Pressure is {pressure} atm,"
        f"\n \U0001F32B Wind speed is {wind} m/s.")

    except Exception:
        await message.reply("You have entered wrong city, please check!")
    


if __name__ == "__main__":
    executor.start_polling(dp)
