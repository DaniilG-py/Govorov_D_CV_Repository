from datetime import datetime
from PyQt5 import QtWidgets, QtCore

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

        self.cells_to_delete = []
        self.ui.new_entry.clicked.connect(self.new_note)


    # Заполнение таблицы данными из БД
    def read_notes_from_db(self):
        self.data = table.read_notes()                 # Чтение из БД
        self.ui.tableWidget.setRowCount(len(self.data))

        row = 0

        for tup in self.data:
            coll = 0

            for item in tup:
                checkbox = QtWidgets.QCheckBox(parent=self.ui.tableWidget)
                checkbox.stateChanged.connect(self.clicked_table)
                cellinfo = QtWidgets.QTableWidgetItem(str(item))

                self.ui.tableWidget.setItem(row, coll, cellinfo)
                self.ui.tableWidget.setCellWidget(row, 3, checkbox)

                coll += 1

            row += 1


    # Открытие окна новой заметки
    def new_note(self):
        print('нажато Добавить')
        self.new_note_win.show()


    # Проверка статуса checkbox, если True, то id записи добавляется в список на удаление
    def clicked_table(self, state):
        checkbox = self.sender()
        row = self.ui.tableWidget.indexAt(checkbox.pos())

        if state == QtCore.Qt.Checked:
            self.cells_to_delete.append(self.ui.tableWidget.item(row.row(), 0).text())
            self.ui.delete_button.clicked.connect(self.delete_button)
        else:
            self.cells_to_delete.remove(self.ui.tableWidget.item(row.row(), 0).text())


    # Удаление выделенных записей
    def delete_button(self, cells_to_delete):
        if self.cells_to_delete:
            table.delete_note(self.cells_to_delete)
        else:
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
