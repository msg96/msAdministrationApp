###########################################################################################################################
########    PYSIDE6 IMPORTS                             ~   * IMPORTANT
###########################################################################################################################
from multiprocessing import parent_process
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
###########################################################################################################################
from gui.widgets.msPanel import msPanel

class msGrip(msPanel):
    def __init__(self, parent: QWidget, type :str):
        super(msGrip, self).__init__(parent)
        try:
            self.parent = parent
            self.setParent(parent)
        except:
            pass
        
        self.weight = 3
        self.type = type
        self.backgroundColor("red")
        self.updateSize()
        
        
    
    def updateSize(self):
        if self.type.lower() == "left":
            self.setGeometry(0, 1, self.weight, self.parent.height())
        if self.type.lower() == "top":
            self.setGeometry(1, 0, self.parent.width(), self.weight)
        if self.type.lower() == "right":
            self.setGeometry(self.parent.width() - self.weight, 1, self.weight, self.parent.height())
        if self.type.lower() == "bottom":
            self.setGeometry(1, self.parent.height() - self.weight, self.parent.width(), self.weight)