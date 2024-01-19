from telebot.types import Message

from loader import bot
from keyboards.inline.inline_button import markup_line
from states.user_date import UserState


@bot.message_handler(commands=['high'])  # задаем команды на которые бот будет реагировать
def send_low(message: Message):
    markup = markup_line()
    mess = 'Выберите категорию с самой высокой оценкой'
    bot.send_message(message.chat.id, mess, reply_markup=markup)  # ответ на сообщение
    bot.set_state(message.from_user.id, UserState.high_user)  # изменение статуса
