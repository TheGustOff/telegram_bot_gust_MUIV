from telebot import types
import telebot, wikipedia, re
from config import *
from base_bot import bot

# Dialog_bot
IDLE = 0
LISTENING_TO_COMMANDS = 2
bot_state = IDLE

'''@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")'''

name = ''
surname = ''
age = 0
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')

def get_name(message): #получаем фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname;
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
    keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes') #кнопка «Да»
    keyboard.add(key_yes); #добавляем кнопку в клавиатуру
    key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no);
    question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
        ... #код сохранения данных, или их обработки
        bot.send_message(call.message.chat.id, 'Запомню : )');
    elif call.data == "no":
         ... #переспрашиваем

@bot.message_handler(commands=['stop'])
def stop(m, res=False):
    global bot_state
    bot_state = IDLE


keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('/wiki', '/stop')

if __name__ == "__main__":
    from base_bot import main
    main()


'''bot.polling(none_stop=True, interval=0)'''

''''@bot.callback_query_handler(func=lambda call: True)
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

keyboard1 = types.InlineKeyboard1Markup(); #наша клавиатура
key_yes = types.InlineKeyboard1Button(text='Да', callback_data='yes'); #кнопка «Да»
keyboard1.add(key_yes); #добавляем кнопку в клавиатуру
key_no= types.InlineKeyboard1Button(text='Нет', callback_data='no');
keyboard1.add(key_no);
question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?';
bot.send_message(message.from_user.id, text=question, reply_markup=keyboard1)'''