from telebot import types
import telebot, wikipedia, re
from config import *

bot = telebot.TeleBot(TOKEN)

# ЭХО-БОТ
IDLE = 0
LISTENING_TO_COMMANDS = 1
bot_state = IDLE

@bot.message_handler(commands=['start'])
def start(m, res=False):
    print("qq")
    global bot_state
    bot_state = LISTENING_TO_COMMANDS
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')

@bot.message_handler(commands=['stop'])
def stop(m, res=False):
    global bot_state
    bot_state = IDLE

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if bot_state != IDLE:
        bot.send_message(message.chat.id, 'Вы написали: ' + message.text)


bot.polling(none_stop=True, interval=0)

