# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_win.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
# from . import style



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")



        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 260, 751, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        self.column_label = ('№', 'Дата публикации', 'Заметка', 'check')
        self.tableWidget.setHorizontalHeaderLabels(self.column_label)
        self.tableWidget.setSortingEnabled(True)

        # widget = self.create_checkbox_for_table()
        # self.tableWidget.setCellWidget(0, 4, widget)
        # self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("Text in column 2"))
        # self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem("Text in column 3"))



        self.new_entry = QtWidgets.QPushButton(self.centralwidget)
        self.new_entry.setGeometry(QtCore.QRect(660, 10, 101, 23))
        self.new_entry.setMouseTracking(True)
        self.new_entry.setObjectName("new_entry")

        # self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        # self.calendarWidget.setGeometry(QtCore.QRect(20, 20, 296, 183))
        # self.calendarWidget.setObjectName("calendarWidget")

        self.errormessage = QtWidgets.QLabel(self.centralwidget)
        self.errormessage.setGeometry(QtCore.QRect(15, 111, 460, 19))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.errormessage.setFont(font)


        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(17, 230, 751, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setGeometry(QtCore.QRect(664, 210, 101, 23))
        self.delete_button.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.delete_button.setMouseTracking(True)
        self.delete_button.setTabletTracking(True)
        self.delete_button.setObjectName("delete_button")

        self.edit_button = QtWidgets.QPushButton(self.centralwidget)
        self.edit_button.setGeometry(QtCore.QRect(504, 210, 151, 23))
        self.edit_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.edit_button.setMouseTracking(True)
        self.edit_button.setTabletTracking(True)
        self.edit_button.setObjectName("edit_button")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.noth_chos_sign = QtWidgets.QLabel(self.centralwidget)
        self.noth_chos_sign.setGeometry(QtCore.QRect(470, 180, 300, 23))
        self.noth_chos_sign.setObjectName("noth_chos_sign")


    # def create_checkbox_for_table(self):
    #     pWidget = QtWidgets.QWidget()
    #     pCheckBox = QtWidgets.QCheckBox()
    #     pCheckBox.setCheckState(QtCore.Qt.Checked)
    #     pLayout = QtWidgets.QHBoxLayout(pWidget)
    #     pLayout.addWidget(pCheckBox)
    #     pLayout.setAlignment(QtCore.Qt.AlignCenter)
    #     pLayout.setContentsMargins(0,0,0,0)
    #     pWidget.setLayout(pLayout)
    #     return pWidget



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.new_entry.setText(_translate("MainWindow", "Новая запись"))
        self.delete_button.setText(_translate("MainWindow", "Удалить запись"))
        self.edit_button.setText(_translate("MainWindow", "Редактировать поле"))
        # self.noth_chos_sign.setText(_translate("MainWindow", "Введите текст заметки:"))
# style = '''
# QTableWidget::item {background-color: white;
# border-style: outset;
# border-width: 3px; border-radius: 7px; border-color: black;}
# QTableWidget::item:selected {background-color: #91F68F;
# border-width: 2px; border-radius: 7px; color: white; border-color: blue}
# '''

class Ui_new_note_dialog(object):
    def setupUi(self, new_note_dialog):
        new_note_dialog.setObjectName("new_note_dialog")
        new_note_dialog.resize(579, 244)

        self.save_button = QtWidgets.QPushButton(new_note_dialog)
        self.save_button.setGeometry(QtCore.QRect(30, 180, 161, 41))
        self.save_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.save_button.setMouseTracking(True)
        self.save_button.setTabletTracking(True)
        self.save_button.setObjectName("save_button")

        self.new_note_input_space = QtWidgets.QLineEdit(new_note_dialog)
        self.new_note_input_space.setGeometry(QtCore.QRect(30, 30, 521, 121))
        self.new_note_input_space.setMaxLength(10000)
        self.new_note_input_space.setObjectName("new_note_input_space")

        self.new_note_label = QtWidgets.QLabel(new_note_dialog)
        self.new_note_label.setGeometry(QtCore.QRect(30, 10, 131, 16))
        self.new_note_label.setObjectName("new_note_label")


    def retranslateUi(self, new_note_dialog):
        _translate = QtCore.QCoreApplication.translate
        new_note_dialog.setWindowTitle(_translate("new_note_dialog", "Dialog"))
        self.new_note_label.setText(_translate("new_note_dialog", "Введите текст заметки:"))
        self.save_button.setText(_translate("new_note_dialog", "Сохранить"))
