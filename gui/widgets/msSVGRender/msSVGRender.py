from unittest import result
from required import *
import os

class msSVGRender(QFrame):
    def __init__(self, parent :str, File = "",
     largura = 25, Altura = 25 , Cor = "red", Composition = True):
        super().__init__()
        self.file = File
        #self.setParent(parent)
        self.__absPathFile = self.updateSVG()
        self.largura = largura
        self.geometry().setWidth(self.largura)
        self.altura = Altura
        self.geometry().setHeight(self.altura)
        self.cor = Cor
        self.composition = Composition
        self.Alinhamento = Qt.AlignLeft
        self.margemLR = 10
        ## Qt.RightEdge or Qt.CenterEdge
    def updateSVG(self) -> str:
        if self.file == "":
            return ""
        __svgPath = os.path.abspath(os.getcwd())
        __svgPath = os.path.join(__svgPath, "assets/svg")
        result = os.path.normpath(os.path.join(__svgPath, self.file))
        self.__Icon = QPixmap(result)
        return result



    def paintIconEvent(self, qp :QPainter, color):
        xPos = 0
        if self.Alinhamento == Qt.AlignLeft:
            xPos = 0 + self.margemLR
        if self.Alinhamento == Qt.AlignCenter:
            xPos = (self.width() - self.__Icon.width()) / 2
        if self.Alinhamento == Qt.AlignRight:
            xPos = self.width() - self.margemLR - self.__Icon.width()

        yPos = (self.height() - self.__Icon.height()) / 2

        rect = QRect(xPos, yPos, 0,0)
        
        
        painter = QPainter(self.__Icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(self.__Icon.rect(), color)
        qp.drawPixmap(rect.x(), rect.y(), self.__Icon)
        painter.end()


    def paintEvent(self, event: QPaintEvent) -> None:
        QFrame.paintEvent(self, event)
        if self.file == "" or not self.__Icon:
            return

        color = self.cor
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)
        self.paintIconEvent(qp, color)
        qp.end()