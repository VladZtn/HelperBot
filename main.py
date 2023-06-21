import os
import telebot
import tempfile
from PIL import ImageGrab
import subprocess


API_TOKEN = '6027482375:AAH8fUTBKL41WwjIkQ35_jgkUwuhW7sLtTQ'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Включить")
    markup.add("Выключить")
    markup.add("Получить скриншот")
    bot.send_message(message.chat.id, 'Приветсвую', reply_markup=markup)

@bot.message_handler(regexp='включить')
def turn_on_computer():
    mac_address = 'FC:E2:6C:00:57:C7'
    subprocess.call(['wakeonlan', mac_address])

@bot.message_handler(regexp='выключить')
def echo_message(message):
    bot.send_message(message.chat.id, 'Выключаю...')
    os.system("sudo shutdown -h 0")

@bot.message_handler(regexp='получить скриншот')
def echo_message(message):
    path = tempfile.gettempdir() + 'screenshot.png'
    screenshot = ImageGrab.grab()
    screenshot.save(path, 'PNG')
    bot.send_photo(message.chat.id, open(path, 'rb'))


bot.infinity_polling()