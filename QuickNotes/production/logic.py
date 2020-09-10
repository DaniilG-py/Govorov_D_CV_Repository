from datetime import datetime
from PyQt5 import QtWidgets

from production import main_win, class_bd



# Инициализация БД и создание таблицы
table = class_bd.Db()
table.table_maker()


class MainWin(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = main_win.Ui_MainWindow()
        self.ui.setupUi(self)

        self.new_note_win = NewNoteWin()
        self.read_notes_from_db()

        self.clicked_spot = []
        self.ui.new_entry.clicked.connect(self.new_note)
        self.ui.delete_button.clicked.connect(self.delete_button)
        self.ui.tableWidget.clicked.connect(self.clicked_table)


    # Заполнение таблицы данными из БД
    def read_notes_from_db(self):
        self.data = table.read_notes()
        self.ui.tableWidget.setRowCount(len(self.data))

        row = 0
        for tup in self.data:
            coll = 0

            for item in tup:
                cellinfo = QtWidgets.QTableWidgetItem(str(item))
                self.ui.tableWidget.setItem(row, coll, cellinfo)

                coll += 1
            row += 1


    def new_note(self):
        print('нажато Добавить')
        self.new_note_win.show()


    def clicked_table(self):
        self.clicked_spot = sorted(set(index.data() for index in
                      self.ui.tableWidget.selectedIndexes()))


    def delete_button(self):
        if self.clicked_spot:
            table.delete_note(self.clicked_spot[0])
        else:
            print('nothing chosen')
            self.ui.noth_chos_sign.setText('Выберите строку таблице, которую следует удалить')


    def edit(self):
        pass



class NewNoteWin(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.new_note_ui = main_win.Ui_new_note_dialog()
        self.new_note_ui.setupUi(self)

        self.save_note()


    def save_note(self):
        self.save_btn = self.new_note_ui.save_button
        self.save_btn.clicked.connect(self.save_new_note)


    def save_new_note(self):
        date = datetime.now()
        text = self.new_note_ui.new_note_input_space.text()
        if text:
            table.add_note(date, text)
            self.close()
        else:
            self.close()
