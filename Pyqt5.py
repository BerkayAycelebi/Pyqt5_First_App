import sys
import PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setWindowTitle("First Application")
        self.setGeometry(200,200,500,500)
        self.setWindowIcon(QIcon('logo.png'))
        self.setToolTip('My Tool Tip')
        self.initUI()

    def initUI(self):
        self.lbl_name=PyQt5.QtWidgets.QLabel(self)
        self.lbl_name.setText("Name: ")
        self.lbl_name.move(50,30)

        self.lbl_surname=PyQt5.QtWidgets.QLabel(self)
        self.lbl_surname.setText("Surname: ")
        self.lbl_surname.move(50,70)
        
        self.txt_name=PyQt5.QtWidgets.QLineEdit(self)
        self.txt_name.move(100,30)
        self.txt_name.resize(200,32)

        self.txt_surname=PyQt5.QtWidgets.QLineEdit(self)
        self.txt_surname.move(100,70)
        self.txt_surname.resize(200,32)

        self.lbl_result= PyQt5.QtWidgets.QLabel(self)
        self.lbl_result.setText('Result:')
        self.lbl_result.resize(300,150)
        self.lbl_result.move(100,150)

        self.btn_save=PyQt5.QtWidgets.QPushButton(self)
        self.btn_save.setText("Save")
        self.btn_save.move(100,110)
        self.btn_save.clicked.connect(self.clicked)

    def clicked(self):
       self.lbl_result.setText('Name: '+self.txt_name.text()+" Surname"+" "+self.txt_surname.text())
        

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()