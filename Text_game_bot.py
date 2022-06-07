from time import sleep
from telebot import types
from config import *
from base_bot import bot

# Text_game_bot
IDLE = 0
LISTENING_TO_COMMANDS = 5
bot_state = IDLE

@bot.message_handler(content_types=['game'])
def send_echo(message):
    m = 0
    while 1:
        if m == 1:
            break
        coins = 100
        house = 100
        farm = 1
        barracks = 1
        barracks1 = 0
        day = 0
        train_farm = 0
        while 1:
            day += 1
            bot.send_message(chat_id=message.from_user.id, text='Day: ' + str(day))
            a = message.text('What do you want to do:build, display data, train, help: ')
            sleep(0.2)
            if house >= 100:
                bot.send_message('You win!')
                win = (message.text('you want to start over?: '))
                if win == 'yes':
                    bot.send_message(chat_id=message.from_user.id, text='You started from the beginning')
                    break
                elif win == 'not':
                    m = 1
                    break
            coins += (farm or farm * train_farm)
            farm1 = house // farm
            barracks1 = house // barracks

            coins1 = coins
            if a == '':
                bot.send_message('1 day has passed')

            elif a == '1':
                b = str(message.text('House,farm,casern: ')).lower()

                if b == ('house' and '1'):
                    coins1 = coins - 50
                    if '-' in str(coins1):
                        bot.send_message('\nNot coins')
                    else:
                        coins -= 50
                        bot.send_message('\nBild house')
                        house += 1

                elif b == ('farm' and '2'):
                    coins1 = coins - 100
                    if '-' in str(coins1):
                        bot.send_message('\nNot coins')
                    if farm > farm1:
                        bot.send_message('\nFew house')
                    else:
                        coins -= 100
                        bot.send_message('\nBild farm')
                        farm += 1

                elif b == ('barracks' and '3'):
                    coins1 = coins - 200
                    if '-' in str(coins1):
                        bot.send_message('\nNot coins')
                    if barracks >= barracks1:
                        bot.send_message('\nFew house')
                    else:
                        coins -= 200
                        bot.send_message('\nBild casern')
                        barracks += 1

            elif a == '2':
                bot.send_message('Coins: ' + str(coins))
                bot.send_message('House: ' + str(house))
                bot.send_message('Farm: ' + str(farm))
                bot.send_message('Casern: ' + str(barracks))
                bot.send_message('Train farm: ' + str(train_farm))

            elif a == '3':
                p = str(message.text('Train:farm:  ')).lower()
                if p == ('farm' and '1'):
                    coins1 = coins - 100
                    if '-' in str(coins1):
                        bot.send_message('\nNot coins')
                    elif train_farm == 10:
                        bot.send_message('Max train farm')
                    elif (train_farm < barracks or train_farm < 10):
                        coins -= 100
                        bot.send_message('\nTrain farm')
                        train_farm += 1
                    else:
                        bot.send_message('Few casern')

            elif a == ('4' and 'help'):
                bot.send_message('Build houses, farms, casern')
                bot.send_message('Improve your farms')
                bot.send_message('And if you have 100 houses you will win')
                bot.send_message('Build(1), display data(2), train(3)')

            else:
                bot.send_message('\nNot command\n')
                coins -= farm
                day -= 1

if __name__ == "__main__":
    from base_bot import main
    main()