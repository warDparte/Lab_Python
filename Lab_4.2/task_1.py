from typing import Union


class Phone:
    def __init__(self, model: str, manufacturer: str, operatorr: str):
        """
        Инициализация объекта Телефон
        :param model: Модель
        :param manufacturer: Производитель
        :operator: Оператор связи
        """
        if not isinstance(model, str):
            raise TypeError('Неверный тип данных')
        self.model = model

        if not isinstance(manufacturer, str):
            raise TypeError('Неверный тип данных')
        self.manufacturer = manufacturer

        if not isinstance(operatorr, str):
            raise TypeError('Неверный тип данных')
        self.operatorr = operatorr

    def __str__(self) -> str:
        return f'Телефон {self.manufacturer}, модель: {self.model}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(model={self.model}, manufacturer={self.manufacturer})'

    def call(self, number) -> None:
        """
        Функция выполняющая соединение по проводной связи
        :return: Выполняет соединение
        """
        ...

    def end_the_call(self) -> None:
        """
        Функция прекращающая соединение
        :return: прекращает соединение
        """
        ...


class Smartphone(Phone):
    def __init__(self, model: str, manufacturer: str, operatorr: str, diagonal: Union[int, float], memory: int):
        """
        Инициализация объекта Смартфон
        :param model: Модель
        :param manufacturer: Производитель
        :param diagonal: Диагональ экрана
        :param memory: Встроенная память устройства в ГигаБайтах
        """
        super().__init__(model, manufacturer, operatorr)

        if not isinstance(diagonal, Union[int, float]):
            raise TypeError('Неверный тип данных')
        if diagonal <= 0:
            raise ValueError('Значение диагонали должно быть положительным')
        self.diagonal = diagonal

        if not isinstance(memory, int):
            raise TypeError('Неверный тип данных')
        if memory < 0:
            raise ValueError('Объем памяти не может быть отрицательным')
        self.memory = memory

    def __str__(self) -> str:
        return f'Смартфон {self.manufacturer}, модель: {self.model}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(model={self.model}, manufacturer={self.manufacturer}, diagonal={self.diagonal}, memory={self.memory})'

    def call(self, number) -> None:
        """
        Функция выполняющая соединение по сотовой связи
        :return: Выполняет соединение
        """
        ...


if __name__ == "__main__":
    phone = Phone('3310', 'NOKIA', 'Мегафон')
    print(phone)
    smartphone = Smartphone('iPhone 16', 'Apple', 'Билайн', 5.9, 256)
    print(smartphone)
    pass
