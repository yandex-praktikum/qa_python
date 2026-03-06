from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    
    import pytest
from main import BooksCollector


class TestBooksCollector:

    # Фикстура для создания предварительно настроенного коллектора
    @pytest.fixture
    def collector_book(self):
        collector = BooksCollector()
        # Добавляем книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('It')
        collector.add_new_book('Три поросенка')

        # Устанавливаем жанры
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('It', 'Ужасы')
        collector.set_book_genre('Три поросенка', 'Мультфильмы')

        return collector

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_init_all_genre_exist(self, genre):
        collector = BooksCollector()
        assert genre in collector.genre

    def test_set_book_genre_genre_from_list_set_ok(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_set_book_genre_genre_out_of_list_not_set(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Драма')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    def test_get_book_genre_return_genre_set(self, collector_book):
        assert collector_book.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_get_books_with_specific_genre_get_two_books_the_same_genre_of_three(self, collector_book):
        assert len(collector_book.get_books_with_specific_genre('Ужасы')) == 2

    def test_get_books_for_children_get_one_book_without_age_rating_of_three(self, collector_book):
        assert len(collector_book.get_books_for_children()) == 1

    def test_add_book_in_favorites_add_two_new_books(self, collector_book):
        collector_book.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector_book.add_book_in_favorites('It')
        assert len(collector_book.get_list_of_favorites_books()) == 2

    def test_add_book_in_favorites_add_book_one_more_time_not_possible(self, collector_book):
        collector_book.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector_book.add_book_in_favorites('It')
        collector_book.add_book_in_favorites('It')
        assert len(collector_book.get_list_of_favorites_books()) == 2

    def test_add_book_in_favorites_add_book_out_of_list_not_possible(self, collector_book):
        collector_book.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector_book.add_book_in_favorites('It')
        collector_book.add_book_in_favorites('The Fall of the House of Usher')
        fav_book = collector_book.get_list_of_favorites_books()
        assert 'The Fall of the House of Usher' not in fav_book

    def test_delete_book_from_favorites_remove_one_book_possible(self, collector_book):
        collector_book.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector_book.add_book_in_favorites('It')
        collector_book.delete_book_from_favorites('It')
        fav_book = collector_book.get_list_of_favorites_books()
        assert 'It' not in fav_book

    def test_get_list_of_favorites_books_return_list_of_favorites_books_successfully(self, collector_book):
        collector_book.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector_book.add_book_in_favorites('It')
        assert len(collector_book.get_list_of_favorites_books()) == 2