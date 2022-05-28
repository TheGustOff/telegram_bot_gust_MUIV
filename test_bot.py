from telebot import types
import telebot, wikipedia, re
from config import *
from base_bot import bot

# Test-bot
IDLE = 0
LISTENING_TO_COMMANDS = 2
bot_state = IDLE

@bot.message_handler(commands=['test'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Три', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='Четыре', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(text='Пять', callback_data=5))
    bot.send_message(message.chat.id, text="Какая средняя оценка была у Вас в школе?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за честный ответ!')
    answer = ''
    if call.data == '3':
        answer = 'Вы троечник!'
    elif call.data == '4':
        answer = 'Вы хорошист!'
    elif call.data == '5':
        answer = 'Вы отличник!'

    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

@bot.message_handler(commands=['stop'])
def stop(m, res=False):
    global bot_state
    bot_state = IDLE

def handle_text(message):
    if bot_state != IDLE:
        bot.send_message(message.chat.id, getwiki(message.text), reply_markup=keyboard1)

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('/test', '/stop')

if __name__ == "__main__":
    from base_bot import main
    main()