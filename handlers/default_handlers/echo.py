from time import sleep
from loader import bot
from telebot.types import Message


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@bot.message_handler(state=None)
def bot_echo(message: Message) -> None:
    """ Функция принимает все сообщения которые не имеют состояния или не команда """
    if message.text in ['/hello-world', 'Привет']:
        mess = (f'Привет, <b> {message.from_user.username}! </b>\n'
                f'Для начала пройди регистрацию /start.\n'
                f'Затем воспользуйся меню или напиши /help.\n'
                f'Данный бот поможет тебе подобрать кино картины по рейтингу.\n'
                f'Или составить свой запрос по году и рейтингу.')
        bot.reply_to(message, mess, parse_mode='html')  # ответ на сообщение
    else:
        msg = bot.reply_to(message, text="Данный запрос некорректный.\n"
                                         "Пожалуйста используйте меню или /help для навигации.")
        sleep(5)
        bot.delete_message(message.chat.id, message.id)  # удаляем сообщение
        sleep(10)
        bot.delete_message(message.chat.id, msg.message_id)  # удаляем ответ на сообщение
