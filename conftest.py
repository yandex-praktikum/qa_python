import pytest

from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()
