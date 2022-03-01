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

class msGrip(QObject):
    def __init__(self, parent :QObject, weight = 10) -> None:
        self.parent = parent
        self.weight = weight
        self.colorize(False)
        self.initiGrips()

    class Grip(msPanel):
        def __init__(self, parent: QWidget, section :Qt.WindowFrameSection, weight :int, color = "Transparent"):
            super().__init__(parent)
            self.setParent(parent)
            self.section = section
            self.weight = weight
            self.backgroundColor(color)
            self.getCursor()
            self.moving = False

            if section == Qt.TopLeftSection or section == Qt.TopRightSection or section == Qt.BottomRightSection or section == Qt.BottomLeftSection:
                self.sub = QSizeGrip(self)
                self.sub.setStyleSheet("background-color: Transparent")

########    DEFINE GRIP CURSOR
        def getCursor(self):
            if self.section == Qt.TopLeftSection : self.setCursor(Qt.CursorShape.SizeFDiagCursor)
            if self.section == Qt.TopSection : self.setCursor(Qt.CursorShape.SizeVerCursor)
            if self.section == Qt.TopRightSection : self.setCursor(Qt.CursorShape.SizeBDiagCursor)
            if self.section == Qt.RightSection : self.setCursor(Qt.CursorShape.SizeHorCursor)
            if self.section == Qt.BottomRightSection : self.setCursor(Qt.CursorShape.SizeFDiagCursor)
            if self.section == Qt.BottomSection : self.setCursor(Qt.CursorShape.SizeVerCursor)
            if self.section == Qt.BottomLeftSection : self.setCursor(Qt.CursorShape.SizeBDiagCursor)
            if self.section == Qt.LeftSection : self.setCursor(Qt.CursorShape.SizeHorCursor)
########    RESIZE A GRIP CORRECTLY
        def updateSize(self):
            if self.section == Qt.TopLeftSection: self.setGeometry(0, 0, self.weight, self.weight)
            if self.section == Qt.TopSection: self.setGeometry(0 + self.weight, 0, self.parent().width() - self.weight * 2, self.weight)
            if self.section == Qt.TopRightSection: self.setGeometry(self.parent().width() - self.weight, 0, self.weight, self.weight)
            if self.section == Qt.RightSection: self.setGeometry(self.parent().width() - self.weight, self.weight, self.weight, self.parent().height() - self.weight * 2)
            if self.section == Qt.BottomRightSection: self.setGeometry(self.parent().width() - self.weight, self.parent().height() - self.weight, self.weight, self.weight)
            if self.section == Qt.BottomSection: self.setGeometry(self.weight, self.parent().height() - self.weight, self.parent().width() - self.weight * 2, self.weight)
            if self.section == Qt.BottomLeftSection: self.setGeometry(0, self.parent().height() - self.weight, self.weight, self.weight)
            if self.section == Qt.LeftSection: self.setGeometry(0, self.weight, self.weight,  self.parent().height() - self.weight * 2)

        def mousePressEvent(self, event: QMouseEvent) -> None:
            if event.button() != Qt.MouseButton.LeftButton:
                return False
            self.moving = True
        def mouseReleaseEvent(self, event: QMouseEvent) -> None:
            if event.button() != Qt.MouseButton.LeftButton:
                return False
            self.moving = False
        def mouseMoveEvent(self, event: QMouseEvent) -> None:
            if not self.moving: return
            if self.section == Qt.TopSection:
                delta = event.pos()
                height = max(self.parent().minimumHeight(), self.parent().height() - delta.y())
                geo = self.parent().geometry()
                geo.setTop(geo.bottom() - height)
                self.parent().setGeometry(geo)
            elif self.section == Qt.RightSection:
                delta = event.pos()
                width = max(self.parent().minimumWidth(), self.parent().width() + delta.x())
                if width > self.parent().minimumWidth() or width < self.parent().maximumWidth():
                    self.parent().resize(width, self.parent().height())
            elif self.section == Qt.BottomSection:
                delta = event.pos()
                height = max(self.parent().minimumHeight(), self.parent().height() + delta.y())
                self.parent().resize(self.parent().width(), height)
            elif self.section == Qt.LeftSection:
                delta = event.pos()
                width = max(self.parent().minimumWidth(), self.parent().width() - delta.x())
                geo = self.parent().geometry()
                geo.setLeft(geo.right() - width)
                self.parent().setGeometry(geo)

#################################################################################################
####    INITIALIZATE THE ALL GRIPS                                                              #
    def initiGrips(self):
        self.TopLeftGrip = self.Grip(self.parent, Qt.TopLeftSection, self.weight, self.color1)
        self.TopGrip = self.Grip(self.parent, Qt.TopSection, self.weight, self.color2)
        self.TopRightGrip = self.Grip(self.parent, Qt.TopRightSection, self.weight, self.color1)
        self.RightGrip = self.Grip(self.parent, Qt.RightSection, self.weight, self.color2)
        self.BottomRightGrip = self.Grip(self.parent, Qt.BottomRightSection, self.weight, self.color1)
        self.BottomGrip = self.Grip(self.parent, Qt.BottomSection, self.weight, self.color2)
        self.BottomLeftGrip = self.Grip(self.parent, Qt.BottomLeftSection, self.weight, self.color1)
        self.LeftGrip = self.Grip(self.parent, Qt.LeftSection, self.weight, self.color2)
####    COLORIZED                                                                               #
    def colorize(self, value :bool):
        self.color1 = "RED" if value else "Transparent"
        self.color2 = "Blue" if value else "Transparent"
####    UPDATESIZE                                                                              #
    def updateSize(self):
        self.TopLeftGrip.updateSize()
        self.TopGrip.updateSize()
        self.TopRightGrip.updateSize()
        self.RightGrip.updateSize()
        self.BottomRightGrip.updateSize()
        self.BottomGrip.updateSize()
        self.BottomLeftGrip.updateSize()
        self.LeftGrip.updateSize()
#################################################################################################

    def setVisible(self, value):
        self.TopLeftGrip.setVisible(value)
        self.TopGrip.setVisible(value)
        self.TopRightGrip.setVisible(value)
        self.RightGrip.setVisible(value)
        self.BottomRightGrip.setVisible(value)
        self.BottomGrip.setVisible(value)
        self.BottomLeftGrip.setVisible(value)
        self.LeftGrip.setVisible(value)