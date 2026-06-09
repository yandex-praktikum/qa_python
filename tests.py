import pytest
from main import BooksCollector


class TestBooksCollector:

    @pytest.fixture(autouse=True)
    def collector(self):
        self.collector = BooksCollector()

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector

        # добавляем две книги
        self.collector.add_new_book('Гордость и предубеждение и зомби')
        self.collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        assert len(self.collector.get_books_genre()) == 2

    @pytest.mark.parametrize('book,genre', [['Вишневый сад', 'Комедии'], ['Дюна', 'Фантастика'], ['Молчание ягнят', 'Детективы']])
    def test_set_book_genre_positive(self, book, genre): 
        self.collector.add_new_book(book)
        self.collector.set_book_genre(book, genre)
        assert self.collector.books_genre[book] == genre

    def test_set_book_genre_negative(self): 
        self.collector.add_new_book('Остров сокровищ')
        self.collector.set_book_genre('Остров сокровищ', 'Приключения')
        assert self.collector.books_genre['Остров сокровищ'] == ''

    def test_get_book_genre(self):
        self.collector.add_new_book('Дюна')
        self.collector.set_book_genre('Дюна', 'Фантастика')
        assert self.collector.get_book_genre('Дюна') == 'Фантастика'

    def test_get_books_with_specific_genre(self):
        self.collector.add_new_book('Золотой теленок')
        self.collector.set_book_genre('Золотой теленок', 'Комедии')
        self.collector.add_new_book('Дракула')
        self.collector.set_book_genre('Дракула', 'Ужасы')
        assert self.collector.get_books_with_specific_genre('Комедии') == ['Золотой теленок']

    def test_get_books_for_children(self):
        self.collector.add_new_book('Дракула')
        self.collector.set_book_genre('Дракула', 'Ужасы')
        self.collector.add_new_book('Молчание ягнят')
        self.collector.set_book_genre('Молчание ягнят', 'Детектив')
        self.collector.add_new_book('Ходячий замок')
        self.collector.set_book_genre('Ходячий замок', 'Мультфильмы')
        self.collector.add_new_book('Дон Кихот')
        self.collector.set_book_genre('Дон Кихот', 'Комедии')
        assert sorted(self.collector.get_books_for_children()) == sorted(['Ходячий замок', 'Дон Кихот'])

    def test_add_book_in_favorites(self):
        self.collector.add_new_book('Ходячий замок')
        self.collector.set_book_genre('Ходячий замок', 'Мультфильмы')
        self.collector.add_new_book('Дон Кихот')
        self.collector.set_book_genre('Дон Кихот', 'Комедии')
        self.collector.add_book_in_favorites('Дон Кихот')
        assert self.collector.favorites == ['Дон Кихот']

    def test_delete_book_from_favorites(self):
        self.collector.add_new_book('Ходячий замок')
        self.collector.set_book_genre('Ходячий замок', 'Мультфильмы')
        self.collector.add_new_book('Дон Кихот')
        self.collector.set_book_genre('Дон Кихот', 'Комедии')
        self.collector.add_book_in_favorites('Дон Кихот')
        self.collector.add_book_in_favorites('Ходячий замок')
        self.collector.delete_book_from_favorites('Дон Кихот')
        assert self.collector.favorites == ['Ходячий замок']

    def test_get_list_of_favorites_books(self):
        self.collector.add_new_book('Ходячий замок')
        self.collector.set_book_genre('Ходячий замок', 'Мультфильмы')
        self.collector.add_new_book('Дон Кихот')
        self.collector.set_book_genre('Дон Кихот', 'Комедии')
        self.collector.add_book_in_favorites('Дон Кихот')
        assert self.collector.get_list_of_favorites_books() == ['Дон Кихот']



