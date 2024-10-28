from main import BooksCollector
import pytest
class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Твин Пикс')
        collector.add_new_book('Бриджит Джонс')
        assert len(collector.get_books_genre()) == 2

    def test_repeated_add_new_book(self, collector):
        collector.add_new_book('Анна Каренина')
        collector.add_new_book('Анна Каренина')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_no_genre(self, collector):
        collector.add_new_book('Последний из Могикан')
        assert collector.books_genre['Последний из Могикан'] == ''

    @pytest.mark.parametrize('name', ['Э', 'Эрк', 'Эркюль Пуаро', 'Эркюль Пуаро. Убийство', 'Эркюль Пуаро. Убийство в восточном экспрессе'])
    def test_add_new_book_check_character_count(self, collector, name):
        collector.add_new_book(name)
        assert list(collector.books_genre.keys()) == [name]

    @pytest.mark.parametrize('name', ['', 'Эркюль Пуаро. Убийство', 'Эркюль Пуаро. Убийство в восточном экспрессе'])
    def test_not_add_new_book_check_character_count(self, collector, name):
        collector.add_new_book(name)
        assert not list(collector.books_genre.keys()) == [name]

    def test_set_book_genre (self, collector):
        collector.add_new_book('Код да Винчи')
        collector.set_book_genre('Код да Винчи', 'Фантастика')
        assert collector.books_genre['Код да Винчи'] == 'Фантастика'

    def test_get_book_genre_name (self, collector):
        collector.add_new_book('Трое из Простоквашино')
        collector.set_book_genre('Трое из Простоквашино', 'Мультфильмы')
        assert collector.books_genre.get('Трое из Простоквашино') == 'Мультфильмы'

    def test_get_books_with_horrors_genre(self, collector):
        collector.add_new_book('От заката до рассвета')
        collector.set_book_genre('От заката до рассвета', 'Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы') == ['От заката до рассвета']

    def test_get_books_with_cartoons_genre(self, collector):
        collector.add_new_book('Дюдюка')
        collector.set_book_genre('Дюдюка', 'Мультфильмы')
        assert collector.get_books_with_specific_genre('Мультфильмы') == ['Дюдюка']

    def test_get_books_genre_one_book(self, collector):
        collector.add_new_book('Старик Хоттабыч')
        collector.set_book_genre('Старик Хоттабыч', 'Фантастика')
        assert collector.get_books_genre() == {'Старик Хоттабыч': 'Фантастика'}

    def test_get_books_genre_many_books(self, collector):
        collector.add_new_book('Курочка Ряба')
        collector.set_book_genre('Курочка Ряба', 'Мультфильмы')
        collector.add_new_book('Резня бензопилой')
        collector.set_book_genre('Резня бензопилой', 'Ужасы')
        collector.add_new_book('Макс Фрай')
        collector.set_book_genre('Макс Фрай', 'Фантастика')
        assert collector.get_books_genre() == {'Курочка Ряба': 'Мультфильмы', 'Резня бензопилой': 'Ужасы', 'Макс Фрай': 'Фантастика'}

    def test_get_books_for_children(self, collector):
        collector.add_new_book('451 по Фаренгейту')
        collector.set_book_genre('451 по Фаренгейту', 'Фантастика')
        collector.add_new_book('Летучий голландец')
        collector.set_book_genre('Летучий голландец', 'Ужасы')
        collector.add_new_book('Кот Леопольд')
        collector.set_book_genre('Кот Леопольд', 'Мультфильмы')
        assert collector.get_books_for_children() == ['451 по Фаренгейту', 'Кот Леопольд']

    def test_age_rated_books_not_get_books_for_children(self, collector):
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.add_new_book('Очень страшная история')
        collector.set_book_genre('Очень страшная история', 'Ужасы')
        collector.add_new_book('Ну погоди')
        collector.set_book_genre('Ну погоди', 'Мультфильмы')
        assert not collector.get_books_for_children() == ['Очень страшная история']

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        assert 'Дюна' in collector.favorites

    def test_repeated_add_book_in_favorites(self, collector):
        collector.add_new_book('Очень страшная история')
        collector.add_book_in_favorites('Очень страшная история')
        collector.add_book_in_favorites('Очень страшная история')
        assert not collector.favorites == ['Очень страшная история', 'Очень страшная история']

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.delete_book_from_favorites('Книга')
        assert collector.favorites == []

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Инферно')
        collector.add_new_book('Интерны')
        collector.add_book_in_favorites('Инферно')
        collector.add_book_in_favorites('Интерны')
        collector.delete_book_from_favorites('Инферно')
        assert 'Интерны' in collector.favorites





