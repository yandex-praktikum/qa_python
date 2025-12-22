import pytest
from main import BooksCollector
from books_data import BOOK_WITH_GENRE


# Фикстура для создания пустого эксземпляра BooksCollector
@pytest.fixture
def collector():
    return BooksCollector()

# Фикстура для создания экземпляра BooksCollector с предзаполненными книгами и жанрами
@pytest.fixture
def collector_with_books(collector):
    for name, genre in BOOK_WITH_GENRE:
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    return collector