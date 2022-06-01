from loguru import logger
import sys
# Импортируем основной класс
from modules import EnglishBot
# Импортируем классы, которые реализуют Telegram-команды
from modules.module import start
# ...
from telegram.ext import CommandHandler

def a(self, key: str):
    # Сначала проверяем нет ли необходимого значения у класса
    # Если нет, то пытаемся вернуть его из chat_data
    try:
        return object.__getattribute__(self, key)
    except:
        return self.chat_data[key]

def b(self, key: str, data=None, replace=True):
    # Небольшой хак: если replace=False и данные существуют, то перезапись не происходит
    # При этом, если данные не указаны, то они ставятся в None
    if replace or not self.chat_data.get(key, None):
        self.chat_data[key] = data

# Биндим context, чтобы получать данные в формате context.data
CallbackContext.__getattribute__ = a
# А также удобный сеттер для своих нужд
CallbackContext.set = b

if __name__ == '__main__':
    # Инициализируем бота
    tbot = EnglishBot(
        # ...
    )

    # Добавляем обработчики в стек
    tbot.add_command_handler(start, 'start')
    # ...

# Настраиваем двухпоточный вывод: в консоль и в файл
config = {
    'handlers': [
        {'sink': sys.stdout, 'level': 'INFO'},
        {'sink': 'logs.log', 'serialize': False, 'level': 'DEBUG'},
    ],
}

logger.configure(**config)

# ...

updater = Updater('YOUR_TOKEN')
dp = updater.dispatcher

# Грубо прикручиваем свой логгер. Дешево и сердито
updater.logger = logger
dp.logger = logger