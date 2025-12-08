# Юнит-тестирование BooksCollector

Проект 4 спринта: покрытие тестами класса `BooksCollector`.

## Описание реализованных тестов

Файл `tests.py` содержит 11 тестов.

### Добавление книг

1. **test_add_new_book_adds_book_without_genre**  
   Проверяет, что при добавлении новой книги она появляется в словаре `books_genre`, а её жанр не задан (`None`). Используется параметризация по нескольким названиям.

2. **test_add_new_book_does_not_add_book_with_name_longer_than_40**  
   Проверяет, что книга с названием длиннее 40 символов не добавляется в `books_genre`.

3. **test_add_new_book_does_not_add_duplicate_book**  
   Проверяет, что одну и ту же книгу нельзя добавить в словарь больше одного раза.

### Работа с жанрами

4. **test_set_book_genre_sets_genre_for_existing_book**  
   Проверяет, что для существующей книги можно установить жанр из списка доступных.

5. **test_set_book_genre_does_not_set_genre_for_unknown_book**  
   Проверяет, что для несуществующей книги жанр не устанавливается и она не добавляется в словарь.

6. **test_get_book_genre_returns_none_for_book_without_genre**  
   Проверяет, что `get_book_genre` возвращает `None`, если жанр не установлен.

7. **test_get_books_with_specific_genre_returns_only_books_with_that_genre**  
   Проверяет, что метод возвращает только книги с указанным жанром.

8. **test_get_books_for_children_excludes_books_with_age_rating**  
   Проверяет, что книги с возрастным рейтингом не попадают в список доступных детям.

### Избранное

9. **test_add_book_in_favorites_adds_only_existing_book_and_ignores_duplicates**  
   Проверяет, что книгу можно добавить в избранное только один раз.

10. **test_add_book_in_favorites_does_not_add_book_which_is_not_in_books_genre**  
   Проверяет, что нельзя добавить в избранное книгу, которой нет в `books_genre`.

11. **test_delete_book_from_favorites_removes_book**  
   Проверяет, что книга удаляется из избранного.

## Как запустить тесты

```bash
pytest -v tests.py

