import telebot
from telebot import types

token = "YOUR_TELEGRAM_TOKEN_HERE"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])  # /start
def say_hello(message: types.Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Olá, eu sou o Wall-PI!")


bot.infinity_polling()
