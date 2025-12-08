import pytest
from main import BooksCollector


# ---------- Тесты для добавления книг ----------

@pytest.mark.parametrize('book_name', ['Книга 1', 'Очень важная книга'])
def test_add_new_book_adds_book_without_genre(book_name):
    collector = BooksCollector()

    collector.add_new_book(book_name)

    books = collector.get_books_genre()
    assert book_name in books
    # у только что добавленной книги жанр — пустая строка
    assert books[book_name] == ''


def test_add_new_book_does_not_add_book_with_name_longer_than_40():
    collector = BooksCollector()
    long_name = 'А' * 41  # 41 символ

    collector.add_new_book(long_name)

    books = collector.get_books_genre()
    assert long_name not in books


def test_add_new_book_does_not_add_duplicate_book():
    collector = BooksCollector()
    book_name = 'Гарри Поттер'

    collector.add_new_book(book_name)
    collector.add_new_book(book_name)

    books = collector.get_books_genre()
    # одна и та же книга должна быть только один раз
    assert list(books.keys()).count(book_name) == 1


# ---------- Тесты для установки и получения жанра ----------

def test_set_book_genre_sets_genre_for_existing_book():
    collector = BooksCollector()
    book_name = 'Безобидная книга'
    collector.add_new_book(book_name)

    any_genre = collector.genre[0]
    collector.set_book_genre(book_name, any_genre)

    assert collector.get_book_genre(book_name) == any_genre


def test_set_book_genre_does_not_set_genre_for_unknown_book():
    collector = BooksCollector()
    unknown_book = 'Неизвестная книга'
    any_genre = collector.genre[0]

    collector.set_book_genre(unknown_book, any_genre)

    books = collector.get_books_genre()
    assert unknown_book not in books


def test_get_book_genre_returns_empty_string_for_book_without_genre():
    collector = BooksCollector()
    book_name = 'Книга без жанра'
    collector.add_new_book(book_name)

    assert collector.get_book_genre(book_name) == ''


# ---------- Тесты для получения книг по жанрам ----------

def test_get_books_with_specific_genre_returns_only_books_with_that_genre():
    collector = BooksCollector()
    safe_genre = collector.genre[0]
    other_genre = collector.genre[1]

    collector.add_new_book('Книга 1')
    collector.set_book_genre('Книга 1', safe_genre)

    collector.add_new_book('Книга 2')
    collector.set_book_genre('Книга 2', other_genre)

    books = collector.get_books_with_specific_genre(safe_genre)

    assert 'Книга 1' in books
    assert 'Книга 2' not in books


def test_get_books_for_children_includes_safe_genre():
    collector = BooksCollector()
    safe_genre = next(
        genre for genre in collector.genre
        if genre not in collector.genre_age_rating
    )

    collector.add_new_book('Детская книга')
    collector.set_book_genre('Детская книга', safe_genre)

    children_books = collector.get_books_for_children()

    assert 'Детская книга' in children_books


def test_get_books_for_children_excludes_age_rating():
    collector = BooksCollector()
    age_genre = collector.genre_age_rating[0]

    collector.add_new_book('Взрослая книга')
    collector.set_book_genre('Взрослая книга', age_genre)

    children_books = collector.get_books_for_children()

    assert 'Взрослая книга' not in children_books


# ---------- Тесты для избранного ----------

def test_add_book_in_favorites_adds_only_existing_book_and_ignores_duplicates():
    collector = BooksCollector()
    book_name = 'Любимая книга'

    collector.add_new_book(book_name)

    collector.add_book_in_favorites(book_name)
    collector.add_book_in_favorites(book_name)  # в избранном она должна остаться одна

    favorites = collector.get_list_of_favorites_books()

    assert book_name in favorites
    assert favorites.count(book_name) == 1


def test_add_book_in_favorites_does_not_add_book_which_is_not_in_books_genre():
    collector = BooksCollector()
    unknown_book = 'Неизвестная книга'

    collector.add_book_in_favorites(unknown_book)

    favorites = collector.get_list_of_favorites_books()
    assert unknown_book not in favorites


def test_delete_book_from_favorites_removes_book():
    collector = BooksCollector()
    book_name = 'Книга для удаления'

    collector.add_new_book(book_name)
    collector.add_book_in_favorites(book_name)

    collector.delete_book_from_favorites(book_name)

    favorites = collector.get_list_of_favorites_books()
    assert book_name not in favorites


def test_get_list_of_favorites_books_returns_correct_list():
    collector = BooksCollector()

    collector.add_new_book('Азбука')
    collector.add_new_book('Алгебра')

    collector.add_book_in_favorites('Азбука')
    collector.add_book_in_favorites('Алгебра')

    assert collector.get_list_of_favorites_books() == ['Азбука', 'Алгебра']

