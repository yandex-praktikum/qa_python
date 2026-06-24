from main import BooksCollector
import pytest

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
        assert len(collector.get_books_genre()) == 2

    """
    Тест добавления новой книги с валидным названием.
    Проверяет корректность работы метода add_new_book:
    1. Добавляе книгу.
    Ожидаемый результат: книга добавилена в словарь books_genre.
    """
    def test_add_new_book_valid_name(self):
        collector = BooksCollector()
        book_name = "50 оттенков серого"
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    """
    Параметризованный тест проверки валидации длины названия книги.
    Проверяет два негативных сценария:
    - добавление книги с пустым названием;
    - добавление книги с названием длиннее 40 символов.
    Ожидаемый результат: ни одна из таких книг не добавляется в словарь books_genre.
    """
    @pytest.mark.parametrize('book_name', [
        '',  # тест с пустой строкой — книга не должна быть добавлена
        'a' * 41  # тест со строкой из 41 символа (превышает лимит в 40 символов) — книга не должна быть добавлена
    ])
    def test_add_new_book_invalid_length(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    """
    Тест установки жанра существующей книги.
    Проверяет корректность работы метода get_book_genre:
    1. Добавляем книгу.
    2. Устанавливаем ей жанр.
    3. Получаем жанр через get_book_genre и убеждаемся, что он равен установленному жанру.
    """
    @pytest.mark.parametrize('book_name, genre', [
        ( 'Король Лев','Мультфильмы'), # проверяем случай когда у книги есть жанр и что он равен 'Мультфильмы'
         ('Дюна', '')  # проверяем случай, когда у книги не задан жанр
        ])
    def test_set_book_genre_valid_book_and_genre(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    """
    Тест попытки установки недопустимого жанра.
    Проверяет, что жанр не устанавливается, если он отсутствует в списке self.genre.
    Сценарий:
    1. Создаём экземпляр BooksCollector.
    2. Добавляем книгу 'Хоббит'.
    3. Пытаемся установить ей жанр 'Романтика', которого нет в self.genre.
    4. Проверяем, что жанр книги не стал равен 'Романтика'.
    """
    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        book_name = 'Хоббит'
        invalid_genre = 'Романтика'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, invalid_genre)
        assert collector.get_book_genre(book_name) != invalid_genre

    """
    Тест попытки установки жанра для книги, которой нет в коллекции.
    Проверяет, что метод корректно обрабатывает ситуацию, когда книга
    отсутствует в словаре books_genre.
    Сценарий:
    1. Создаём экземпляр BooksCollector.
    2. Не добавляем книгу 'Неизвестная книга' в коллекцию.
    3. Пытаемся установить ей жанр 'Фантастика'.
    4. Проверяем, что книга не появилась в словаре и жанр не установлен.
    """
    def test_set_book_genre_book_not_in_collection(self):
        collector = BooksCollector()
        book_name = 'Неизвестная книга'
        genre = 'Фантастика'
        collector.set_book_genre(book_name, genre)
        assert book_name not in collector.get_books_genre()
        assert collector.get_book_genre(book_name) is None

    """
    Параметризованный тест получения списка книг по жанру.
    Проверяет работу метода get_books_with_specific_genre для разных жанров:
    - 'Фантастика' — должна вернуть ['Дюна'];
    - 'Мультфильмы' — должна вернуть ['Король Лев'];
    - 'Комедии' — список должен быть пустым (книг этого жанра нет).
    """
    @pytest.mark.parametrize('genre, expected_books', [
        ('Фантастика', ['Дюна']),
        ('Мультфильмы', ['Король Лев']),
        ('Комедии', [])  # проверяем случай, когда книг заданного жанра нет
    ])
    def test_get_books_with_specific_genre_specific_genre(self, genre, expected_books):
        collector = BooksCollector()
        # добавляем тестовые книги
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.add_new_book('Король Лев')
        collector.set_book_genre('Король Лев', 'Мультфильмы')
        result = collector.get_books_with_specific_genre(genre)
        assert sorted(result) == sorted(expected_books)

    """
    Тест отбора книг, подходящих для детей.
    Проверяет метод get_books_for_children:
    1. Добавляем книги разных жанров.
    2. Книги жанров из genre_age_rating ('Ужасы', 'Детективы') не должны попасть в результат.
    3. Остальные книги (без возрастного рейтинга) должны быть в списке.
    Ожидаемый результат: в списке только 'Винни Пух' и 'Золушка'.
    """
    def test_get_books_for_children_correct_selection(self):
        collector = BooksCollector()
        # книга для детей
        collector.add_new_book('Винни Пух')
        collector.set_book_genre('Винни Пух', 'Мультфильмы')
        # книга не для детей (в жанре с возрастным рейтингом)
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        children_books = collector.get_books_for_children()
        assert 'Винни Пух' in children_books
        assert 'Оно' not in children_books

    """
    Тест добавления книги в избранное.
    Проверяет:
    1. Книга добавлена в books_genre через add_new_book.
    2. Книга успешно добавлена в список favorites через add_book_in_favorites.
    3. Книга присутствует в списке избранного после добавления.
    """
    def test_add_book_in_favorites_valid_book(self):
        collector = BooksCollector()
        book_name = 'Маленький принц'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()

    """
    Тест удаления книги из избранного.
    Проверяет сценарий:
    1. Книга добавлена в избранное.
    2. Вызывается метод delete_book_from_favorites.
    3. После удаления книга отсутствует в списке избранного.
    """
    def test_delete_book_from_favorites_existing_book(self):
        collector = BooksCollector()
        book_name = '1984'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()

    """
    Тест попытки повторного добавления книги в коллекцию.
    Проверяет, что книга не добавляется в список повторно.
    Шаги:
    1. Добавляем книгу в коллекцию.
    2. Пытаемся добавить её в коллекцию второй раз.
    4. Проверяем, что в списке только одна копия книги.
    """
    def test_add_book_already_in_books_genre(self):
        collector = BooksCollector()
        book_name = 'Война и мир'
        collector.add_new_book(book_name)
        collector.add_new_book(book_name) # повторная попытка добавления
        books = collector.get_books_genre()
        assert len(books) == 1

    """
    Тест попытки повторного добавления книги в избранное.
    Проверяет, что книга не добавляется в список избранного повторно.
    Шаги:
    1. Добавляем книгу в коллекцию.
    2. Добавляем её в избранное первый раз.
    3. Пытаемся добавить её в избранное второй раз.
    4. Проверяем, что в списке избранного только одна копия книги.
    """
    def test_add_book_in_favorites_already_in_favorites(self):
        collector = BooksCollector()
        book_name = 'Война и мир'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.add_book_in_favorites(book_name)  # повторная попытка добавления
        favorites = collector.get_list_of_favorites_books()
        assert favorites.count(book_name) == 1

    """
    Тест получения словаря books_genre для пустой коллекции.
    Проверяет, что при отсутствии добавленных книг метод возвращает пустой словарь.
    """
    def test_get_books_genre_empty_collection(self):
        collector = BooksCollector()
        books_genre = collector.get_books_genre()
        assert isinstance(books_genre, dict)
        assert len(books_genre) == 0