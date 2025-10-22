import pytest

from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name', ['', 'a'*41])
    def test_add_new_book_invalid_name_lenght(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.books_genre

    def test_set_book_genre_add_one_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Голова профессора Доуэля')
        collector.set_book_genre('Голова профессора Доуэля', 'Фантастика')
        assert collector.books_genre['Голова профессора Доуэля'] == 'Фантастика'

    def test_get_book_genre_positive(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.books_genre['Оно'] = 'Ужасы'
        assert collector.get_book_genre('Оно') == 'Ужасы'
    
    def test_get_books_with_specific_genre_positive(self):
        collector = BooksCollector()
        collector.books_genre.update({'Убийство на улице Морг': 'Детективы', 'Рассказы о Шерлоке Холмсе': 'Детективы'})
        result = collector.get_books_with_specific_genre('Детективы')
        assert result == ['Убийство на улице Морг', 'Рассказы о Шерлоке Холмсе']

    def test_get_books_genre_positive(self):
        collector = BooksCollector()
        collector.books_genre = {'Оно': 'Ужасы'}
        assert collector.get_books_genre() == {'Оно': 'Ужасы'}

    def test_get_books_for_children_positive(self):
        collector = BooksCollector()
        collector.books_genre = {'Голова профессора Доуэля': 'Фантастика'}
        result = collector.get_books_for_children()
        assert 'Голова профессора Доуэля' in result

    def test_get_books_for_children_negative(self):
        collector = BooksCollector()
        collector.books_genre = {'Оно': 'Ужасы'}
        result = collector.get_books_for_children()
        assert 'Оно' not in result

    def test_add_book_in_favorites_positive(self):
        collector = BooksCollector()
        collector.add_new_book('Трое в лодке, не считая собаки')
        collector.add_book_in_favorites('Трое в лодке, не считая собаки')
        assert 'Трое в лодке, не считая собаки' in collector.favorites
    
    def test_delete_book_from_favorites_positive(self):
        collector = BooksCollector()
        collector.favorites = ['Убийство на улице Морг']
        collector.delete_book_from_favorites('Убийство на улице Морг')
        assert 'Убийство на улице Морг' not in collector.favorites

    def test_get_list_of_favorites_books_positive(self):
        collector = BooksCollector()
        collector.favorites = ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']