from telebot.types import Message

from loader import bot
from keyboards.inline.inline_button import markup_line


@bot.message_handler(commands=['low'])  # задаем команды на которые бот будет реагировать
def send_low(message: Message):
    markup = markup_line()
    mess = 'Выберите категорию с самой низкой оценкой'
    bot.send_message(message.chat.id, mess, reply_markup=markup)
