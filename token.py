import telebot
from telebot import types

ip_token = "5629606"
ip_token_bot_admin = ip_token

bot = telebot.TeleBot("55800830WTE8OMIZTk")
bot_admin = telebot.TeleBot("5580083308:AAG0")


bot.polling(none_stop=True)
