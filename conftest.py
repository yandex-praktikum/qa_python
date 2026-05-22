import pytest

from main import BooksCollector

@pytest.fixture
def books_collector():
    books_collector = BooksCollector()
    books_collector.add_new_book('Книга')
    return books_collector
