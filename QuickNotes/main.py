import sys
from PyQt5 import QtWidgets

from production import logic



# Запуск
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = logic.MainWin()

    win.show()

    sys.exit(app.exec())
