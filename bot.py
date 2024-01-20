import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("TG_APY_KEY")

bot = telebot.TeleBot(api_key)


@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Узнать погоду🥶"))
    bot.send_message(message.chat.id, 'Я могу показать погоду в любом городе!', 
                     reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == 'Узнать погоду🥶':
        bot.send_message(message.chat.id, 'Введите название города')
    else:
        data = get_weather(message.text)
        if data:
            result = f"Температура в городе {message.text}:\
    {data['temperature']}\nАтмосферное давление: {data['atm_pressure']} \
    мм рт.ст.\nСкорость ветра (в м/с).: {data['wind_speed']} м/с"
        else:
            result = 'Город не найден'
        bot.send_message(message.chat.id, result)


def get_weather(city: str):
    headers = {
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    try:
        response = requests.get(f"http://django:8000/weather/?city={city}",
                                headers=headers)
        if response.status_code == 200:
            return response.json()
    except Exception:
        return None


if __name__ == '__main__':
    bot.polling()
