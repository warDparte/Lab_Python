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
        self.id = id_

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


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
