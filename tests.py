import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_added_successfully(self, collector):
        collector.add_new_book('Властелин колец')
        assert 'Властелин колец' in collector.get_books_genre()

    @pytest.mark.parametrize('name, expected', [
    ('А' * 40, True),   # граница — должна добавиться
    ('А' * 41, False),  # за границей — не должна
    ('Властелин колец',   True),   # обычное название
    ('',       False),  # пустое — не должна
])
    def test_add_new_book_parametrized(self, collector, name, expected):
        collector.add_new_book(name)
        assert (name in collector.get_books_genre()) == expected

    def test_add_new_book_empty_name_not_added(self, collector):
        collector.add_new_book('')
        assert '' not in collector.get_books_genre()

    def test_add_new_book_duplicate_not_added_twice(self, collector):
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Властелин колец')
        assert len(collector.get_books_genre()) == 1

    def test_get_book_genre_returns_genre(self, collector):
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        assert collector.get_book_genre('Властелин колец') == 'Фантастика'   
         
    def test_add_new_book_default_genre_is_empty_string(self, collector):
        collector.add_new_book('Властелин колец')
        assert collector.get_book_genre('Властелин колец') == ''

    def test_set_book_genre_sets_correctly(self, collector):
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        assert collector.get_book_genre('Властелин колец') == 'Фантастика'

    def test_set_book_genre_not_set_if_book_missing(self, collector):
        collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert collector.get_book_genre('Несуществующая книга') is None

    def test_set_book_genre_not_set_if_genre_not_in_list(self, collector):
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Романтика')
        assert collector.get_book_genre('Властелин колец') == ''

    def test_get_book_genre_returns_empty_string_if_genre_not_set(self, collector):
        collector.add_new_book('Властелин колец')
        assert collector.get_book_genre('Властелин колец') == ''        

    def test_get_books_with_specific_genre_returns_correct_books(self, collector):
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Мартин Иден')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.set_book_genre('Мартин Иден', 'Комедии')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Властелин колец']

    def test_get_books_with_specific_genre_returns_empty_list_if_no_books(self, collector):
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        assert collector.get_books_with_specific_genre('Комедии') == []

    def test_get_books_for_children_returns_books_without_age_rating(self, collector):
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        assert 'Властелин колец' in collector.get_books_for_children()

    def test_get_books_for_children_excludes_books_with_age_rating(self, collector):
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert 'Оно' not in collector.get_books_for_children()

    def test_get_books_for_children_excludes_books_without_genre(self, collector):
        collector.add_new_book('Властелин колец')
        assert 'Властелин колец' not in collector.get_books_for_children()

    def test_add_book_in_favorites_added_successfully(self, collector):
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')
        assert 'Властелин колец' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_not_added_if_book_not_in_books_genre(self, collector):
        collector.add_book_in_favorites('Властелин колец')
        assert 'Властелин колец' not in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_not_added_twice(self, collector):
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')
        assert len(collector.get_list_of_favorites_books()) == 1         

    def test_delete_book_from_favorites_deleted_successfully(self, collector):
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')
        collector.delete_book_from_favorites('Властелин колец')
        assert 'Властелин колец' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_no_error_if_book_not_in_favorites(self, collector):
        collector.add_new_book('Властелин колец')
        collector.delete_book_from_favorites('Властелин колец')
        assert 'Властелин колец' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_returns_correct_list(self, collector):
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Властелин колец')
        collector.add_book_in_favorites('Оно')
        assert collector.get_list_of_favorites_books() == ['Властелин колец', 'Оно']
