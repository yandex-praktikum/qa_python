import pytest
from qa_python.main import BooksCollector


@pytest.fixture
def books_collector():
    return BooksCollector()


# add_new_book — книга добавляется в коллекцию
def test_add_new_book_adds_book_to_collection(books_collector):
    books_collector.add_new_book('Властелин колец')
    assert 'Властелин колец' in books_collector.get_books_genre()


# add_new_book — новая книга добавляется без жанра
def test_add_new_book_has_empty_genre_by_default(books_collector):
    books_collector.add_new_book('Дюна')
    assert books_collector.get_book_genre('Дюна') == ''


# add_new_book — книга с названием > 40 символов не добавляется
def test_add_new_book_with_long_name_is_not_added(books_collector):
    long_name = 'А' * 41
    books_collector.add_new_book(long_name)
    assert long_name not in books_collector.get_books_genre()


# set_book_genre + get_book_genre — жанр устанавливается корректно
def test_set_and_get_book_genre_returns_correct_genre(books_collector):
    books_collector.add_new_book('Матрица')
    books_collector.set_book_genre('Матрица', 'Фантастика')
    assert books_collector.get_book_genre('Матрица') == 'Фантастика'


# set_book_genre — жанр не из списка не устанавливается
def test_set_book_genre_not_from_allowed_list_is_not_set(books_collector):
    books_collector.add_new_book('Оно')
    books_collector.set_book_genre('Оно', 'Роман')
    assert books_collector.get_book_genre('Оно') == ''


# get_books_with_specific_genre — возвращаются книги нужного жанра
def test_get_books_with_specific_genre_returns_correct_books(books_collector):
    books_collector.add_new_book('Чужой')
    books_collector.set_book_genre('Чужой', 'Ужасы')

    books_collector.add_new_book('Назад в будущее')
    books_collector.set_book_genre('Назад в будущее', 'Фантастика')

    assert books_collector.get_books_with_specific_genre('Ужасы') == ['Чужой']


# get_books_for_children — книги с возрастным рейтингом исключаются
def test_get_books_for_children_excludes_age_restricted_genres(books_collector):
    books_collector.add_new_book('Оно')
    books_collector.set_book_genre('Оно', 'Ужасы')

    books_collector.add_new_book('Король Лев')
    books_collector.set_book_genre('Король Лев', 'Мультфильмы')

    assert books_collector.get_books_for_children() == ['Король Лев']


# add_book_in_favorites — книга добавляется в избранное
def test_add_book_in_favorites_adds_book(books_collector):
    books_collector.add_new_book('Интерстеллар')
    books_collector.add_book_in_favorites('Интерстеллар')
    assert 'Интерстеллар' in books_collector.get_list_of_favorites_books()


# add_book_in_favorites — книга не добавляется повторно
def test_add_book_in_favorites_does_not_duplicate(books_collector):
    books_collector.add_new_book('Гарри Поттер')
    books_collector.add_book_in_favorites('Гарри Поттер')
    books_collector.add_book_in_favorites('Гарри Поттер')
    assert books_collector.get_list_of_favorites_books().count('Гарри Поттер') == 1


# delete_book_from_favorites — книга удаляется из избранного
def test_delete_book_from_favorites_removes_book(books_collector):
    books_collector.add_new_book('Аватар')
    books_collector.add_book_in_favorites('Аватар')
    books_collector.delete_book_from_favorites('Аватар')
    assert 'Аватар' not in books_collector.get_list_of_favorites_books()
