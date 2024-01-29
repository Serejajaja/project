import os
from dotenv import load_dotenv, find_dotenv
from pydantic import SecretStr, StrictStr
from pydantic_settings import BaseSettings

# Проверяем наличие env файла
if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

# Кортеж стандартных команд
DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("low", "Вывод 5 картин с минимальным рейтингом"),
    ("high", "Вывод 5 картин с максимальным рейтингом"),
    ("custom", "Вывод 5 картин в диапазоне выбранного вами рейтинга и года"),
    ("history", "Вывод истории ваших запросов"),
)

# Типы фильмов для колбэков в сценарии
type_films_dict = {
    '1': 'Фильмы',
    '2': 'Сериалы',
    '3': 'Мультфильмы',
    '4': 'Мультсериалы',
    '5': 'Аниме',
}

# Типы команд-статусов сценария
type_meny_check = (
    ('Низкий рейтинг 🔽', '/low'),
    ('Высокий рейтинг 🔼', '/high'),
    ('Выборочный рейтинг 📶', '/custom'),
    ('История запросов 📖', '/history'),
)


# Зачем добавили в класс не знаю, но вроде так создается уникальный объект с данными для входа
class SiteSettings(BaseSettings):
    """
    Класс со всем данными для входа, тут так же проверяется на наличие этих данных в .env
    """
    BOT_TOKEN: SecretStr = os.getenv('BOT_TOKEN', None)
    if BOT_TOKEN is None:
        exit('BOT_TOKEN отсутствует в переменных окружения')

    BOT_ID: SecretStr = os.getenv('BOT_ID', None)
    if BOT_ID is None:
        exit('BOT_TOKEN отсутствует в переменных окружения')

    API_KEY: SecretStr = os.getenv('API_KEY', None)
    if API_KEY is None:
        exit('API_KEY отсутствует в переменных окружения')

    API_URL: StrictStr = os.getenv('API_URL', None)
    if API_URL is None:
        exit('API_URL отсутствует в переменных окружения')
