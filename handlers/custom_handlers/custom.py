from telebot.types import Message

from loader import bot
from keyboards.inline.inline_button import markup_line
from states.user_date import UserState


@bot.message_handler(commands=['custom'])  # задаем команды на которые бот будет реагировать
def send_low(message: Message):
    markup = markup_line()
    mess = 'Задайте свои данные для поиска'
    bot.send_message(message.chat.id, mess, reply_markup=markup)
    bot.set_state(message.from_user.id, UserState.custom_user)
