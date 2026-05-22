# Sprint_4

## Список тестов для BooksCollector

1. **test_add_new_book_add_two_books** — проверка добавления двух книг
2. **test_add_new_book_valid_name_book_added** — добавление книги с валидным именем
3. **test_add_new_book_invalid_name_not_added** — не добавляется книга с пустым или длинным именем 
4. **test_add_new_book_dublicate_not_added** — не добавляется уже существующая книга
5. **test_set_book_genre_valid_book_without_genre_genre_set** — установка жанра книге без жанра
6. **test_set_book_genre_valid_book_with_genre_genre_update** — установка нового жанра книге с жанром
7. **test_set_book_genre_book_not_exist_not_added** — установка жанра для несуществующей книги не добавит книгу в словарь
8. **test_set_book_genre_valid_book_invalid_genre_genre_not_set** — не установит несуществующий жанр
9. **test_get_book_genre_book_in_dict_genre_returned** — получение жанра для книги из словаря
10. **test_get_book_genre_book_not_in_dict_none_returned**  получение жанра вернет None, если книга не в словаре
11. **test_get_books_with_specific_genre_valid_genre** — получение списка книг определённого жанра
12. **test_get_books_with_specific_genre_invalid_genre_empty_list** — получение пустого списка книг для несуществующего жанра
13. **test_get_books_genre** — получение текущего словаря books_genre
14. **test_get_books_for_children_return_children_books** — получение книг для детей возвращает книги детских жанров
15. **test_get_books_for_children_not_return_age_books** — получение книг для детей не возвращает книги взрослых жанров
16. **test_add_book_in_favorites_from_dict_added** — добавление в избранное книги из словаря 
17. **test_add_book_in_favorites_not_from_dict_not_added** — не добавляется в избранное книга не из словаря 
18. **test_add_book_in_favorites_duplicate_not_added** — не добавляется в избранное дубликат 
19. **test_delete_book_from_favorites_exist_deleted** — удаление книги из избранного
20. **test_delete_book_from_favorites_not_exist_no_changes** — удаление книги, которой нет в избранном, ничего не изменит 
21. **test_get_list_of_favorites_books** — получение списка избранных книг
