from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys

class testeme(QMainWindow):
    def __init__(self) -> None:
        super(testeme, self).__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.centerS = QApplication.primaryScreen().availableGeometry()
        self.setGeometry((self.centerS.width() - 500) / 2, (self.centerS.height() - 500) / 2 , 500, 500)
        self.setMinimumSize(QSize(50, 50))
        self.show()


        


def subApp():
    app = QApplication(sys.argv)

    thiswindow = testeme()

    try:
        sys.exit(app.exec())       
    except:
        print("some error on teste side")
        exit()