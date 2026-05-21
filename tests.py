from main import BooksCollector
import pytest

class TestBooksCollector:

    # пример теста
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # 1. Добавление книги с валидным названием
    def test_add_new_book_valid_name(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        assert "Война и мир" in collector.get_books_genre()

    # 2. Невалидные названия (параметризация)
    @pytest.mark.parametrize("name", ["A"*41, ""])
    def test_add_new_book_invalid_name(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    # 3. Дубликат не добавляется
    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book("Дубликат")
        collector.add_new_book("Дубликат")
        assert len(collector.get_books_genre()) == 1

    # 4. Установка жанра
    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        assert collector.get_book_genre("Гарри Поттер") == "Фантастика"

    # 5. Нельзя установить несуществующий жанр
    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Тест")
        collector.set_book_genre("Тест", "Роман")
        assert collector.get_book_genre("Тест") == ""

    # 6. Получение жанра
    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", "Детективы")
        assert collector.get_book_genre("Книга") == "Детективы"

    # 7. Список книг по жанру
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Ужасная книга")
        collector.set_book_genre("Ужасная книга", "Ужасы")
        result = collector.get_books_with_specific_genre("Ужасы")
        assert "Ужасная книга" in result

    # 8а. Книги для детей: детские книги попадают в список
    def test_get_books_for_children_includes_children_books(self):
        collector = BooksCollector()
        collector.add_new_book("Детская книга")
        collector.set_book_genre("Детская книга", "Мультфильмы")
        children_books = collector.get_books_for_children()
        assert "Детская книга" in children_books

    # 8б. Книги для детей: книги с возрастным рейтингом не попадают в список
    def test_get_books_for_children_excludes_age_restricted_books(self):
        collector = BooksCollector()
        collector.add_new_book("Страшная книга")
        collector.set_book_genre("Страшная книга", "Ужасы")
        children_books = collector.get_books_for_children()
        assert "Страшная книга" not in children_books

    # 9. Добавление в избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Любимая книга")
        collector.add_book_in_favorites("Любимая книга")
        assert "Любимая книга" in collector.get_list_of_favorites_books()

    # 10. Удаление из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        collector.delete_book_from_favorites("Книга")
        assert "Книга" not in collector.get_list_of_favorites_books()