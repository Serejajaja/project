from telebot.handler_backends import State, StatesGroup


class UserState(StatesGroup):
    """ Создаем статусы пользователя """
    new_user = State()
    help_user = State()
    low_user = State()
    high_user = State()
    custom_user = State()
    history_user = State()
    date_user = State()
    question_1 = State()
    question_2 = State()
    question_3 = State()
    question_4 = State()
