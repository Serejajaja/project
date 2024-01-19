from loader import bot
import handlers  # noqa
from utils.set_bot_commands import set_default_commands
from database.core import db_start


if __name__ == "__main__":
    db_start()  # запуск базы данных
    set_default_commands(bot)  # команды для кнопки меню
    bot.infinity_polling(none_stop=True)  # бесконечный цикл работы чата пока не остановим
