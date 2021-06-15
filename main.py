# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
import sys


class ClickedLabel(QtWidgets.QLabel):
    clicked = pyqtSignal()

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        self.clicked.emit()

class Ui_Erorr_Window(object):
    def setupUi(self, Erorr_Window):
        Erorr_Window.setObjectName("Erorr_Window")
        Erorr_Window.setFixedSize(480, 700)
        Erorr_Window.setStyleSheet("background-color: black;")
        self.centralwidget = QtWidgets.QWidget(Erorr_Window)
        self.centralwidget.setObjectName("centralwidget")
        Erorr_Window.setCentralWidget(self.centralwidget)
        self.label = ClickedLabel(self.centralwidget)
        self.label.setPixmap(QPixmap('img/png65.png'))
        self.label.setFixedSize(QSize(480, 700))
        self.text_label = QtWidgets.QLabel(self.centralwidget)
        self.text_label.setGeometry(QtCore.QRect(170, 600, 300, 40))
        self.text_label.setText("Water is not poured\n error: 04xF")
        self.text_label.setStyleSheet('background-color: none; color: red; font-size: 16px')
        self.text_label1 = QtWidgets.QLabel(self.centralwidget)
        self.text_label1.setGeometry(QtCore.QRect(170, 100, 300, 40))
        self.text_label1.setText("Technical indigestion")
        self.text_label1.setStyleSheet('background-color: none; color: red; font-size: 16px')
        self.retranslateUi(Erorr_Window)
        QtCore.QMetaObject.connectSlotsByName(Erorr_Window)

    def retranslateUi(self, Erorr_Window):
        _translate = QtCore.QCoreApplication.translate
        Erorr_Window.setWindowTitle(_translate("Erorr_Window", "MainWindow"))
        self.label.clicked.connect(lambda: self.returned())

    def returned(self):
        print("Exit_from Error Window")
        global SecWindow
        SecWindow = QtWidgets.QMainWindow()
        ui = Ui_SecWindow()
        ui.setupUi(SecWindow)
        Ero.close()
        SecWindow.show()



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(480, 700)
        Form.setStyleSheet('background-color: black;')
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")

        self.pay_btn = QtWidgets.QPushButton(self.centralwidget)
        self.pay_btn.setGeometry(QtCore.QRect(260, 60, 180, 180))
        self.pay_btn.setText("")
        self.pay_btn.setObjectName("pay_btn")
        self.pay_btn.setIcon(QIcon('img/png9.png'))
        self.pay_btn.setIconSize(QSize(120, 120))
        self.pay_btn.setStyleSheet('QPushButton:pressed {background-color: white;};')

        self.return_btn = QtWidgets.QPushButton(self.centralwidget)
        self.return_btn.setGeometry(QtCore.QRect(10, 50, 88, 91))
        self.return_btn.setText("")
        self.return_btn.setObjectName("return_btn")
        self.return_btn.setIcon(QIcon('img/png7.png'))
        self.return_btn.setIconSize(QSize(75, 75))
        self.return_btn.setStyleSheet('QPushButton:pressed {background-color: white;};')

        self.rfid_btn = QtWidgets.QPushButton(self.centralwidget)
        self.rfid_btn.setGeometry(QtCore.QRect(270, 420, 171, 141))
        self.rfid_btn.setText("")
        self.rfid_btn.setObjectName("rfid_btn")
        self.rfid_btn.setIcon(QIcon('img/png19.png'))
        self.rfid_btn.setIconSize(QSize(120, 120))
        self.rfid_btn.setStyleSheet('QPushButton:pressed {background-color: white;};')

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 260, 291, 111))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        Form.setCentralWidget(self.centralwidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Select a payment method"))
        self.label.setStyleSheet('color: white;')
        self.return_btn.clicked.connect(lambda: self.make_return())
        self.pay_btn.clicked.connect(lambda: self.make_return())
        self.rfid_btn.clicked.connect(lambda: self.make_return())


    def make_return(self):
        global SecWindow
        SecWindow = QtWidgets.QMainWindow()
        ui = Ui_SecWindow()
        ui.setupUi(SecWindow)
        Sec.hide()
        SecWindow.show()






class Ui_SecWindow(object):
    def setupUi(self, SecWindow):
        SecWindow.setObjectName("SecWindow")
        SecWindow.setFixedSize(480, 700)
        SecWindow.setStyleSheet("background-color: black;")
        self.centralwidget = QtWidgets.QWidget(SecWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.flag = True
        self.flag1 = True
        self.flag2 = True
        self.flag_liter = 0

        self.timer = QTimer(self.centralwidget, interval=600)
        self.timer.timeout.connect(self.flashing)
        self.timer.start()

        self.timer1 = QTimer(self.centralwidget, interval=600)
        self.timer1.timeout.connect(self.flashing1)
        self.timer1.start()

        self.timer2 = QTimer(self.centralwidget, interval=600)
        self.timer2.timeout.connect(self.flashing2)
        self.timer2.stop()

        self.normal_water33 = QtWidgets.QPushButton(self.centralwidget)
        self.normal_water33.setGeometry(QtCore.QRect(20, 20, 120, 80))
        self.normal_water33.setText("")
        self.normal_water33.setObjectName("normal_water33")
        self.normal_water33.setStyleSheet('QPushButton:pressed {background-color: white;};')

        self.frezee_water35 = QtWidgets.QPushButton(self.centralwidget)
        self.frezee_water35.setGeometry(QtCore.QRect(170, 20, 120, 80))
        self.frezee_water35.setText("")
        self.frezee_water35.setObjectName("frezee_water35")
        self.frezee_water35.setStyleSheet('QPushButton:pressed {background-color: white;};')

        self.artes_water31 = QtWidgets.QPushButton(self.centralwidget)
        self.artes_water31.setGeometry(QtCore.QRect(330, 20, 120, 80))
        self.artes_water31.setText("")
        self.artes_water31.setObjectName("artes_water31")
        self.artes_water31.setStyleSheet('QPushButton:pressed {background-color: white;};')

        self.main_btn32 = QtWidgets.QPushButton(self.centralwidget)
        self.main_btn32.setGeometry(QtCore.QRect(120, 240, 250, 250))
        self.main_btn32.setText("")
        self.main_btn32.setObjectName("main_btn32")
        self.main_btn32.setStyleSheet('QPushButton:pressed {background-color: white;};')

        self.half_btn = QtWidgets.QToolButton(self.centralwidget)
        self.half_btn.setGeometry(QtCore.QRect(20, 600, 120, 90))
        self.half_btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.half_btn.setObjectName("half_btn")
        self.half_btn.setText("Liter")
        self.half_btn.setStyleSheet('QToolButton{color: blue; };')
        self.half_btn.setStyleSheet('QToolButton:pressed {background-color: white;};')

        self.half_line = QtWidgets.QLineEdit(self.centralwidget)
        self.half_line.setGeometry(QtCore.QRect(65, 630, 40, 20))
        self.half_line.setObjectName("lineEdit_2")
        self.half_line.setText("0.5L")
        self.half_line.setStyleSheet('QLineEdit{color: blue;}')

        self.one_btn = QtWidgets.QToolButton(self.centralwidget)
        self.one_btn.setGeometry(QtCore.QRect(180, 600, 120, 90))
        self.one_btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.one_btn.setObjectName("one_btn")
        self.one_btn.setText("Liter")
        self.one_btn.setStyleSheet('QToolButton{color: blue; }')
        self.one_btn.setStyleSheet('QToolButton:pressed {background-color: white;};')

        self.one_line = QtWidgets.QLineEdit(self.centralwidget)
        self.one_line.setGeometry(QtCore.QRect(225, 630, 40, 20))
        self.one_line.setObjectName("lineEdit_2")
        self.one_line.setText("1.0L")
        self.one_line.setStyleSheet('QLineEdit{color: blue;}')

        self.halfone_btn = QtWidgets.QToolButton(self.centralwidget)
        self.halfone_btn.setGeometry(QtCore.QRect(340, 600, 120, 90))
        self.halfone_btn.setObjectName("halfone_btn")
        self.halfone_btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.halfone_btn.setText("Liter")

        self.halfone_line = QtWidgets.QLineEdit(self.centralwidget)
        self.halfone_line.setGeometry(QtCore.QRect(385, 630, 40, 20))
        self.halfone_line.setObjectName("lineEdit_2")
        self.halfone_line.setText("1.5L")
        self.halfone_line.setStyleSheet('QLineEdit{color: blue;}')
        self.halfone_btn.setStyleSheet('QToolButton:pressed {background-color: white;};')

        self.main_liter_line = QtWidgets.QLineEdit(self.centralwidget)
        self.main_liter_line.setGeometry(QtCore.QRect(195, 340, 100, 40))
        self.main_liter_line.setObjectName("main_liter_line")
        self.main_liter_line.setStyleSheet('background-color: #00BFFF; color: white; font-size: 20px')
        self.main_liter_line.setAlignment(QtCore.Qt.AlignCenter)
        self.main_liter_line.hide()

        self.liter_label = QtWidgets.QLabel(self.centralwidget)
        self.liter_label.setGeometry(QtCore.QRect(195, 320, 100, 20))
        self.liter_label.setObjectName("liter_label")
        self.liter_label.setStyleSheet('background-color: none; color: white; font-size: 16px')
        self.liter_label.setAlignment(QtCore.Qt.AlignCenter)
        self.liter_label.setText("Liters:")
        self.liter_label.hide()

        self.price_label = QtWidgets.QLabel(self.centralwidget)
        self.price_label.setGeometry(QtCore.QRect(195, 380, 100, 20))
        self.price_label.setObjectName("liter_label")
        self.price_label.setStyleSheet('background-color: none; color: white; font-size: 16px')
        self.price_label.setAlignment(QtCore.Qt.AlignCenter)
        self.price_label.setText("Price:")
        self.price_label.hide()

        self.main_price_line = QtWidgets.QLineEdit(self.centralwidget)
        self.main_price_line.setGeometry(QtCore.QRect(195, 400, 100, 40))
        self.main_price_line.setObjectName("main_liter_line")
        self.main_price_line.setStyleSheet('background-color: #00BFFF; color: white; font-size: 20px')
        self.main_price_line.setAlignment(QtCore.Qt.AlignCenter)
        self.main_price_line.hide()
        SecWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(SecWindow)
        QtCore.QMetaObject.connectSlotsByName(SecWindow)

    def flashing(self):
        if self.flag:
            self.normal_water33.setIcon(QIcon('img/png33.png'))
            self.normal_water33.setIconSize(QSize(72, 75))

            self.frezee_water35.setIcon(QIcon('img/png35.png'))
            self.frezee_water35.setIconSize(QSize(72, 75))

            self.artes_water31.setIcon(QIcon('img/png31.png'))
            self.artes_water31.setIconSize(QSize(72, 75))

            self.main_btn32.setIcon(QIcon('img/png32.png'))
            self.main_btn32.setIconSize(QSize(240, 240))

        else:
            self.normal_water33.setIcon(QIcon('img/png37.png'))
            self.normal_water33.setIconSize(QSize(72, 75))

            self.frezee_water35.setIcon(QIcon('img/png45.png'))
            self.frezee_water35.setIconSize(QSize(72, 75))

            self.artes_water31.setIcon(QIcon('img/png43.png'))
            self.artes_water31.setIconSize(QSize(72, 75))

            # self.main_btn32.setIcon(QIcon('img/png27.png'))
            # self.main_btn32.setIconSize(QSize(240, 240))

        self.flag = not self.flag

    def flashing1(self):
        if self.flag1:
            self.half_btn.setIcon(QIcon('img/png26.png'))
            self.half_btn.setIconSize(QSize(80, 70))
            self.one_btn.setIcon(QIcon('img/png26.png'))
            self.one_btn.setIconSize(QSize(80, 70))
            self.halfone_btn.setIcon(QIcon('img/png26.png'))
            self.halfone_btn.setIconSize(QSize(80, 70))
        else:
            self.half_btn.setIcon(QIcon('img/png49.png'))
            self.half_btn.setIconSize(QSize(80, 70))
            self.one_btn.setIcon(QIcon('img/png49.png'))
            self.one_btn.setIconSize(QSize(80, 70))
            self.halfone_btn.setIcon(QIcon('img/png49.png'))
            self.halfone_btn.setIconSize(QSize(80, 70))

        self.flag1 = not self.flag1

    def flashing2(self):
        if self.flag2:
            self.main_btn32.setIcon(QIcon('img/png32.png'))
            self.main_btn32.setIconSize(QSize(240, 240))
        else:
            self.main_btn32.setIcon(QIcon('img/png27.png'))
            self.main_btn32.setIconSize(QSize(240, 240))

        self.flag2 = not self.flag2

    def retranslateUi(self, SecWindow):
        _translate = QtCore.QCoreApplication.translate
        SecWindow.setWindowTitle(_translate("SecWindow", "MainWindow"))
        self.half_btn.clicked.connect(lambda: self.half_make())
        self.one_btn.clicked.connect(lambda: self.one_make())
        self.halfone_btn.clicked.connect(lambda: self.halfone_make())
        self.normal_water33.clicked.connect(lambda: self.normal_make())
        self.frezee_water35.clicked.connect(lambda: self.frezze_make())
        self.artes_water31.clicked.connect(lambda: self.artesian_make())
        self.main_btn32.clicked.connect(lambda: self.random_face())

    # self.half_btn.setText(_translate("SecWindow", "0.5L"))
    # self.one_btn.setText(_translate("SecWindow", "1L"))
    # self.halfone_btn.setText(_translate("SecWindow", "1.5L"))

    def half_make(self):
        self.timer1.stop()
        self.main_liter_line.show()
        self.liter_label.show()
        self.main_liter_line.setText("0.5")
        self.flag1 = 1

        self.half_btn.setIcon(QIcon('img/png49.png'))
        self.half_btn.setIconSize(QSize(80, 70))
        self.one_btn.setIcon(QIcon('img/png26.png'))
        self.one_btn.setIconSize(QSize(80, 70))
        self.halfone_btn.setIcon(QIcon('img/png26.png'))
        self.halfone_btn.setIconSize(QSize(80, 70))
        print(self.flag1)

    def one_make(self):
        self.timer1.stop()
        self.main_liter_line.show()
        self.liter_label.show()
        self.main_liter_line.setText("1.0")
        self.flag1 = 2

        self.half_btn.setIcon(QIcon('img/png26.png'))
        self.half_btn.setIconSize(QSize(80, 70))
        self.one_btn.setIcon(QIcon('img/png49.png'))
        self.one_btn.setIconSize(QSize(80, 70))
        self.halfone_btn.setIcon(QIcon('img/png26.png'))
        self.halfone_btn.setIconSize(QSize(80, 70))
        print(self.flag1)

    def halfone_make(self):
        self.timer1.stop()
        self.main_liter_line.show()
        self.liter_label.show()
        self.main_liter_line.setText("1.5")
        self.flag1 = 3

        self.half_btn.setIcon(QIcon('img/png26.png'))
        self.half_btn.setIconSize(QSize(80, 70))
        self.one_btn.setIcon(QIcon('img/png26.png'))
        self.one_btn.setIconSize(QSize(80, 70))
        self.halfone_btn.setIcon(QIcon('img/png49.png'))
        self.halfone_btn.setIconSize(QSize(80, 70))
        print(self.flag1)

    def normal_make(self):
        self.timer.stop()
        self.timer2.start()
        self.price_label.show()
        self.main_price_line.show()
        x = float(self.main_liter_line.text())
        self.main_price_line.setText(str(x * 1))
        self.normal_water33.setIcon(QIcon('img/png37.png'))
        self.normal_water33.setIconSize(QSize(72, 75))
        self.frezee_water35.setIcon(QIcon('img/png35.png'))
        self.frezee_water35.setIconSize(QSize(72, 75))

        self.artes_water31.setIcon(QIcon('img/png31.png'))
        self.artes_water31.setIconSize(QSize(72, 75))

    def frezze_make(self):
        self.timer.stop()
        self.timer2.start()
        self.price_label.show()
        self.main_price_line.show()
        x = float(self.main_liter_line.text())
        self.main_price_line.setText(str(x * 1.5))
        self.frezee_water35.setIcon(QIcon('img/png45.png'))
        self.frezee_water35.setIconSize(QSize(72, 75))
        self.normal_water33.setIcon(QIcon('img/png33.png'))
        self.normal_water33.setIconSize(QSize(72, 75))
        self.artes_water31.setIcon(QIcon('img/png31.png'))
        self.artes_water31.setIconSize(QSize(72, 75))

    def artesian_make(self):
        self.timer.stop()
        self.timer2.start()
        self.price_label.show()
        self.main_price_line.show()
        x = float(self.main_liter_line.text())
        self.main_price_line.setText(str(x * 2))
        self.artes_water31.setIcon(QIcon('img/png43.png'))
        self.artes_water31.setIconSize(QSize(72, 75))
        self.normal_water33.setIcon(QIcon('img/png33.png'))
        self.normal_water33.setIconSize(QSize(72, 75))
        self.frezee_water35.setIcon(QIcon('img/png35.png'))
        self.frezee_water35.setIconSize(QSize(72, 75))

    def random_face(self):
        if True:
            f = [self.pay_face, self.error_face]
            rnd = random.choice(f)
            rnd()

    def pay_face(self):
        global Sec
        Sec = QtWidgets.QMainWindow()
        ui = Ui_Form()
        ui.setupUi(Sec)
        SecWindow.close()
        Sec.show()

    def error_face(self):
        global Ero
        Ero = QtWidgets.QMainWindow()
        ui = Ui_Erorr_Window()
        ui.setupUi(Ero)
        SecWindow.close()
        Ero.show()

class GifImg(QtWidgets.QLabel):
    signal = QtCore.pyqtSignal()

    def __init__(self, file_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.move = QtGui.QMovie(file_name)
        self.move.start()
        self.setMovie(self.move)
        self.setScaledContents(True)

    def mousePressEvent(self, event):
        self.signal.emit()


class Main(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.main_gif = GifImg("demo_gif1.gif")
        self.main_gif.setFixedSize(480, 700)
        self.main_gif.signal.connect(self.stop_gif)
        layout = QtWidgets.QVBoxLayout()
        # layout.addWidget(self.text)
        layout.addWidget(self.main_gif)
        self.setLayout(layout)

    def stop_gif(self):
        global SecWindow
        SecWindow = QtWidgets.QMainWindow()
        ui = Ui_SecWindow()
        ui.setupUi(SecWindow)
        self.hide()
        SecWindow.show()







if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())


import sys

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     SecWindow = QtWidgets.QMainWindow()
#     ui = Ui_SecWindow()
#     ui.setupUi(SecWindow)
#     SecWindow.show()
#     sys.exit(app.exec_())
