from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from random import randint as r

import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setWindowTitle("Моя первая программа на pyqt")
        self.setGeometry(300, 300, 400, 225)

        self.text = QtWidgets.QLabel(self)
        self.text.setText('Привет, пользователь!')
        self.text.move(100, 20)
        self.text.adjustSize()

        self.text_input = QLineEdit(self)
        self.text_input.move(100, 100)

        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText('НАЖМИ')
        self.btn.move(70, 150)
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.action)

        self.btn_bg = QtWidgets.QPushButton(self)
        self.btn_bg.move(100, 50)
        self.btn_bg.setFixedWidth(200)
        self.btn_bg.clicked.connect(self.bg_color)
        self.btn_bg.hide()

    def action(self):
        if self.text_input.text():
            self.btn_bg.setText(f'Поменяй фон, {self.text_input.text()}')
        else:
            self.btn_bg.setText(f'Поменяй фон, пользователь')
        self.btn_bg.show()
        # для срабатывания кнопки 1 раз
        #self.btn.clicked.disconnect(self.action)'''

    def bg_color(self):
        self.setStyleSheet(f"background-color: rgb({r(0, 256)}, {r(0, 256)}, {r(0, 256)});")

def application():
    app = QApplication(sys.argv)
    window = MyWindow()

    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()


