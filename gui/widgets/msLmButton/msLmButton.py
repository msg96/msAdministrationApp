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
from assets.styles import style
################################
#### widget pai ################
from ..msButton import msButton
###########################################################################################################################

class msLmButton(msButton):
    def __init__(self, parent :QWidget):
        super(msLmButton, self).__init__(parent)
        if not self.objectName():
            self.setObjectName(str(hash(self)))
        try:
            self.setParent(parent)
            self.setGeometry(parent.geometry())
        except:
            pass
        self.iconleft = 50
        self.actived = False
        self.ownerDrawnerIcon = QPixmap()
        self.activebarColor = "transparent"

    def padronizerBtnLeftMenu(self):
        self.setMaximumHeight(style["topbarheight"])
        self.setMinimumHeight(style["topbarheight"])
        self.paddingLeft(52)
        self.textAlign("left")
        self.color("#CDCDCD")
        self.backgroundColor("transparent")
        self.hoverBackgroundColor(style["hoverbtns"])
        self.border(0, "none", "transparent")
        self.borderRadius(0, 0, 0, 0)
        self.hoverBorder(0,"none", "Transparent")
        self.activebarColor = style["primarybg"] 

    def active(self):

        for i in self.parent().children():
            if i == self:
                self.backgroundColor(style["primarybg"])
                self.border(0, "none", "transparent")
                self.hoverBackgroundColor(style["primarybg"])
                self.hoverBorder(0, "none", "transparent")
                self.borderLeft(2, "solid", style["hoverbtns"] )
                self.hoverBorderLeft(2, "solid", style["hoverbtns"] )
                self.borderRadius(15, 0, 0 , 15)
                self.updateStyles()
            else:
                try:
                   
                    i.actived = False
                    i.padronizerBtnLeftMenu()

                except:
                    pass

    def paintIconEvent(self, qp :QPainter, color):

        icon = self.ownerDrawnerIcon

        _w = self.iconleft
        _x = 0
        rect = QRect(0,0, _w, self.height())
        
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        qp.drawPixmap((rect.width() - icon.width()) / 2, (rect.height() - icon.height()) / 2 , icon)
        painter.end()

    def myIcon(self, value :str):
        self.ownerDrawnerIcon = QPixmap(value)

    def paintEvent(self, event: QPaintEvent) -> None:
        QPushButton.paintEvent(self, event)


        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen) 
        if self.ownerDrawnerIcon:
            self.paintIconEvent(qp, style["textcolor"])

        if self.actived:
            qp.setBrush(QBrush(self.activebarColor, Qt.BrushStyle.SolidPattern))
            qp.drawRect(self.width() - 5, 0, 5, self.height()) 
        qp.end()
