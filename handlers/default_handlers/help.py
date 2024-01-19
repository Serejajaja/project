from telebot.types import Message

from config_data.config import DEFAULT_COMMANDS
from loader import bot
from keyboards.inline.inline_button import markup_line


@bot.message_handler(commands=["help"])  # задаем команды на которые бот будет реагировать
def bot_help(message: Message):
    markup = markup_line()
    text = [f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]
    bot.reply_to(message, "\n".join(text), parse_mode='html', reply_markup=markup)
