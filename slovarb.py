from __future__ import annotations # В дальнейшем я буду опускать этот импорт
from loguru import logger

import inspect
import functools
import os

def file_is_empty(path: str) -> bool:
    return os.stat(path).st_size == 0

def clear_file(path: str) -> None:
    with open(path, 'w'): pass

def cache_decorator(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        res = method(self, *args, **kwargs)
        Cache.link.recess(self, {'method_name': method.__name__}) # (1)
        # В процессе тестирования множественные вызовы могут замедлять
        # работу программы; opt позволяет избежать этого
        logger.opt(lazy=True).debug(f'Decorator for {method.__name__} was end')
        return res
    return wrapper

@cache_decorator
def add_smth_important(*args, **kwargs) -> Any:
    # ...
    # Производим какие-то важные действия над данными...
    # ...

class Cache:
    """
    + cache_size  - Шаг, через который будет происходить сохранение всех данных
    + cache_files - Файл дампов, в котором сохраняются все промежуточные операции над данными
    """

    link = None

    def __init__(self, cache_size=10):
        # Сохраняем все прикрученные классы. Это позволяет гибко работать с данными
        self._classes = []
        # Файлы, соответствующие классам
        self._cache_files = []
        # (1): Небольшой хак, который позволяет вызвать конкретный экземпляр через общий класс
        # Это работает, потому что у нас есть всего один экземпляр класса, который
        # реализует всю логику работы с данными. К тому же, это удобно и позволяет
        # значительно расширить функционал в будущем
        self.__class__.link = self

        self._counter = 0
        self.CACHE_SIZE = cache_size

    def add(self, cls: class, file: str) -> None:
        """
        Позволяет прикрутить класс к сейверу

        + cls  - Экземпляр класса
        + file - Файл, с которым работает экземпляр
        """

        self._cache_files.append(file)
        self._classes.append(cls)

        if file_is_empty(file): return None

        logger.opt(lazy=True).debug(f'For {cls.__class__.__name__} file {file} is not empty')

        for data in self.load(file):
            cls.save_non_caching(data)

        clear_file(file)
        self._counter = 0

    def recess(self, cls: class, data: dict) -> None:
        """
        Основной метод, выполняющий основную логику сейвов
        """

        if self._counter + 1 >= self.CACHE_SIZE:
            self.save_all()
        else:
            self._counter += 1
            filename = self._cache_files[self._classes.index(cls)]
            self.save(data, filename=filename)

    # ...
    # Для простоты методы save_all, save, load опущены
    # ...