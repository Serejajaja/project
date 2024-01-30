
def string_request(page_data='1', sort_type_data=None, type_number_data=None, year_data=None, rating_data=None,
                   type_sort_data=None) -> str:
    """ На основание данных от пользователя формируем строку для api запроса """
    # данный для api запроса
    page_data = page_data  # номер выгружаемой страницы
    limit_data = '5'  # количество результатов на странице
    sort_field_data = 'rating.kp'  # сегмент поиска
    sort_type_data = sort_type_data  # 1 от 0 до 10, -1 от 10 до 0
    type_number_data = type_number_data  # 1 (movie), 2 (tv-series), 3 (cartoon), 4 (anime), 5 (animated-series)
    year_data = year_data  # дата фильма
    rating_data = rating_data  # рейтинг фильма
    not_genres_data = '!музыка'  # исключаемый жанр
    type_sort_data = type_sort_data

    if year_data:  # если запрос пользователя ручной
        result = (f'?page={page_data}'
                  f'&limit={limit_data}'
                  f'&sortField={sort_field_data}'
                  f'&sortType={sort_type_data}'
                  f'&typeNumber={type_number_data}'
                  f'&year={year_data}'
                  f'&rating.kp={rating_data}'
                  f'&genres.name={not_genres_data}')
        return result
    elif type_sort_data:
        result = (f'?page={page_data}'
                  f'&limit={limit_data}'
                  f'&sortField={sort_field_data}'
                  f'&sortType={sort_type_data}'
                  f'&lists={type_sort_data}')
        return result
    else:  # если запрос по умолчанию
        result = (f'?page={page_data}'
                  f'&limit={limit_data}'
                  f'&sortField={sort_field_data}'
                  f'&sortType={sort_type_data}'
                  f'&typeNumber={type_number_data}'
                  f'&genres.name={not_genres_data}')
        return result
