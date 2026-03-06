import pytest
from main import BooksCollector


class TestBooksCollector:

    # фикстура для пустого коллектора
    @pytest.fixture
    def collector(self):
        return BooksCollector()

    # фикстура с несколькими книгами и жанрами
    @pytest.fixture
    def collector_with_books(self):
        collector = BooksCollector()
        # добавляем книги разных жанров
        collector.add_new_book('Гарри Поттер')       # фантастика
        collector.add_new_book('Дюна')               # фантастика
        collector.add_new_book('Оно')                # ужасы
        collector.add_new_book('Дракула')            # ужасы
        collector.add_new_book('Малыш и Карлсон')    # детская / мультфильм
        collector.add_new_book('Незнайка на Луне')   # детская / мультфильм
        collector.add_new_book('Ну, погоди!')        # мультфильм

        # устанавливаем жанры
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Дракула', 'Ужасы')
        collector.set_book_genre('Малыш и Карлсон', 'Мультфильмы')
        collector.set_book_genre('Незнайка на Луне', 'Мультфильмы')
        collector.set_book_genre('Ну, погоди!', 'Мультфильмы')
        return collector

    # проверка добавления одной книги
    def test_add_new_book_add_one_book(self, collector):
        collector.add_new_book('Том Сойер')
        # проверяем, что книга добавилась
        assert 'Том Сойер' in collector.get_books_genre()
        # проверяем, что жанр пустой
        assert collector.get_book_genre('Том Сойер') == ''

    # проверка разных вариантов добавления книги
    @pytest.mark.parametrize(
        "name, expected_count",
        [
            ('Том Сойер', 1),
            ('', 0),
            ('А'*41, 0)  # название слишком длинное
        ],
        ids=["valid_name", "empty_name", "too_long_name"]
    )
    def test_add_new_book_various_cases(self, collector, name, expected_count):
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == expected_count

    # проверка установки жанра книги корректного
    def test_set_book_genre_correct(self, collector):
        collector.add_new_book('Том Сойер')
        collector.set_book_genre('Том Сойер', 'Фантастика')
        assert collector.get_book_genre('Том Сойер') == 'Фантастика'

    # проверка установки жанра книги некорректного
    def test_set_book_genre_wrong_genre(self, collector):
        collector.add_new_book('Том Сойер')
        collector.set_book_genre('Том Сойер', 'НеверныйЖанр')
        assert collector.get_book_genre('Том Сойер') == ''

    # проверка получения жанра книги
    def test_get_book_genre_returns_right_genre(self, collector_with_books):
        assert collector_with_books.get_book_genre('Гарри Поттер') == 'Фантастика'
        assert collector_with_books.get_book_genre('Оно') == 'Ужасы'

    # проверка получения списка книг по жанру
    def test_get_books_with_specific_genre(self, collector_with_books):
        books = collector_with_books.get_books_with_specific_genre('Фантастика')
        assert 'Гарри Поттер' in books
        assert 'Дюна' in books
        assert len(books) == 2

    # проверка получения словаря всех книг
    def test_get_books_genre_returns_dict(self, collector_with_books):
        books_dict = collector_with_books.get_books_genre()
        assert 'Гарри Поттер' in books_dict
        assert isinstance(books_dict, dict)

    # проверка получения книг для детей
    def test_get_books_for_children_excludes_rated(self, collector_with_books):
        books_for_children = collector_with_books.get_books_for_children()
        # книги без возрастного рейтинга должны быть
        assert 'Малыш и Карлсон' in books_for_children
        assert 'Незнайка на Луне' in books_for_children
        assert 'Ну, погоди!' in books_for_children
        # книги с возрастным рейтингом не должны быть
        assert 'Оно' not in books_for_children
        assert 'Дракула' not in books_for_children

    # проверка добавления книги в избранное
    def test_add_book_in_favorites_adds_book(self, collector):
        collector.add_new_book('Том Сойер')
        collector.add_book_in_favorites('Том Сойер')
        assert collector.get_list_of_favorites_books() == ['Том Сойер']

    # проверка, что дубликаты не добавляются в избранное
    def test_add_book_in_favorites_no_duplicates(self, collector):
        collector.add_new_book('Том Сойер')
        collector.add_book_in_favorites('Том Сойер')
        collector.add_book_in_favorites('Том Сойер')
        assert collector.get_list_of_favorites_books() == ['Том Сойер']

    # проверка удаления книги из избранного
    def test_delete_book_from_favorites(self, collector):
        # создаём книгу
        collector.add_new_book('Том Сойер')

        # добавляем в избранное
        collector.add_book_in_favorites('Том Сойер')
        # проверяем, что книга в избранном
        assert collector.get_list_of_favorites_books() == ['Том Сойер']

        # удаляем из избранного
        collector.delete_book_from_favorites('Том Сойер')
        # проверяем, что её больше нет
        assert collector.get_list_of_favorites_books() == []

    # проверка получения списка всех избранных книг
    def test_get_list_of_favorites_books_returns_correct_list(self, collector):
        collector.add_new_book('Том Сойер')
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Том Сойер')
        collector.add_book_in_favorites('Дюна')
        favorites = collector.get_list_of_favorites_books()
        assert favorites == ['Том Сойер', 'Дюна']

        