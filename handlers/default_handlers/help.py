from telebot.types import Message

from config_data.config import DEFAULT_COMMANDS
from loader import bot
from keyboards.reply.reply_button import markup_button
from states.user_date import UserState


@bot.message_handler(commands=["help"])  # задаем команды на которые бот будет реагировать
def bot_help(message: Message):
    markup = markup_button()
    text = [f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]
    bot.reply_to(message, "\n".join(text), parse_mode='html', reply_markup=markup)  # ответ на сообщение
    bot.set_state(message.from_user.id, UserState.help_user)  # изменение статуса
