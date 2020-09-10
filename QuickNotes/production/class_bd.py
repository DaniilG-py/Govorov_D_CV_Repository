from datetime import datetime
import sqlalchemy as sa



class Db:

    def __init__(self):
        self.engine = sa.create_engine('sqlite:///db.sqlite3', echo=True)
        self.conn = self.engine.connect()
        self.metadata = sa.MetaData()
        self.data = []


    # Создание таблицы БД
    def table_maker(self):
        self.notes_table = sa.Table(
            'quick_notes_db',
            self.metadata,
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('pub_date', sa.String(80), nullable=False),
            sa.Column('note_text', sa.String(200), nullable=False),
        )
        self.metadata.create_all(self.engine)


    # Запись новой заметки в БД
    def add_note(self, date, text):
        ins = ({'pub_date': date, 'note_text': text}, )
        for item in ins:
            self.conn.execute(self.notes_table.insert().values(**item))


    # Чтение заметок из БД
    def read_notes(self):
        s = self.notes_table.select(self.notes_table)
        result = self.conn.execute(s)
        data = []

        for row in result:
            data.append(row)

        return data


    def delete_note(self, id_for_deletion):

        to_be_deleted = self.notes_table.delete().where(self.notes_table.c.id == id_for_deletion)
        self.conn.execute(to_be_deleted)


# tests

# table = Db()
# table.table_maker()
# #
# #
# table.read_notes()
# date = datetime.now()
# text = 'privet dydya'
#
# table.add_note(date, text)
