from telebot.types import Message

from loader import bot


@bot.message_handler(commands=['123'])  # задаем команды на которые бот будет реагировать
def welcome(message: Message):
    mesg = bot.send_message(message.chat.id, 'Введите имя')  # запрашиваем имя
    print(mesg)
    bot.register_next_step_handler(mesg, test)  # регистрируем следующее сообщение пользователя и передаем его в другую функцию


def test(message: Message):
    name = message.text  # сохраняем имя пользователя
    bot.send_message(message.chat.id, f'Ваше имя: {name}')  # выводим ответ в чате
    bot.send_message(message.chat.id, 'Новое сообщение!')  # отправка сообщения напрямую в чат бота через запрос id
