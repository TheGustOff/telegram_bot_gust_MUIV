from telebot import types
import telebot, wikipedia, re
from config import *
from base_bot import bot


item_yes = types.InlineKeyboardButton(text='да', callback_data='yes')
item_no = types.InlineKeyboardButton(text='нет', callback_data='no')
IDLE = 0
LISTENING_TO_COMMANDS = 2
bot_state = IDLE


@bot.message_handler(commands=['get_info', 'info'])
def get_user_info(message):
    global bot_state
    bot_state = LISTENING_TO_COMMANDS
    markup_inline = types.InlineKeyboardMarkup()
    markup_inline.add(item_yes, item_no)
    bot.send_message(message.chat.id, 'Желаете узнать информацию о Вас',
        reply_markup=markup_inline
    )

@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    print(call)
    if call.data == 'yes':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item_id = types.KeyboardButton('МОЙ ID')
        item_username = types.KeyboardButton('МОЙ НИК')
        markup_reply.add(item_id, item_username)
        bot.send_message(call.message.chat.id, 'Нажмите на одну из кнопок',
            reply_markup=markup_reply
        )
    elif call.data == 'no':
        pass


@bot.message_handler(commands=['stop'])
def stop(m, res=False):
    global bot_state
    bot_state = IDLE

def get_text(message):
    if bot_state != IDLE:
        if message.text == 'МОЙ ID':
            bot.send_message(message.chat.id, f'Your ID: {message.from_user.id}')
        elif message.text == 'МОЙ НИК':
            bot.send_message(message.chat.id, f'Your ID: {message.from_user.first_name} {message.from_user.last_name}')


if __name__ == "__main__":
    from base_bot import main
    main()
