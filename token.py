import telebot
from telebot import types

ip_token = "5629606"
ip_token_bot_admin = ip_token

bot = telebot.TeleBot("5741977374:AAEc5FVED6rUzoNGVl25wePgoONqz9Ouh-c")
bot_admin = telebot.TeleBot("5741977374:AAEc5FVED6rUzoNGVl25wePgoONqz9Ouh-c")


bot.polling(none_stop=True)
