# qa_python

----Реализованные тесты----
1. test_add_new_book_valid_name - добавления новой книги.
2. test_add_new_book_invalid_length - проверка валидации длины названия книги.
3. test_set_book_genre_valid_book_and_genre - установка жанра существующей книги.
4. test_set_book_genre_invalid_genre - установка недопустимого жанра.
5. test_set_book_genre_book_not_in_collection - установка жанра для книги, которой нет в коллекции.
6. test_get_books_with_specific_genre_specific_genre - получение списка книг по жанру.
7. test_get_books_for_children_correct_selection - отбор книг подходящих для детей.
8. test_add_book_in_favorites_valid_book - добавление книги в избранное.
9. test_delete_book_from_favorites_existing_book - удаление книги из избранного.
10. test_add_book_already_in_books_genre - повторное добавление книги в коллекцию.
11. test_add_book_in_favorites_already_in_favorites - попытка повторного добавления книги в избранное.
12. test_get_books_genre_empty_collection - получение пустой коллекции.