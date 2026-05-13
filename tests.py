import pytest
from main import BooksCollector


class TestBooksCollector:
    @pytest.mark.parametrize(
        'name', [
            '', 'Невероятно длинное название фильма, которое точно не пройдет проверку'],
        ids=['null-name', 'toolong-name']
    )
    def test_add_new_book_invalid_names_not_added(self, collector, name):
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    def test_add_new_book_duplicate_name_not_added(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_valid_name_added(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector.get_books_genre()

    @pytest.mark.parametrize("name, genre", [
        ['Гордость и предубеждение и зомби', 'Триллер'],
        ['Гордость и честь и зомби', 'Ужасы'],
        ['Гордость и честь и зомби', 'Триллер']
    ],
        ids=['not_genre', 'not_name', 'not_coincidences'])
    def test_set_book_genre_invalid_names_and_genre_not_added(self, collector, name, genre):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre(name, genre)
        assert collector.get_books_genre().get(name) != genre

    def test_set_book_genre_valid_data_genre_added(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre(
            'Гордость и предубеждение и зомби') == 'Ужасы'

    def test_get_book_genre_returns_correct_genre(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

    def test_get_book_genre_returns_none_for_missing_book(self, collector):
        assert collector.get_book_genre('Неизвестная книга') is None

    def test_get_books_with_specific_genre_returns_books_list(self, collector):
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Оно']

    @pytest.mark.parametrize('genre', ['Боевик', 'Триллер'], ids=['non-existent-genre', 'invalid-genre'])
    def test_get_books_with_specific_genre_invalid_genre_returns_empty_list(self, collector, genre):
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_books_with_specific_genre(genre) == []

    def test_get_books_with_specific_genre_existing_genre_without_books_returns_empty_list(self, collector):
        assert collector.get_books_with_specific_genre('Комедии') == []

    def test_get_books_for_children_returns_books_without_age_rating(self, collector):
        collector.add_new_book('Шрек')
        collector.set_book_genre('Шрек', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Шрек']

    def test_get_books_genre_returns_dict(self, collector):
        collector.add_new_book('Оно')
        assert collector.get_books_genre() == {'Оно': ''}

    def test_add_book_in_favorites_adds_book(self, collector):
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')
        assert 'Оно' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_duplicate_not_added(self, collector):
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')
        collector.add_book_in_favorites('Оно')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_deletes_book(self, collector):
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')
        collector.delete_book_from_favorites('Оно')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_returns_favorites_list(self, collector):
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')
        assert collector.get_list_of_favorites_books() == ['Оно']

    def test_add_book_in_favorites_missing_book_not_added(self, collector):
        collector.add_book_in_favorites('Несуществующая книга')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_missing_book_not_deleted(self, collector):
        collector.delete_book_from_favorites('Несуществующая книга')
        assert collector.get_list_of_favorites_books() == []
