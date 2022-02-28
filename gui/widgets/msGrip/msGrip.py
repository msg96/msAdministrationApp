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
    def __init__(self, parent: QWidget, object :QWidget,type :Qt.Edge, weidht = 3, colorizer=True):
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
        self.busy = False
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
        if self.type == Qt.LeftEdge:    self.setGeometry(0, self.weight, self.weight, self.parent.height() -  self.weight)

        if self.type == Qt.TopEdge:     self.setGeometry(0, 0, self.parent.width(), self.weight)
        if self.type == Qt.RightEdge:   self.setGeometry(self.parent.width() - self.weight, 0, self.weight, self.parent.height())

        if self.type == Qt.BottomEdge:  self.setGeometry(0, self.parent.height() - self.weight, self.parent.width(), self.weight)

        self.beforePanel.setGeometry(0, 0, 10, 10)
        if self.type == Qt.LeftEdge or self.type == Qt.RightEdge:
            self.midPanel.setGeometry(0, 10, self.weight, self.height() - 20)
            self.midPanel.setCursor(Qt.CursorShape.SizeHorCursor)
            self.afterPanel.setGeometry(0, self.height() - 10, 10, 10)
            
        elif self.type == Qt.TopEdge or self.type == Qt.BottomEdge:
            self.midPanel.setGeometry(10, 0, self.width() - 20, self.weight)
            self.midPanel.setCursor(Qt.CursorShape.SizeVerCursor)
            self.afterPanel.setGeometry(self.width() - 10, 0, 10, 10)

########    BEFORE MOVE
    def beforeMove(self, event: QEvent):
        formPos = self.object.geometry()
        um = Qt.BottomEdge
        dois = Qt.RightEdge
        tres = Qt.TopEdge
        quatro = Qt.LeftEdge
        if self.type == um:
            height = formPos.height() + event.pos().y()
            if event.pos().x() < 0: width = formPos.width() + abs(event.pos().x())
            else: width = formPos.width() - event.pos().x()
            parsedxpos = formPos.x() + event.pos().x()
            if width <= self.object.minimumWidth(): parsedxpos = formPos.x()
            elif width >= self.object.maximumWidth(): parsedxpos = formPos.x()
            self.object.setGeometry(parsedxpos, formPos.y(), width, height)
        elif self.type == dois:
            width = formPos.width() + event.pos().x()
            if event.pos().y() < 0: height = formPos.height() + abs(event.pos().y())
            else: height = formPos.height() - event.pos().y()
            parsedypos = formPos.y() + event.pos().y()
            if height <= self.object.minimumHeight(): parsedypos = formPos.y()
            elif height >= self.object.maximumHeight(): parsedypos = formPos.y()
            self.object.setGeometry(formPos.x(), parsedypos, width, height)
        elif self.type == tres or self.type == quatro:
            if event.pos().x() < 0: width = formPos.width() + abs(event.pos().x())
            else: width = formPos.width() - event.pos().x()
            if event.pos().y() < 0: height = formPos.height() + abs(event.pos().y())
            else: height = formPos.height() - event.pos().y()
            parsedxpos = formPos.x() + event.pos().x()
            if width <= self.object.minimumWidth(): parsedxpos = formPos.x()
            elif width >= self.object.maximumWidth(): parsedxpos = formPos.x()
            parsedypos = formPos.y() + event.pos().y()
            if height <= self.object.minimumHeight(): parsedypos = formPos.y()
            elif height >= self.object.maximumHeight(): parsedypos = formPos.y()
            self.object.setGeometry(parsedxpos, parsedypos, width, height)
        print("Before: {} - {} ".format(event.pos().x(), event.pos().y()))


########    MID MOVE
    def midMove(self, event: QEvent):
########
        formPos = self.object.geometry()
########    MID MOVE BY BOTTOM
        if self.type == Qt.BottomEdge:
            height = formPos.height() + event.pos().y()
            if height <= self.object.minimumHeight() or height >= self.object.maximumHeight():
                return
            self.object.setGeometry(formPos.x(), formPos.y(), formPos.width(), height)
########    MID MOVE BY RIGHT
        elif self.type == Qt.RightEdge:
            width = formPos.width() + event.pos().x()
            if width <= self.object.minimumWidth() or width >= self.object.maximumWidth():
                return
            self.object.setGeometry(formPos.x(), formPos.y(), width, formPos.height())
########    MID MOVE BY TOP
        elif self.type == Qt.TopEdge:
            if event.pos().y() < 0:
                height = formPos.height() + abs(event.pos().y())
            else:
                height = formPos.height() - event.pos().y()
            if height <= self.object.minimumHeight() or height >= self.object.maximumHeight():
                return
            self.object.setGeometry(formPos.x(), formPos.y() + event.pos().y(), formPos.width(), height)
########    MID MOVE BY LEFT
        elif self.type == Qt.LeftEdge:
            if event.pos().x() < 0:
                width = formPos.width() + abs(event.pos().x())
            else:
                width = formPos.width() - event.pos().x()
            if width <= self.object.minimumWidth() or width >= self.object.maximumWidth():
                return
            self.object.setGeometry(formPos.x() + event.pos().x(), formPos.y(), width, formPos.height())
        self.object.busy = False
########    AFTER MOVE
    def afterMove(self, event: QEvent):
        formPos = self.object.geometry()
        print("After: {} - {} ".format(event.pos().x(), event.pos().y()))

    def event(self, e: QEvent) -> bool:
        if e.type() == e.MouseButtonPress:  self.resizeing = True
        if e.type() == e.MouseButtonRelease: self.resizeing = False
        if e.type() == e.MouseMove: 
            if self.resizeing:
                if self.beforePanel.underMouse():
                    self.beforeMove(e)
                if self.midPanel.underMouse():
                    self.midMove(e)
                if self.afterPanel.underMouse():
                    self.afterMove(e)
        msPanel.event(self, e)
        return True

