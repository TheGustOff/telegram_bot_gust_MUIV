from config import *
import telebot
bot = telebot.TeleBot(TOKEN)
text_handlers = None


def main(*new_text_handlers):
    global text_handlers

    def handle_text(message):
        for handler in text_handlers:
            handler(message)

    text_handlers = new_text_handlers
    bot.message_handler(content_types=['text'])(handle_text)
    bot.polling(none_stop=True, interval=0)

# @

def text_handlers():
    for handler in handlers:
        bot.message_handler(content_types=['text'])(handler)

if __name__ == "__main__":
    main()
