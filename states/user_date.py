from telebot.handler_backends import State, StatesGroup


class UserState(StatesGroup):
    new_user = State()
    help_user = State()
    low_user = State()
    high_user = State()
    custom_user = State()
    history_user = State()
    date_user = State()
