import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # добавление книги с валидным именем 
    def test_add_new_book_valid_name_book_added(self, books_collector):
        book_name = "Новая книга"
        books_collector.add_new_book(book_name)
        assert book_name in books_collector.get_books_genre()

    # не добавляется книга c пустым именем и длинным именем
    @pytest.mark.parametrize("book_name", ["", "X"*41])
    def test_add_new_book_invalid_name_not_added(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 0

   # не добавляется уже существующая книга 
    def test_add_new_book_dublicate_not_added(self, books_collector):          
        dublicate_book = 'Книга'
        books_collector.add_new_book(dublicate_book)
        assert len(books_collector.get_books_genre()) == 1

    # установка жанра в первый раз
    def test_set_book_genre_book_in_dict_without_genre_genre_set(self, books_collector):
        book_name = "Книга"
        genre = "Детективы"
        books_collector.set_book_genre(book_name, genre)
        assert books_collector.get_book_genre(book_name) == genre 

    # замена жанра
    def test_set_book_genre_book_in_dict_with_genre_genre_update(self, books_collector):
        book_name = "Книга"
        genre = "Фантастика"
        new_genre = "Детективы"
        books_collector.set_book_genre(book_name, genre)
        books_collector.set_book_genre(book_name, new_genre)
        assert books_collector.get_book_genre(book_name) == new_genre 

    # при установке жанра несуществующая книга не добавляется
    def test_set_book_genre_book_not_exist_not_added(self):
        books_collector = BooksCollector()
        book_name = 'Несуществующая абракадабра'
        genre = 'Фантастика'
        books_collector.set_book_genre(book_name, genre)
        assert len(books_collector.get_books_genre()) == 0

    # несуществующий жанр не устанавливается
    def test_set_book_genre_book_in_dict_invalid_genre_genre_not_set(self, books_collector):
        book_name = 'Книга'
        genre = 'Несуществующий'
        books_collector.set_book_genre(book_name, genre)
        assert books_collector.get_book_genre(book_name) == ''
    
    # получение жанра для книги из словаря
    def test_get_book_genre_book_in_dict_genre_returned(self, books_collector):
        book_name = 'Книга'
        genre = 'Детективы'
        books_collector.set_book_genre(book_name, genre)
        assert books_collector.get_book_genre(book_name) == genre

    # получение жанра для книги не из словаря вернет None
    def test_get_book_genre_book_not_in_dict_none_returned(self, books_collector):
        book_name = 'Несуществующая'
        assert books_collector.get_book_genre(book_name) is None

    # получение списка книг по жанру
    def test_get_books_with_specific_genre_valid_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Книга-детектив")
        collector.set_book_genre("Книга-детектив", "Детективы")
        collector.add_new_book("Книга-фанастика")
        collector.set_book_genre("Книга-фанастика", "Фантастика")
        assert collector.get_books_with_specific_genre("Детективы") == ["Книга-детектив"]

    # получение пустого списка книг для несуществующего жанра
    def test_get_books_with_specific_genre_invalid_genre_empty_list(self, books_collector):
        assert books_collector.get_books_with_specific_genre("несуществующий") == []
        
    # получение текущего словаря books_genre
    def test_get_books_genre(self, books_collector):
        books_genre = books_collector.get_books_genre()
        assert len(books_genre) == 1 and 'Книга' in books_genre

    # получение списка детских книг включает детские жанры
    @pytest.mark.parametrize("genre", ["Фантастика", "Мультфильмы", "Комедии"])
    def test_get_books_for_children_return_children_books(self, genre, books_collector):
        book_name = "Книга"
        books_collector.set_book_genre(book_name, genre)
        children_books = books_collector.get_books_for_children()
        assert children_books == [book_name]

    # получение списка детских книг не включает взрослые жанры
    @pytest.mark.parametrize("genre", ["Ужасы", "Детективы"])
    def test_get_books_for_children_not_return_age_books(self, genre, books_collector):
        book_name = "Книга"
        books_collector.set_book_genre(book_name, genre)
        children_books = books_collector.get_books_for_children()
        assert children_books == []

    # добавление книги из словаря в избранное
    def test_add_book_in_favorites_from_dict_added(self, books_collector):
        book_name = "Книга"
        books_collector.add_book_in_favorites(book_name)
        assert books_collector.get_list_of_favorites_books() == [book_name]

    # не добавит в избранное книгу не из словаря
    def test_add_book_in_favorites_not_from_dict_not_added(self, books_collector):
        book_name = "Несуществующая книга"
        books_collector.add_book_in_favorites(book_name)
        assert books_collector.get_list_of_favorites_books() == []

    # добавление дубликата в избранное не добавит
    def test_add_book_in_favorites_duplicate_not_added(self, books_collector):
        book_name = "Книга"
        books_collector.add_book_in_favorites(book_name)
        books_collector.add_book_in_favorites(book_name)
        assert books_collector.get_list_of_favorites_books() == [book_name]

    # удаление книги из избранного удалит книгку
    def test_delete_book_from_favorites_exist_deleted(self, books_collector):
        book_name = "Книга"
        books_collector.add_book_in_favorites(book_name)
        books_collector.delete_book_from_favorites(book_name)
        assert books_collector.get_list_of_favorites_books() == []

    # удаление книги, которой нет в избранном, ничего не изменит   
    def test_delete_book_from_favorites_not_exist_no_changes(self, books_collector):
        book_name = "Несуществующая Книга"
        books_collector.add_book_in_favorites("Книга")
        books_collector.delete_book_from_favorites(book_name)
        assert books_collector.get_list_of_favorites_books() == ["Книга"]

    # получение списка избранных книг
    def test_get_list_of_favorites_books(self, books_collector):
        book_name = "Любимая книга"
        books_collector.add_new_book(book_name)
        books_collector.add_book_in_favorites(book_name)
        assert books_collector.get_list_of_favorites_books() == [book_name]
