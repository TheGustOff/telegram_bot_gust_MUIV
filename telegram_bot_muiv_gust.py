import types

import telebot
import telebot, wikipedia, re
from config import *
from telebot import types

bot = telebot.TeleBot(TOKEN)

'''@bot.message_handler(commands=['get_info', 'info'])
def get_user_info(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text='да', callback_data='yes')
    item_no = types.InlineKeyboardButton(text='нет', callback_data='no')

    markup_inline.add(item_yes, item_no)
    bot.send_message(message.chat.id, 'Желаете узнать информацию о Вас',
        reply_markup=markup_inline
    )

@bot.callback_query_handler(func=lambda call:True)
def answer(call):
    if call.data == 'yes':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_id = types.KeyboardButton('МОЙ ID')
        item_username = types.KeyboardButton('МОЙ НИК')

        markup_reply.add(item_id, item_username)
        bot.send_message(call.message.chat.id, 'Нажмите на одну из кнопок',
            reply_markup=markup_reply
        )
    elif call.data == 'no':
        pass

@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text == 'МОЙ ID':
        bot.send_message(message.chat.id, f'Your ID: {message.from_user.id}')
    elif message.text == 'МОЙ НИК':
        bot.send_message(message.chat.id, f'Your ID: {message.from_user.first_name} {message.from_user.last_name}')'''


# ЭХО-БОТ
'''@bot.message_handler(commands=['start'])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')

@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)'''


# WIKIPEDIA-БОТ
wikipedia.set_lang("ru")
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext=ny.content[:1000]
        wikimas=wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not('==' in x):
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception as e:
        return 'В энциклопедии нет информации об этом'
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))
# Запускаем бота
bot.polling(none_stop=True, interval=0)


////


'''@bot.message_handler(commands=['stop'])
def stop(message):
  if message.from_user.username == cfg.Father:
    pid = str(os.getpid())
    stoper = open('ozerx/stoper.bat', 'w')
    stoper.write("Taskkill /PID " + pid + " /F")
    stoper.close()
    os.system('C:/Users/smp/Desktop/SMP/ozerx/stoper.bat')
  else:
    bot.send_message(message.chat.id, "Ты не Создатель бота; у тебя нет админ-прав, проваливай!")'''


@bot.message_handler(commands=['start'])
def welcome_start(message):
    print(message.from_user)
    bot.send_message(408505187, 'Салам алейкум')
    bot.send_message(message.chat.id, 'Ты быканул шо ли. Молись, что ты мне написал /help', reply_markup=keyboard1)


@bot.message_handler(commands=['help'])
def welcome_help(message):
    print(message.from_user)
    bot.send_message(408505187, 'Hello')
    bot.send_message(message.chat.id, 'Надеюсь, что вы мне написали /start', reply_markup=keyboard1)


keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Привет', 'Пока')
keyboard1.row('/start', '/stop')
keyboard1.row('За', 'Против')
keyboard1.row('Слава', 'России')
keyboard1.row('info')


'''@bot.message_handler(content_types=['sticker'])
def welcome_help(message):
    print(message)'''


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Приветствую тебя, Сталкер!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Да прибудет с тобой Зона!')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMnYl9O36QVjqWTbJy_nR27mFQM5rkAApUAA7AoMgNC_M3XEnpXryQE')
    elif message.text.lower() == 'я тебя не люблю':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMsYl9SSaM2DQdCO_m7Zos4D6U9C2EAAkcBAAKKEqoOPBb4W9tL3GYkBA')
    if message.text.lower() == 'sticker':
        bot.send_sticker(408505187, 'CAACAgIAAxkBAAPCYl9yeHPbMgSiJQOu9eRz4DERQIIAAoUJAAIvD_AG71vanav0H08kBA')
    if message.text.lower() == 'здарова':
        bot.send_message(message.chat.id, 'И тебе здарова')


'''reply_markup=keyboard1'''


@bot.message_handler(content_types=['audio'])
def second(message):
    bot.send_message(message.chat.id, 'Аудио')


@bot.message_handler(content_types=['video'])
def third(message):
    bot.send_message(message.chat.id, 'Видео')


@bot.message_handler(content_types=['document'])
def fourth(message):
    bot.send_message(message.chat.id, 'Документ')


@bot.message_handler(content_types=['photo'])
def fifth(message):
    bot.send_message(message.chat.id, 'Фото')


@bot.message_handler(content_types=['document', 'audio', 'video', 'photo'])
def sixth(message):
    bot.send_message(message.chat.id, 'Всё сразу')



'''@bot.message_handler(content_types=['text'])
def text(message):
    if message.text.lower() == 'sticker':
        bot.send_sticker(408505187, 'CAACAgIAAxkBAAPCYl9yeHPbMgSiJQOu9eRz4DERQIIAAoUJAAIvD_AG71vanav0H08kBA')
    if message.text.lower() == 'здарова':
        bot.send_message(message.chat.id, 'И тебе здарова')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMnYl9O36QVjqWTbJy_nR27mFQM5rkAApUAA7AoMgNC_M3XEnpXryQE')
    elif message.text.lower() == 'я тебя не люблю':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMsYl9SSaM2DQdCO_m7Zos4D6U9C2EAAkcBAAKKEqoOPBb4W9tL3GYkBA')'''


'''@bot.message_handler(content_types=['text'])
def text(message):
    if message.text.lower() == 'здарова':
        bot.send_message(message.chat.id, 'И тебе здарова')'''


'''@bot.message_handler(content_types=['audio'])
def second(message):
    bot.send_message(message.chat.id, 'Аудио')


@bot.message_handler(content_types=['video'])
def third(message):
    bot.send_message(message.chat.id, 'Видео')


@bot.message_handler(content_types=['document'])
def fourth(message):
    bot.send_message(message.chat.id, 'Документ')


@bot.message_handler(content_types=['photo'])
def fifth(message):
    bot.send_message(message.chat.id, 'Фото')


@bot.message_handler(content_types=['document', 'audio', 'video', 'photo'])
def sixth(message):
    bot.send_message(message.chat.id, 'Всё сразу')'''


'''@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)'''


'''keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Привет', 'Пока')
keyboard1.row('/start', '/help')
keyboard1.row('Слава', 'России')'''


'''bot.polling()'''
bot.polling(none_stop=True, interval=0)

