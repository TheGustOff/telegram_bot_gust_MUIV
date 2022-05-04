from telebot import types
import telebot, wikipedia, re
from config import *
from base_bot import bot

# ЭХО-БОТ
IDLE = 0
LISTENING_TO_COMMANDS = 1
bot_state = IDLE

@bot.message_handler(commands=['start'])
def start(message):
    global bot_state
    bot_state = LISTENING_TO_COMMANDS
    bot.send_message(message.chat.id, 'Я на связи. Напиши мне что-нибудь )', reply_markup=keyboard1)

@bot.message_handler(commands=['stop'])
def stop(message):
    global bot_state
    bot_state = IDLE

def handle_text(message):
    if bot_state != IDLE:
        bot.send_message(message.chat.id, 'Вы написали: ' + message.text)


keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('/start', '/stop')

if __name__ == "__main__":
    from base_bot import main
    main()

