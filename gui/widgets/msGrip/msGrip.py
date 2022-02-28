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

    def moveme(self, event):
        fSize = self.object.geometry()
        parsedX = parsedY = width = height = 0
        if self.type == Qt.TopEdge:
            if self.beforePanel.underMouse():
                width = (fSize.width() + abs(event.pos().x())) if event.pos().x() < 0 else (fSize.width() - event.pos().x())
                height = (fSize.height() + abs(event.pos().y())) if event.pos().y() < 0 else (fSize.height() - event.pos().y())
                parsedX = fSize.x() + event.pos().x()
                parsedY = fSize.y() + event.pos().y()
                if width < self.object.minimumWidth() or width > self.object.maximumWidth(): parsedX = fSize.x()
                if height < self.object.minimumHeight() or height > self.object.maximumHeight(): parsedY = fSize.y()
            elif self.midPanel.underMouse():
                width = fSize.width()
                height = (fSize.height() + abs(event.pos().y())) if event.pos().y() < 0 else (fSize.height() - event.pos().y())
                parsedX = fSize.x()
                parsedY = fSize.y() + event.pos().y()
                if height < self.object.minimumHeight() or height > self.object.maximumHeight(): parsedY = fSize.y()
            elif self.afterPanel.underMouse():
                width = fSize.width() + abs(self.width() - event.pos().x()) if self.width() - event.pos().x() < 0 else fSize.width() - (self.width() - event.pos().x())
                height = fSize.height() + abs(event.pos().y()) if event.pos().y() < 0 else fSize.height() - event.pos().y()
                parsedX = fSize.x()
                parsedY = fSize.y() + event.pos().y()
                if width < self.object.minimumWidth() or width > self.object.maximumWidth(): parsedX = fSize.x()
                if height < self.object.minimumHeight() or height > self.object.maximumHeight(): parsedY = fSize.y()
        elif self.type == Qt.BottomEdge:
            if self.beforePanel.underMouse():
                width = (fSize.width() + abs(event.pos().x())) if event.pos().x() < 0 else (fSize.width() - event.pos().x())
                width = self.object.minimumWidth() if width < self.object.minimumWidth() else width
                width = self.object.maximumWidth() if width > self.object.maximumWidth() else width
                height = fSize.height() + event.pos().y()
                height = self.object.minimumHeight() if height < self.object.minimumHeight() else height
                height = self.object.maximumHeight() if height > self.object.maximumHeight() else height
                parsedX = fSize.x() + event.pos().x()
                if width <= self.object.minimumWidth(): parsedX = fSize.x()
                parsedY = fSize.y()
            elif self.midPanel.underMouse():
                width = fSize.width()
                height = fSize.height() + event.pos().y()
                parsedX = fSize.x()
                parsedY = fSize.y()
                if height < self.object.minimumHeight() or height > self.object.maximumHeight(): parsedY = fSize.y()
            elif self.afterPanel.underMouse():
                width = fSize.width() + abs(self.width() - event.pos().x()) if self.width() - event.pos().x() < 0 else fSize.width() - (self.width() - event.pos().x())
                height = fSize.height() + event.pos().y()
                parsedX = fSize.x()
                parsedY = fSize.y()
                if width < self.object.minimumWidth() or width > self.object.maximumWidth(): parsedX = fSize.x()
                if height < self.object.minimumHeight() or height > self.object.maximumHeight(): parsedY = fSize.y()
        elif self.type == Qt.LeftEdge:
            if self.beforePanel.underMouse():
                width = (fSize.width() + abs(event.pos().x())) if event.pos().x() < 0 else (fSize.width() - event.pos().x())
                height = (fSize.height() + abs(event.pos().y())) if event.pos().y() < 0 else (fSize.height() - event.pos().y())
                parsedX = fSize.x() + event.pos().x()
                parsedY = fSize.y() + event.pos().y()
                if width < self.object.minimumWidth() or width > self.object.maximumWidth(): parsedX = fSize.x()
                if height < self.object.minimumHeight() or height > self.object.maximumHeight(): parsedY = fSize.y()
            elif self.midPanel.underMouse():
                width = (fSize.width() + abs(event.pos().x())) if event.pos().x() < 0 else (fSize.width() - event.pos().x())
                height = fSize.height()
                parsedX = fSize.x() + event.pos().x()
                parsedY = fSize.y()
                if width < self.object.minimumWidth() or width > self.object.maximumWidth(): parsedX = fSize.x()
                if height < self.object.minimumHeight() or height > self.object.maximumHeight(): parsedY = fSize.y()
            elif self.afterPanel.underMouse():
                width = (fSize.width() + abs(event.pos().x())) if event.pos().x() < 0 else (fSize.width() - event.pos().x())
                width = self.object.minimumWidth() if width < self.object.minimumWidth() else width
                width = self.object.maximumWidth() if width > self.object.maximumWidth() else width
                height = fSize.height() - (self.height() - event.pos().y())
                height = self.object.minimumHeight() if height < self.object.minimumHeight() else height
                height = self.object.maximumHeight() if height > self.object.maximumHeight() else height
                parsedX = fSize.x() + event.pos().x()
                if width <= self.object.minimumWidth(): parsedX = fSize.x()
                parsedY = fSize.y()
        elif self.type == Qt.RightEdge:
            if self.beforePanel.underMouse():
                width = fSize.width() + event.pos().x()
                height = fSize.height() + abs(event.pos().y()) if event.pos().y() < 0 else fSize.height() - event.pos().y()
                parsedX = fSize.x()
                parsedY = fSize.y() + event.pos().y()
                if width < self.object.minimumWidth() or width > self.object.maximumWidth(): parsedX = fSize.x()
                if height < self.object.minimumHeight() or height > self.object.maximumHeight(): parsedY = fSize.y()
            elif self.midPanel.underMouse():
                width = fSize.width() + abs(self.width() - event.pos().x()) if self.width() - event.pos().x() < 0 else fSize.width() - (self.width() - event.pos().x())
                height = fSize.height()
                parsedX = fSize.x()
                parsedY = fSize.y()
                if width < self.object.minimumWidth() or width > self.object.maximumWidth(): parsedX = fSize.x()
                if height < self.object.minimumHeight() or height > self.object.maximumHeight(): parsedY = fSize.y()
            elif self.afterPanel.underMouse():
                width = fSize.width() + event.pos().x()
                height = fSize.height() - (self.height() - event.pos().y())
                parsedX = fSize.x()
                parsedY = fSize.y()
                if width < self.object.minimumWidth() or width > self.object.maximumWidth(): parsedX = fSize.x()
                if height < self.object.minimumHeight() or height > self.object.maximumHeight(): parsedY = fSize.y()
        self.object.setGeometry(parsedX, parsedY, width, height)                
        self.object.update()

    def event(self, event: QEvent) -> bool:
        if event.type() == event.MouseButtonPress:  self.resizeing = True
        if event.type() == event.MouseButtonRelease: self.resizeing = False
        if event.type() == event.MouseMove: 
            if self.resizeing:
                self.moveme(event)
                
        msPanel.event(self, event)
        return True

