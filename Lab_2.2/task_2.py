from typing import Optional


BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: str):
        """
        Создание и подготовка к работе объекта "Книга"
        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        """
        if not isinstance(id_, int):
            raise TypeError('Неверный тип данных')
        if id_ <= 0:
            raise ValueError('Значение должно быть положительным')
        self.id_ = id_

        if not isinstance(name, str):
            raise TypeError('Неверный тип данных')
        self.name = name

        if not isinstance(pages, int):
            raise TypeError('Неверный тип данных')
        if pages <= 0:
            raise ValueError('Значение не может быть отрицательным')
        self.pages = pages


    def __str__(self) -> str:
        return f'Книга "{self.name}"'


    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(id_={self.id}, name={self.name!r}, pages={self.pages})'

# TODO написать класс Library
class Library:
    def __init__(self, books: Optional[list[Book]] = []):
        """
        Создание и подготовка к работе объекта "Библиотека"
        :param books: Список книг
        """
        if not isinstance(books, list):
            raise TypeError('Ожидался список книг')
        self.books = books


    def __str__(self):
        list_library = [v.name for i,v in enumerate(self.books)]
        return f'Библиотека книг: {list_library}'


    def __repr__(self):
        return f'{self.__class__.__name__}(books={self.books})'


    def get_next_book_id(self):
        """
        Метод, возвращающий идентификатор для добавления новой книги в библиотеку
        :return: Идентификатор для добавления новой книги в библиотеку
        """
        actual_id = len(self.books)
        next_id = actual_id + 1
        return next_id


    def get_index_by_book_id(self, id_):
        """
        Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса
        :param id_: Идентификатор книги
        :return: Индекс книги в списке
        """
        for i, v in enumerate(self.books):
            if id_ == v.id_:
                return i
            else:
                raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
