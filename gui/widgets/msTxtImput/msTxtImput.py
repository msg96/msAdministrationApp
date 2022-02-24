import os
###########################################################################################################################
########    PYSIDE6 IMPORTS                             ~   * IMPORTANT
###########################################################################################################################
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *


def updateSVG(parca) -> str:
    if parca.SvgIconUrl == "":
        return QPixmap(None)
    svgPath = os.path.abspath(os.getcwd())
    svgPath = os.path.join(svgPath, "assets/svg")
    result = os.path.normpath(os.path.join(svgPath, parca.SvgIconUrl))
    parca.SvgIconUrl = result
    return QPixmap(result)
            

class MsTxtImput(QLineEdit):
    def __init__(self, SvgIconUrl) -> None:
        super(MsTxtImput, self).__init__()
        self.SvgIconUrl = SvgIconUrl
        self.SvgIconAlign = Qt.AlignLeft
        self.SvgIconColor = "red"
        self.SvgMargem = 10
        self.icon = updateSVG(self)
        self.setTextMargins(30,0,0,10)

    def paintIconEvent(self, qp :QPainter, color):
        xPos = 0
        if self.SvgIconAlign == Qt.AlignLeft:
            xPos = 0 + self.SvgMargem
        if self.SvgIconAlign == Qt.AlignCenter:
            xPos = (self.width() - self.icon.width()) / 2
        if self.SvgIconAlign == Qt.AlignRight:
            xPos = self.width() - self.SvgMargem - self.icon.width()

        yPos = (self.height() - self.icon.height()) / 2

        rect = QRect(xPos, yPos, 0,0)
        
        
        painter = QPainter(self.icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(self.icon.rect(), color)
        qp.drawPixmap(rect.x(), rect.y(), self.icon)
        painter.end()


    def paintEvent(self, event: QPaintEvent) -> None:
        QLineEdit.paintEvent(self, event)
        if self.SvgIconUrl == "":
            return

        color = self.SvgIconColor
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)
        self.paintIconEvent(qp, color)
        qp.end()