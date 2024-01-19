from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from config_data.config import SiteSettings

config_bot = SiteSettings()
TOKEN = config_bot.BOT_TOKEN.get_secret_value()  # импортировали токен из конфига
chat_id = config_bot.BOT_ID.get_secret_value()  # импортировали id чата из конфига
storage = StateMemoryStorage()

bot = TeleBot(token=TOKEN, state_storage=storage)
