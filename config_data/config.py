import os
from dotenv import load_dotenv, find_dotenv
from pydantic import SecretStr, StrictStr
from pydantic_settings import BaseSettings

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("low", "Вывод 10 картин с минимальным рейтингом"),
    ("high", "Вывод 10 картин с максимальным рейтингом"),
    ("custom", "Вывод 10 картин в диапазоне выбранного вами рейтинга и года"),
    ("history", "Вывод истории ваших запросов"),
)


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


# a = SiteSettings()  # удалить
# print(a.BOT_TOKEN)  # удалить
# print(a.BOT_ID)  # удалить
# print(a.API_KEY)  # удалить
# print(a.API_URL)  # удалить
