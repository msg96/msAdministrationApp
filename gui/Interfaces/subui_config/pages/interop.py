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
########    MODULES
###########################################################################################################################
from assets.styles import style
from modulos.msVariables import Svgs
###########################################################################################################################
########    WIDGETS
###########################################################################################################################
from gui.widgets.msPanel.msPanel import msPanel


class interopPage(msPanel):
    def __init__(self, parent: QWidget):
        super(interopPage, self).__init__(parent)

        self.applyStyles()


    def applyStyles(self):
        self.backgroundColor("blue")
        #self.backgroundColor(style['primarybg'])