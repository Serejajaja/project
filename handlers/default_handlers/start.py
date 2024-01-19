from telebot.types import Message

from loader import bot
from database.core import User
from peewee import IntegrityError
from states.user_date import UserState


@bot.message_handler(commands=["start"])  # задаем команды на которые бот будет реагировать
def bot_start(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    try:
        User.create(
            user_id=user_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        mess = (f'Привет, <b> {message.from_user.username}! </b>\n'
                f'Для помощи воспользуйся меню или напиши /help.\n'
                f'Данный бот поможет тебе подобрать кино картины по рейтингу.')
        bot.reply_to(message, mess, parse_mode='html')
        bot.set_state(message.from_user.id, UserState.new_user)
    except IntegrityError:
        mess = (f'Рад вас снова видеть, <b> {message.from_user.username} </b>!\n'
                f'Для помощи воспользуйся меню или напиши /help.')
        bot.reply_to(message, mess, parse_mode='html')
        bot.set_state(message.from_user.id, UserState.new_user)
