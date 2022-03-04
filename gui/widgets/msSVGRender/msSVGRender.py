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
from modulos import msVariables

###########################################################################################################################
class msSVGRender(QFrame):
    def __init__(self, parent :str, File,
     largura = 25, altura = 25 , cor = "red"):
        super().__init__()
        self.file = File
        self.ownerDrawnerIcon = QPixmap()
        self.setParent(parent)
        self.mySize(largura, altura)
        self.cor(cor)
        self.myIcon(self.file)
        self.__privileges = [msVariables.admin]
        ####
###########################################################################################################################
########    PROPERTYS
###########################################################################################################################
###########################################################################################################################   
    @property
    def privileges(self):
        return self.__privileges
    @privileges.setter
    def privileges(self, value):
        if type(value) == 'str':
            self.__privileges.append(value)
        elif type(value) == 'list':
            self.__privileges.extend(value)
    @privileges.deleter
    def privileges(self, value):
        self.__privileges.remove(value)
########################################################################
####    SET SIZE OF THE SVG DISPLAYER
    def mySize(self, largura, altura):
        self.__largura = largura
        self.__altura = altura
        self.setMinimumSize(QSize(self.__largura, self.__altura))
        self.setMaximumSize(QSize(self.__largura, self.__altura))
        self.geometry().setSize(QSize(self.__largura, self.__altura))
####    SET THE COLOR FOR OUR SVG
    def cor(self, value: str):
        self.__cor = QColor(value)
####    DEFINE SOME ICON TO OUR SVG
    def myIcon(self, value :str):
        self.ownerDrawnerIcon = QPixmap(value)
        self.ownerDrawnerIcon = self.ownerDrawnerIcon.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
####    EVENT PAINT SVG ON PAINT EVENT
    def paintIconEvent(self, qp :QPainter, color):
        icon = self.ownerDrawnerIcon
        rect = QRect(0,0, self.width() / 2, self.height() / 2)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        qp.drawPixmap(self.width() - icon.width(), self.height() - icon.height(), icon)
        painter.end()
####    PAINT EVENT
    def paintEvent(self, event: QPaintEvent) -> None:
        QFrame.paintEvent(self, event)
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen) 
        if self.ownerDrawnerIcon:
            self.paintIconEvent(qp, self.__cor)
        qp.end()