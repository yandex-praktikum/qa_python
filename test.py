import pytest
from main import BooksCollector
from books_data import BOOK_WITH_GENRE

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
        # словарь books_rating, который нам возвращает метод get_books_gengre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # Тест на проверку игнорирования дубликатов при добавлении книги
    def test_add_new_book_ignore_duplicate_name(self):
        collector = BooksCollector()
        # Добавляем две книги с одинаковым именем
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        # Проверяем, что добавиласьь только одна книга
        assert len(collector.get_books_genre()) == 1

    # Тест на проверку игнорирования пустого имени при добавлении книги
    def test_add_new_book_igonore_empty_name(self):
        collector = BooksCollector()
        # Добавляем книгу с пустым именем
        collector.add_new_book("")
        # Проверяем, что книга не добавилась
        assert len(collector.get_books_genre()) == 0

    # Тест на проверку игнорирования добавления книги с именем длинее 40 символа
    def test_add_new_book_igonore_book_name_longer_than_41_symblos(self):
        collector = BooksCollector()
        # Создаем имя длиной 41 символа
        name = "A" * 41 
        # Добавляем книгу с именем длиной 41 символа
        collector.add_new_book(name)
        # # Проверяем, что книга не добавилась
        assert len(collector.get_books_genre()) == 0

    # Тест на проверку установки жанра книги черрез параметризацию
    @pytest.mark.parametrize("book, genre", BOOK_WITH_GENRE)
    def test_set_book_genre(self, book, genre):
        collector = BooksCollector()
        # Добавляем книгу
        collector.add_new_book(book)
        # Устанавливаем жанр книги
        collector.set_book_genre(book, genre)
        # Проверяем, что жанр книги установлен правильно
        assert collector.get_book_genre(book) == genre

    # Тест на проверку игнорирования установки жанра книги не из списка жанров
    def test_set_book_genre_ignore_genre_not_in_list(self):
        collector = BooksCollector()
        # Добавляем книгу 
        collector.add_new_book('Гордость и предубеждение и зомби')
        # Добаляем жанр не из списка жанров 
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Роман')
        # Проверяем, что жанр книги не установлен 
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''
    
    # Тест на проверку игнорирования установки жанра книги, которой нет в коллекции
    def test_set_book_genre_ignore_book_not_in_collection(self):
        collector = BooksCollector()
        # Добавляем жанр книге, которой нет в коллекции
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        #  Проверяем, что жанр книги не установлен
        assert collector.get_book_genre('Гордость и предубеждение и зомби') is None

    # Тест на проверку получения жанра книги с фикстурой
    def test_get_book_genre_book_exist(self, collector_with_books):
        collector = collector_with_books
        assert collector.get_book_genre("Оно") == "Ужасы"

    # Тест на проверку получения жанра книги, которой нет в коллекции, с фикстурой
    def test_get_book_genre_book_not_exist(self, collector_with_books):
        collector = collector_with_books
        assert collector.get_book_genre("Неизвестная книга") is None

    # Тест на проверку получения списка книг с определнным жанром черрез параметризацию
    @pytest.mark.parametrize("book, genre", BOOK_WITH_GENRE)
    def test_get_books_with_specific_genre(self, book, genre, collector_with_books):
        collector = collector_with_books
        # Добавляем книгу
        collector.add_new_book(book)
        # Устанавливаем жанр книги
        collector.set_book_genre(book, genre)
        # Проверяем, что книга возвращается в списке книг с определенным жанром
        assert book in collector.get_books_with_specific_genre(genre)
        
    # Тест на проверку получения словаря books_genre
    def test_get_books_genre_book_exist (self, collector_with_books):
        collector = collector_with_books
        # Преобразуем список книг с жанрами в словарь   
        dic_books = dict(BOOK_WITH_GENRE)
        # Проверяем, что метод возвращает правильный словарь книг с жанрами
        assert collector.get_books_genre() == dic_books
    
    # Тест на проверку получения списка книг, подходящих для детей
    def test_get_books_for_children_only_children_genres(self, collector_with_books):
        collector = collector_with_books
        # Получаем список книг для детей
        book_for_children = set(collector.get_books_for_children())
        # Проверяем, что в списке книг для детей только книги без возрастного рейтинга
        assert book_for_children == {"Цветы для Элджернона", "Приключения Винни", "Горе от ума"}

    # Тест на проверку получения списка книг, подходящих для детей, когда все книги имеют возрастной рейтинг
    @pytest.mark.parametrize("adult_genre", ['Ужасы', 'Детективы'])
    def test_get_books_for_children_no_children_genres(self, adult_genre):
        collector = BooksCollector()
        # Добавляем книгу с возрастныи рейтингом
        collector.add_new_book('Взрослая книга')
        collector.set_book_genre('Взрослая книга', adult_genre)
        # Проверяем, что список книг для детей пустой
        assert collector.get_books_for_children() == []

    #Тест на проверку добавление книги в избранное
    def test_add_book_in_favorites_one_book(self, collector_with_books):
        collector = collector_with_books
        # Добавляем книгу в избранное
        collector.add_book_in_favorites("Приключения Винни")
        # Проверяем, что книга добавлена в избраное
        assert "Приключения Винни" in collector.get_list_of_favorites_books()

    #Тест на проверку игнорирования дубликатов при добавлении книги в избранное
    def test_add_book_in_favorites_ignore_duplicates(self, collector_with_books):
        collector = collector_with_books
        # Добавляем книгу в избранное
        collector.add_book_in_favorites("Приключения Винни")
        collector.add_book_in_favorites("Приключения Винни")
        # Проверяем, что книга добавлена в избраное
        assert len(collector.get_list_of_favorites_books()) == 1
    
    #Тест на проверку удаления книги из избранного
    def tes_delete_book_from_favorites_one_book(self, collector_with_books):
        collector = collector_with_books
        # Добавляем книгу в избранное
        collector.add_book_in_favorites("Приключения Винни")
        # Удаляем книгу из избранного
        collector.delete_book_from_favorites("Приключения Винни")
        # Проверяем, что книга удалена из избраного
        assert "Приключения Винни" not in collector.get_list_of_favorites_books()

    #Тест на проверку удаления только одной книги из избранного при наличии нескольких книг
    def test_delete_book_from_favorites_one_of_many(self, collector_with_books):
        collector = collector_with_books
        # Добавляем книги в избранное
        collector.add_book_in_favorites("Приключения Винни")
        collector.add_book_in_favorites("Горе от ума")
        # Удаляем одну книгу из избранного
        collector.delete_book_from_favorites("Приключения Винни")
        # Проверяем, что удалена только одна книга из избраного
        assert collector.get_list_of_favorites_books() == ["Горе от ума"]

    # Тест на проверку не удаления книги из избранного, если ее там нет
    def test_delete_book_from_favorites_book_not_in_favorites(self, collector_with_books):
        collector = collector_with_books
        # Добавляем книгу в избранное
        collector.add_book_in_favorites("Приключения Винни")
        # Пытаемся удалить книгу, которой нет в избранном
        collector.delete_book_from_favorites("Горе от ума")
        # Проверяем, что в избранном осталась только добавленная книга
        assert collector.get_list_of_favorites_books() == ["Приключения Винни"] 

    # Тест на проверку получения списка избранных книг
    def test_get_list_of_favorites_books_return_favorites(self, collector_with_books):
        collector = collector_with_books
        # Добавляем книги в избранное
        collector.add_book_in_favorites("Приключения Винни")
        collector.add_book_in_favorites("Горе от ума")
        # Проверяем, что метод возвращает правильный список избранных книг
        assert collector.get_list_of_favorites_books() == ["Приключения Винни", "Горе от ума"]
    
    # Тест на проверку получения списка избранных книг, когда избранное пусто
    def test_get_list_of_favorites_books_empty_favorites(self, collector_with_books):
        collector = collector_with_books
        # Проверяем, что метод возвращает пустой список избранных книг
        assert collector.get_list_of_favorites_books() == []
    
    