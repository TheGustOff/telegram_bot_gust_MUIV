from telebot import types
import telebot, wikipedia, re
from config import *
from base_bot import bot

# WIKIPEDIA-БОТ
IDLE = 0
LISTENING_TO_COMMANDS = 2
bot_state = IDLE

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

@bot.message_handler(commands=['wiki'])
def wiki(m, res=False):
    global bot_state
    bot_state = LISTENING_TO_COMMANDS
    bot.send_message(m.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia', reply_markup=keyboard1)

@bot.message_handler(commands=['stop'])
def stop(m, res=False):
    global bot_state
    bot_state = IDLE

def handle_text(message):
    if bot_state != IDLE:
        bot.send_message(message.chat.id, getwiki(message.text), reply_markup=keyboard1)


keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('/wiki', '/stop')

if __name__ == "__main__":
    from base_bot import main
    main()
