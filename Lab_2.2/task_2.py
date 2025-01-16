from typing import Optional
from pydantic import BaseModel, Field

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
class Book(BaseModel):
    """
    :param id_: Идентификатор книги
    :param name: Название книги
    :param pages: Количество страниц в книге
    """
    id_: int = Field(gt=0)
    name: str
    pages: int = Field(gt=0)


# TODO написать класс Library
class Library(BaseModel):
    """
    :param books: Список книг
    """
    books: Optional[list[Book]] = Field(default=[])


    def get_next_book_id(self):
        """
        Метод, возвращающий идентификатор для добавления новой книги в библиотеку.

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
