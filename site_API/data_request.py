
def string_request(sort_type_data='1', type_number_data='1') -> str:

    # данный для api запроса
    page_data = '1'
    limit_data = '10'
    sort_field_data = 'rating.kp'
    sort_type_data = sort_type_data  # 1 от 0 до 10, -1 от 10 до 0
    type_number_data = type_number_data  # 1 (movie), 2 (tv-series), 3 (cartoon), 4 (anime), 5 (animated-series)
    year_data = ''

    if year_data:
        result = (f'?page={page_data}'
                  f'&limit={limit_data}'
                  f'&sortField={sort_field_data}'
                  f'&sortType={sort_type_data}'
                  f'&typeNumber={type_number_data}'
                  f'&year={year_data}')
        return result
    else:
        result = (f'?page={page_data}'
                  f'&limit={limit_data}'
                  f'&sortField={sort_field_data}'
                  f'&sortType={sort_type_data}'
                  f'&typeNumber={type_number_data}')
        return result
