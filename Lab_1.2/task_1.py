import doctest
from typing import Union, Optional


LOWER_LIMIT_CHLORINE_NORM = 0.035  # Нижняя допустимая граница хлора в бассейне (литры/кубометры)
UPPER__LIMIT_CHLORINE_NORM = 0.045  # Верхняя допустимая граница хлора в бассейне (литры/кубометры)


class Table:
    def __init__(self, length: Union[int, float], width: Union[int, float], height: Union[int, float], obj: Optional[str]=None):
        """
    Создание и подготовка к работе объекта "Стол"

    :param: table_length: Длинна стола
    :param: table_width: Ширина стола
    :param: table_height: Высота стола
    :param: obj: список объектов на столе

    Примеры:
    >>> table_1 = Table(100, 120, 120) # инициализация экземпляра класса
        """

        if not isinstance(length, (int, float)):
            raise TypeError("Неверный тип данных")
        if not length > 0:
            raise ValueError("Значение должно быть положительным")
        self.table_length = length

        if not isinstance(width, (int, float)):
            raise TypeError("Неверный тип данных")
        if not width > 0:
            raise ValueError("Значение должно быть положительным")
        self.table_width = width

        if not isinstance(height, (int, float)):
            raise TypeError("Неверный тип данных")
        if not height > 0:
            raise ValueError("Значение должно быть положительным")
        self.table_height = height

        if not isinstance(obj, Optional[str]):
            raise TypeError("Предмет должен быть описан 'str' или None")
        self.obj = obj


    def object_on_the_table(self) -> bool:
        """
    Функция проверяет есть ли на столе предметы

    :return: есть ли на столе предметы

    Примеры:
    >>> table_1 = Table(100, 120, 120, 'кружка')
    >>> table_1.object_on_the_table() # TODO не могу понять как сделать так, чтобы интерпретатор не ругался. Подскажите, как можно исправить?
    """
        return False if self.obj is None else True


    def add_obj(self, add_obj: Optional[str]) -> None:
        """
    Функция ставит предмет на стол

    :param: add_obj: объект, который ставим на стол

    Примеры:
    >>> table_2 = Table(10, 10, 10)
    >>> table_2.add_obj('кружка')
    """
        if not isinstance(add_obj, Optional[str]):
            raise TypeError("Предмет описывается 'str'")
        self.obj = add_obj


class Pool:
    def __init__(self, capacity_pool: Union[int, float], occupied_pool: Union[int, float], chlorine: Union[int, float]):
        """
    Создание и подготовка к работе объекта "Бассейн"

    :param: capacity_pool: Объем бассейна в кубометрах
    :param: occupied_pool: Объем воды в бассейн в кубометрах
    :param: chlorine: Количество хлорки в бассейне в литрах

    :raise ValueError: Если количество хлора в бассейне ниже или выше нормы

    Примеры:
     >>> pool_1 = Pool(1000, 900, 31.5)# инициализация экземпляра класса
        """

        if not isinstance(capacity_pool, (int, float)):
            raise TypeError("Неверный тип данных")
        if not capacity_pool > 0:
            raise ValueError("Значение должно быть положительным")
        if capacity_pool < occupied_pool:
            raise ValueError("Объем бассейна не может быть меньше объема воды в бассейне")
        self.capacity_pool = capacity_pool

        if not isinstance(occupied_pool, (int, float)):
            raise TypeError("Неверный тип данных")
        if not occupied_pool > 0:
            raise ValueError("Значение должно быть положительным")
        if occupied_pool > capacity_pool:
            raise ValueError("Объем воды в бассейне не может быть больше объема бассейна")
        self.occupied_pool = occupied_pool

        if not isinstance(chlorine, (int, float)):
            raise TypeError("Неверный тип данных")
        if not chlorine > 0:
            raise ValueError("Значение должно быть положительным")
        if chlorine / occupied_pool < LOWER_LIMIT_CHLORINE_NORM:
            raise ValueError("Недостаточное количество хлора для оптимальной обработки бассейна")
        if chlorine / occupied_pool > UPPER__LIMIT_CHLORINE_NORM:
            raise ValueError("Избыточное количество хлора, опасно для жизни!")
        self.chlorine = chlorine

    def add_water_to_pool(self, water: Union[int, float]) -> None:
        """
        Функция добавляет воды в бассейн

        :param water: Объем добавляемой жидкости

        :raise ValueError: Если объем жидкости превышает объем бассейна

        Пример:
        >>> pool_2 = Pool(1000, 900, 31.5)
        >>> pool_2.add_water_to_pool(100)
        """
        if not isinstance(water, Union[int, float]):
            raise TypeError("Неверный тип данных")
        if water + self.occupied_pool > self.capacity_pool:
            raise ValueError("Невозможно залить воды больше объема бассейна")
        self.occupied_pool += water


    def del_water_in_pool(self) -> None:
        """

        :return: Сливает всю воду с бассейна

        :raise ValueError: Если в бассейне нет воды

        Пример:
        >>> pool_3= Pool(1000, 900, 31.5)
        >>> pool_3.del_water_in_pool()
        """
        self.occupied_pool = 0


class Messenger:
    def __init__(self, chats: list[dict[int, str]], unread_chat: list[dict[int, str]], new_message: Optional[str]=None):
        """
        Создание и подготовка к работе объекта "Мессенджер"

        :param chats: список чатов [{порядковый номер сообщения в чате, текст сообщения}, ...]
        :param unread_chat: количество чатов с новыми сообщениями
        :param new_message: текст в строке отправки сообщения

        Примеры:
        >>> peter_petrov = {1: "Привет!", 2: "Сделал лабораторную?", 3: "Дай списать :)"} # чат с прочитанными сообщениями
        >>> ivan_ivanov = {187: "Привет! Петя тоже тебе пишет?"} # чат с новым сообщение
        >>> chat_list = [peter_petrov, ivan_ivanov, ...] # список всех чатов
        >>> new_message_list = [ivan_ivanov, ...] # список чатов с новыми сообщениями
        >>> mess_1 = Messenger(chat_list, new_message_list)
        """

        if not isinstance(chats, list):
            raise TypeError("Неверный тип данных")
        self.chats = chats

        if not isinstance(unread_chat, list):
            raise TypeError("Неверный тип данных")
        self.unread_chat = unread_chat

        if not isinstance(new_message, Optional[str]):
            raise TypeError("Неверный тип данных")
        self.new_message = new_message

    def value_of_unread_chat(self) -> int:
        """
        Функция считает количество чатов с новыми сообщениями

        :return: Возвращает количество чатов с новыми сообщениями

        Пример:
        >>> peter_petrov = {1: "Привет!", 2: "Сделал лабораторную?", 3: "Дай списать :)"} #
        >>> ivan_ivanov = {187: "Привет! Петя тоже тебе пишет?"} # чат с новым сообщение
        >>> anonymous = {1: "Привет! Слышал что-то про ГДЗ?"} # чат с новым сообщение
        >>> chat_list = [peter_petrov, ivan_ivanov, anonymous, ...] # список всех чатов
        >>> new_message_list = [ivan_ivanov, anonymous, ...] # список чатов с новыми сообщениями
        >>> mess_2 = Messenger(chat_list, new_message_list)
        """

        return len(self.unread_chat)


    def value_of_unread_message(self, chat: dict[int, str]) -> int:
        """
        Функция считает количество новых сообщений в чате

        :param chat: чат с новыми сообщениями

        :return: количество новых сообщений в чате

        Примеры:

        """
        ...

    def enter_message(self, new_message) -> None:
        """
        Функция вводит текст в строку отправки сообщения

        :param new_message: текст нового сообщения

        Примеры:
        >>> peter_petrov = {...} # чат с прочитанными сообщениями
        >>> ivan_ivanov = {...} # чат с новым сообщение
        >>> chat_list = [peter_petrov, ivan_ivanov, ...] # список всех чатов
        >>> new_message_list = [ivan_ivanov, ...] # список чатов с новыми сообщениями
        >>> new_mess = "Петя, привет! Давай я лучше объясню как решить лабораторную." # Текст нового сообщения
        >>> mess_3 = Messenger(chat_list, new_message_list)
        >>> mess_3.enter_message(new_mess)
        """

        if not isinstance(new_message, str):
            raise TypeError("Неверный тип данных")
        self.new_message = new_message


if __name__ == "__main__":
    doctest.testmod()
    pass
