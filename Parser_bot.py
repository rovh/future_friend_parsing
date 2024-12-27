import telebot #импорт pyTelegramBotAPI 
from telebot import types #также достанем типы
import random #рандом обязательно
from Parsing import run_parsing

bot = telebot.TeleBot("7570096229:AAHCI-Da4C6KfyVV2-qwiKMViVlR4S69LXs")

with open('Preview.txt', 'r', encoding='utf-8') as f:
    text = f.read()

@bot.message_handler(commands=['start'])

def main(message):
	
    run_parsing()

    bot.send_message(message.chat.id, text)

bot.polling(non_stop=True)
