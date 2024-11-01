
# Тесты для BooksCollector

Этот проект включает тесты, которые проверяют функциональность приложения `BooksCollector`, предназначенного для управления книгами, их жанрами и избранными книгами. В `BooksCollector` реализованы методы для добавления книг, присвоения жанров, управления избранными книгами и фильтрации книг по возрастным ограничениям.

## Реализованные тесты

### 1. `add_new_book`
   - **Добавление двух книг**: Проверяет, что книги добавляются корректно, если они уникальны. Проверка реализована через `test_add_new_book_add_two_books`.
   - **Повторное добавление книги**: Проверяет, что невозможно добавить одну и ту же книгу несколько раз. Тест `test_repeated_add_new_book`.
   - **Книга без жанра**: Проверяет, что новая книга добавляется с пустым значением жанра. Тест `test_add_new_book_no_genre`.
   - **Проверка длины названия**: Убедитесь, что книги добавляются, если их название находится в пределах 1–40 символов, и не добавляются, если длина не соответствует. Используется параметризация в `test_add_new_book_check_character_count` и `test_not_add_new_book_check_character_count`.

### 2. `set_book_genre`
   - **Присвоение жанра книге**: Проверяет, что жанр успешно устанавливается, если книга существует и жанр допустимый. Реализован в `test_set_book_genre`.

### 3. `get_book_genre`
   - **Получение жанра книги**: Проверяет, что `get_book_genre` корректно возвращает установленный жанр книги, если он задан. Тест `test_get_book_genre_name`.

### 4. `get_books_with_specific_genre`
   - **Фильтрация книг по жанру**: Проверяет, что метод возвращает корректный список книг, соответствующих указанному жанру. `test_get_books_with_horrors_genre` и `test_get_books_with_cartoons_genre`.

### 5. `get_books_genre`
   - **Получение полного словаря книг**: Проверяет, что `get_books_genre` возвращает правильное содержание словаря. Используются тесты `test_get_books_genre_one_book` и `test_get_books_genre_many_books`.

### 6. `get_books_for_children`
   - **Получение детских книг**: Проверяет, что возвращаются только книги, не содержащие возрастных ограничений. `test_get_books_for_children` проверяет, что жанры, не входящие в `genre_age_rating`, корректно возвращаются.

### 7. `add_book_in_favorites`
   - **Добавление книги в избранное**: Проверяет, что книгу можно добавить в избранное, если она есть в `books_genre`. Реализовано в `test_add_book_in_favorites`.
   - **Повторное добавление в избранное**: Проверяет, что одну книгу нельзя добавить в `favorites` несколько раз. `test_repeated_add_book_in_favorites`.

### 8. `delete_book_from_favorites`
   - **Удаление книги из избранного**: Проверяет, что книга удаляется из `favorites`, если она там была. `test_delete_book_from_favorites`.

### 9. `get_list_of_favorites_books`
   - **Получение списка избранных книг**: Проверяет, что `get_list_of_favorites_books` возвращает корректный список избранных книг. `test_get_list_of_favorites_books`.

## Запуск тестов

Для запуска тестов используйте:

```bash
pytest -v имя_теста.py
```

## Заключение

Реализованные тесты покрывают основные функции `BooksCollector` и проверяют как стандартные, так и специфические сценарии использования.
