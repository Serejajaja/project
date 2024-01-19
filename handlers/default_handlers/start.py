from telebot.types import Message

from loader import bot


@bot.message_handler(commands=["start"])  # задаем команды на которые бот будет реагировать
def bot_start(message: Message):
    mess = (f'Привет, <b> {message.from_user.username}! </b> Для помощи воспользуйся меню или напиши /help.\n'
            f'Данный бот тебе поможет подобрать кино картины по рейтингу.')
    bot.reply_to(message, mess, parse_mode='html')
