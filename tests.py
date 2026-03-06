import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_initial_state(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {} and collector.get_list_of_favorites_books() == []

    def test_add_new_book_correct_add_book_successful_add(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        assert collector.get_book_genre('Азбука') == ''

    @pytest.mark.parametrize("name, expected_count", [
        ('Азбука', 1),
        ('', 0),
        ('Азбука' * 10, 0)
    ])
    def test_add_new_book_incorrect_add_book_unsuccessful_add(self, name, expected_count):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == expected_count

    def test_set_book_genre_correct_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        collector.set_book_genre('Азбука', 'Ужасы')
        assert collector.books_genre['Азбука'] == 'Ужасы'

    def test_set_book_genre_incorrect_genre_unsuccess(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        collector.set_book_genre('Азбука', 'FFFFFF')
        assert collector.books_genre['Азбука'] == ''

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        collector.set_book_genre('Азбука', 'Ужасы')
        assert collector.get_book_genre('Азбука') == 'Ужасы'

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        books = ['Азбука', 'Алгебра', 'Маленький принц']
        for book in books:
            collector.add_new_book(book)
            collector.set_book_genre(book, 'Ужасы')
        
        collector.add_new_book('Ну погоди')
        collector.set_book_genre('Ну погоди', 'Мультфильмы')

        assert collector.get_books_with_specific_genre('Ужасы') == books

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        assert collector.get_books_genre() == {'Азбука': ''}

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Детская')
        collector.add_new_book('Взрослая')
        collector.set_book_genre('Детская', 'Фантастика')
        collector.set_book_genre('Взрослая', 'Ужасы')

        assert collector.get_books_for_children() == ['Детская']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        collector.add_book_in_favorites('Азбука')
        assert collector.get_list_of_favorites_books() == ['Азбука']

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        collector.add_book_in_favorites('Азбука')
        collector.delete_book_from_favorites('Азбука')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        collector.add_new_book('Алгебра')
        collector.add_book_in_favorites('Азбука')
        collector.add_book_in_favorites('Алгебра')
        assert collector.get_list_of_favorites_books() == ['Азбука', 'Алгебра']