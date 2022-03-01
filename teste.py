from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
from gui.Interfaces import subui_Login

class testeme(QMainWindow):
    def __init__(self) -> None:
        super(testeme, self).__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.centerS = QApplication.primaryScreen().availableGeometry()
        self.setGeometry((self.centerS.width() - 500) / 2, (self.centerS.height() - 550) / 2 , 500, 550)
        self.login = subui_Login()
        self.login.start(self)
        self.show()


        


def subApp():
    app = QApplication(sys.argv)

    thiswindow = testeme()

    try:
        sys.exit(app.exec())       
    except:
        print("some error on teste side")
        exit()