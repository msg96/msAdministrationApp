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
from random import randint
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
###########################################################################################################################
from gui.widgets.msPanel import msPanel

class msGrip(msPanel):
    def __init__(self, parent: QWidget, object :QWidget,type :Qt.Edge, weidht = 3, colorizer=False):
        super(msGrip, self).__init__(parent)
        try:
            self.parent = parent
            self.setParent(parent)
        except:
            pass 
        #
        self.object = object
        self.weight = weidht
        self.type = type
        self.resizeing = False
        #
        self.beforePanel = msPanel(self)
        self.midPanel = msPanel(self)
        self.afterPanel = msPanel(self)
        #
        if colorizer:
            x = randint(444444, 999999)
            self.beforePanel.backgroundColor("#{}".format(x))
            x = randint(444444, 999999)
            self.midPanel.backgroundColor("#{}".format(x))
            x = randint(444444, 999999)
            self.afterPanel.backgroundColor("#{}".format(x))
        #
        if self.type == Qt.LeftEdge or self.type == Qt.TopEdge:
            self.beforePanel.setCursor(Qt.CursorShape.SizeFDiagCursor)    
            self.afterPanel.setCursor(Qt.CursorShape.SizeBDiagCursor)
        elif self.type == Qt.RightEdge or self.type == Qt.BottomEdge:  
            self.beforePanel.setCursor(Qt.CursorShape.SizeBDiagCursor)    
            self.afterPanel.setCursor(Qt.CursorShape.SizeFDiagCursor)
        self.updateSize()
            
    def updateSize(self):
        if self.type == Qt.LeftEdge:    self.setGeometry(0, 1, self.weight, self.parent.height())
        if self.type == Qt.TopEdge:     self.setGeometry(1, 0, self.parent.width(), self.weight)
        if self.type == Qt.RightEdge:   self.setGeometry(self.parent.width() - self.weight, 1, self.weight, self.parent.height())
        if self.type == Qt.BottomEdge:  self.setGeometry(1, self.parent.height() - self.weight, self.parent.width(), self.weight)

        self.beforePanel.setGeometry(0, 0, 10, 10)
        if self.type == Qt.LeftEdge or self.type == Qt.RightEdge:
            self.midPanel.setGeometry(0, 10, self.weight, self.height() - 20)
            self.midPanel.setCursor(Qt.CursorShape.SizeHorCursor)
            self.afterPanel.setGeometry(0, self.height() - 10, 10, 10)
            
        elif self.type == Qt.TopEdge or self.type == Qt.BottomEdge:
            self.midPanel.setGeometry(10, 0, self.width() - 20, self.weight)
            self.midPanel.setCursor(Qt.CursorShape.SizeVerCursor)
            self.afterPanel.setGeometry(self.width() - 10, 0, 10, 10)

    
    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.resizeing = True
    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self.resizeing = False
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
       if self.resizeing:
            if self.midPanel.underMouse():
               print("mid")
            if self.beforePanel.underMouse():
                print("before")
            if self.afterPanel.underMouse():
                print("after")