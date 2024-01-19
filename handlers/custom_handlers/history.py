from telebot.types import Message

from loader import bot
from keyboards.inline.inline_button import markup_line


@bot.message_handler(commands=['history'])  # задаем команды на которые бот будет реагировать
def send_low(message: Message):
    markup = markup_line()
    mess = 'Истории ваших запросов'
    bot.send_message(message.chat.id, mess, reply_markup=markup)