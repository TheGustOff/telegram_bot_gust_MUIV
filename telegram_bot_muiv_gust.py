import telebot
from config import *

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome_start(message):
    print(message.from_user)
    bot.send_message(408505187, 'Салам алейкум')
    bot.send_message(message.chat.id, 'Ты быканул шо ли. Молись, что ты мне написал /help', reply_markup=keyboard1)


@bot.message_handler(commands=['help'])
def welcome_help(message):
    print(message.from_user)
    bot.send_message(408505187, 'Hello')
    bot.send_message(message.chat.id, 'Или мне показалось. Надеюсь, что ты мне написал /start', reply_markup=keyboard1)


'''@bot.message_handler(content_types=['sticker'])
def welcome_help(message):
    print(message)'''


@bot.message_handler(content_types=['text'])
def text(message):
    if message.text.lower() == 'sticker':
        bot.send_sticker(408505187, 'CAACAgIAAxkBAAPCYl9yeHPbMgSiJQOu9eRz4DERQIIAAoUJAAIvD_AG71vanav0H08kBA')


@bot.message_handler(content_types=['text'])
def text(message):
    if message.text.lower() == 'здарова':
        bot.send_message(message.chat.id, 'И тебе здарова')


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


'''@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)'''


keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Чё по чём', 'Ну бывай')
keyboard1.row('1337', '1488')
keyboard1.row('Слава', 'России')


bot.polling()
