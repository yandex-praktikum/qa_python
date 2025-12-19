import pytest
from main import BooksCollector
from books_data import BOOK_WITH_GENRE


@pytest.fixture
def collector_with_books():
    collector = BooksCollector()
    for name, genre in BOOK_WITH_GENRE:
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    return collector