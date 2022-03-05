from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
from gui.Interfaces import subui_config

from required import *

from gui.Interfaces.subui_config import subui_Config

class testeme(QMainWindow):
    def __init__(self) -> None:
        super(testeme, self).__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.centerS = QApplication.primaryScreen().availableGeometry()
        self._w = 940 - 350
        self._h = 500 - 33
        self.setStyleSheet("background: #202020;")
        self.setGeometry((self.centerS.width() - self._w) / 2, (self.centerS.height() - self._h) / 2 , self._w, self._h)
        self.sp = subui_config.stylePage(self)
        self.setCentralWidget(self.sp)
        self.show()


        


def subApp():
    app = QApplication(sys.argv)

    thiswindow = testeme()

    try:
        sys.exit(app.exec())       
    except:
        exit()

    # pass