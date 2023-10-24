import os
import telebot
import tempfile
from PIL import ImageGrab
import subprocess


API_TOKEN = 'YOUR_TOKEN'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("turnOn")
    markup.add("turnOff")
    markup.add("Get Screenshot")
    bot.send_message(message.chat.id, 'Welcome', reply_markup=markup)

@bot.message_handler(regexp='turnOn')
def turn_on_computer():
    mac_address = 'YOUR_MAC_ADDRESS'
    subprocess.call(['wakeonlan', mac_address])

@bot.message_handler(regexp='turnOff')
def echo_message(message):
    bot.send_message(message.chat.id, 'Выключаю...')
    os.system("sudo shutdown -h 0")

@bot.message_handler(regexp='Get Screenshot')
def echo_message(message):
    path = tempfile.gettempdir() + 'screenshot.png'
    screenshot = ImageGrab.grab()
    screenshot.save(path, 'PNG')
    bot.send_photo(message.chat.id, open(path, 'rb'))


bot.infinity_polling()
