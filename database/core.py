from datetime import datetime
import peewee as pw

db = pw.SqliteDatabase('database.db')


class ModelBase(pw.Model):
    created_at = pw.DateField(default=datetime.now())  # дата общая для обоих классов в БД

    class Meta:
        database = db


class User(ModelBase):
    user_id = pw.IntegerField(primary_key=True)  # первичный ключ модели, будет совпадать с Telegram ID.
    # Это значит, что он будет уникальным для всей таблицы.
    username = pw.CharField()
    first_name = pw.CharField()
    last_name = pw.CharField(null=True)


class History(ModelBase):
    number = pw.AutoField()
    user = pw.ForeignKeyField(User, backref="history")  # внешний ключ, ссылающийся на пользователя; backref создаёт
    # обратную ссылку: мы сможем получить задачи пользователя с помощью user.tasks.
    name_film = pw.TextField()


def db_start():
    db.connect()
    db.create_tables(ModelBase.__subclasses__())  # Создаем таблицу сразу для нескольких классов
