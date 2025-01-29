class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        if not isinstance(name, str):
            raise TypeError('Неверный тип данных')
        self._name = name
        if not isinstance(author, str):
            raise TypeError('Неверный тип данных')
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author


class PaperBook(Book):
    """Класс бумажной книги"""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError('Неверный тип данных')
        if not pages >= 0:
            raise ValueError('Значение должно быть положительным')
        self._pages = pages

    def __str__(self):
        return f"Бумажная книга {self._name}. Автор {self._author}. Кол-во страниц: {self._pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages})"

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages):
        if not isinstance(new_pages, int):
            raise TypeError('Неверный тип данных')
        if not new_pages >= 0:
            raise ValueError('Значение должно быть положительным')
        self._pages = new_pages


class AudioBook(Book):
    """Класс аудиокниги"""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    def __str__(self):
        return f"Аудио книга {self._name}. Автор {self._author}. Продолжительность: {self._duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration})"

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration):
        if not isinstance(new_duration, float):
            raise TypeError('Неверный тип данных')
        if not new_duration >= 0:
            raise ValueError('Значение должно быть положительным')
        self._duration = new_duration
