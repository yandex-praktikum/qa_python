class BooksCollector:

    def __init__(self):
        self.books_genre = {}
        self.favorites = []
        self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        self.genre_age_rating = ['Ужасы', 'Детективы']

    # добавляем новую книгу
    def add_new_book(self, name):
        if not self.books_genre.get(name) and 0 < len(name) < 41:
            self.books_genre[name] = ''

    # устанавливаем книге жанр
    def set_book_genre(self, name, genre):
        if name in self.books_genre and genre in self.genre:
            self.books_genre[name] = genre

    # получаем жанр книги по её имени
    def get_book_genre(self, name):
        return self.books_genre.get(name)

    # выводим список книг с определённым жанром
    def get_books_with_specific_genre(self, genre):
        result = []
        for key, value in self.books_genre.items():
            if self.books_genre[key] == genre:
                result.append(key)
        return result

    # метод для детей: исключаем по возрастному рейтингу
    def get_books_for_children(self):
        result = []
        for name, genre in self.books_genre.items():
            if genre not in self.genre_age_rating:
                result.append(name)
        return result

    # добавляем в избранное
    def add_book_in_favorites(self, name):
        if name in self.books_genre and name not in self.favorites:
            self.favorites.append(name)

    # удаляем из избранного
    def delete_book_from_favorites(self, name):
        if name in self.favorites:
            self.favorites.remove(name)

    # получаем список избранных книг
    def get_list_of_favorites_books(self):
        return self.favorites
