from config import *
import telebot
bot = telebot.TeleBot(TOKEN)

def main():
    bot.polling(none_stop=True, interval=0)

# @bot.message_handler(content_types=['text'])

def text_handlers(*handlers):
    for handler in handlers:
        bot.message_handler(content_types=['text'])(handler)

if __name__ == "__main__":
    main()
