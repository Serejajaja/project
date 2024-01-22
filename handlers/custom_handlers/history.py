from telebot.types import Message

from loader import bot
from keyboards.inline.inline_button import markup_line
from states.user_date import UserState


@bot.message_handler(commands=['history'])  # задаем команды на которые бот будет реагировать
def send_history(message: Message) -> None:
    markup = markup_line()
    mess = 'Истории ваших запросов'
    bot.send_message(message.chat.id, mess, reply_markup=markup)  # ответ на сообщение
    bot.set_state(message.from_user.id, UserState.history_user)  # изменение статуса
