from telebot.types import Message

from loader import bot
from keyboards.inline.inline_button import markup_line


@bot.message_handler(commands=['custom'])  # задаем команды на которые бот будет реагировать
def send_low(message: Message):
    markup = markup_line()
    mess = 'Задайте свои данные для поиска'
    bot.send_message(message.chat.id, mess, reply_markup=markup)