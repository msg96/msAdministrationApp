###########################################################################################################################
###########################################################################################################################
###########################################################################################################################
###########################################################################################################################
############################################## -> DESGINED BY MATHEUS SANTOS ##############################################
###########################################################################################################################
###########################################################################################################################
###########################################################################################################################
###########################################################################################################################
###########################################################################################################################
########    PYSIDE6 IMPORTS                             ~   * IMPORTANT
###########################################################################################################################
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
###########################################################################################################################

class msHBoxLayout(QHBoxLayout):
    def __init__(self, parent :QWidget):
        super(msHBoxLayout, self).__init__(parent)
        self.setSpacing(0)
        self.setContentsMargins(0, 0, 0, 0)

    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()