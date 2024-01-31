from config_data.config import DEFAULT_COMMANDS
from database.core import User
from keyboards.reply.reply_button import markup_button
from loader import bot
from states.user_date import UserState
from telebot.types import Message


@bot.message_handler(commands=["help"])  # задаем команды на которые бот будет реагировать
def bot_help(message: Message) -> None:
    """ Функция выдает пользователю список возможностей бота """
    user_id = message.from_user.id
    user = User.get_or_none(User.user_id == user_id)

    if user is None:
        bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
        return

    markup = markup_button()
    text = [f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]  # формируем список команд
    bot.reply_to(message, "\n".join(text), parse_mode='html', reply_markup=markup)  # ответ на сообщение
    bot.set_state(message.from_user.id, UserState.help_user, message.chat.id)  # изменение статуса
