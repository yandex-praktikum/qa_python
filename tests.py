import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_valid_length(self):
        collector = BooksCollector()
        name = 'Книга'
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    def test_add_new_book_invalid_length_long(self):
        collector = BooksCollector()
        name = 'Очень длинное название книги, которое должно быть больше сорока символов, чтобы проверить граничное значение'
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    def test_add_new_book_invalid_length_empty(self):
        collector = BooksCollector()
        name = ''
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    def test_add_new_book_duplicate_not_allowed(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Дюна')
        assert len(collector.get_books_genre()) == 1

    def test_new_book_has_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        assert collector.get_book_genre('1984') == ''

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_valid_genre(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', genre)
        assert collector.get_book_genre('Война и мир') == genre

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Бойцовский Клуб')
        collector.set_book_genre('Бойцовский Клуб', 'Драма')
        assert collector.get_book_genre('Бойцовский Клуб') == ''

    def test_set_book_genre_for_nonexistent_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert collector.get_book_genre('Несуществующая книга') is None

    @pytest.mark.parametrize('genre, expected_books', [
        ('Фантастика', ['Дюна', 'Марсианин']),
        ('Ужасы', ['Оно']),
        ('Детективы', [])
    ])
    def test_get_books_with_specific_genre(self, genre, expected_books):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Марсианин')
        collector.add_new_book('Оно')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Марсианин', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_books_with_specific_genre(genre) == expected_books

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 1', 'Фантастика')
        expected = {'Книга 1': 'Фантастика', 'Книга 2': ''}
        assert collector.get_books_genre() == expected

    def test_get_books_for_children_excludes_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Вий')
        collector.add_new_book('Шерлок Холмс')
        collector.add_new_book('Колобок')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Вий', 'Ужасы')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        collector.set_book_genre('Колобок', 'Мультфильмы')
        books_for_children = collector.get_books_for_children()
        assert 'Гарри Поттер' in books_for_children
        assert 'Колобок' in books_for_children
        assert 'Вий' not in books_for_children
        assert 'Шерлок Холмс' not in books_for_children

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление и Наказание')
        collector.add_book_in_favorites('Преступление и Наказание')
        assert 'Преступление и Наказание' in collector.get_list_of_favorites_books()
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_not_in_books_genre(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Несуществующая книга')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_add_duplicate_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Волшебник Изумрудного Города')
        collector.add_book_in_favorites('Волшебник Изумрудного Города')
        collector.add_book_in_favorites('Волшебник Изумрудного Города')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Волшебник Изумрудного Города')
        collector.add_book_in_favorites('Волшебник Изумрудного Города')
        collector.delete_book_from_favorites('Волшебник Изумрудного Города')
        assert 'Волшебник Изумрудного Города' not in collector.get_list_of_favorites_books()
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_nonexistent_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Богомолов')
        collector.add_book_in_favorites('Богомолов')
        collector.delete_book_from_favorites('Несуществующая книга')
        assert len(collector.get_list_of_favorites_books()) == 1
        assert 'Богомолов' in collector.get_list_of_favorites_books()