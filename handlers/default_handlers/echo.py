from telebot.types import Message

from loader import bot


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@bot.message_handler(state=None)
def bot_echo(message: Message):
    bot.reply_to(
        message, "Эхо без состояния или фильтра.\n" f"Сообщение: {message.text}"
    )

# @bot.message_handler(func=lambda message: True)  # проверяем текст на сообщение это или нет, если да то
# def echo_all(message):
#     bot.reply_to(message, message.text)  # отвечаем тем же текстом

# @bot.message_handler()
# def get_user_text(message: Message):
#     """Данный метод позволяет взглянуть на все содержимые данные от введенного пользователем сообщения"""
#     bot.send_message(message.chat.id, message, parse_mode='html')
