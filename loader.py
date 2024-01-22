from telebot import TeleBot, StateMemoryStorage
from config_data.config import SiteSettings

config_bot = SiteSettings()  # загружаем настройки
TOKEN = config_bot.BOT_TOKEN.get_secret_value()  # импортировали токен из конфига
chat_id = config_bot.BOT_ID.get_secret_value()  # импортировали id чата из конфига
storage = StateMemoryStorage()  # Хранилище состояний (стейтов), по умолчанию StateMemoryStorage

bot = TeleBot(token=TOKEN, state_storage=storage)
