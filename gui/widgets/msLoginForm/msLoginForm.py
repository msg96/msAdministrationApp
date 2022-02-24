from required import *

class msLoginForm(QMainWindow):
    def __init__(self):
        super(msLoginForm, self).__init__()
        pass
        self.bar = QWidget()
        self.__moving = False
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        QMainWindow.mousePressEvent(self, event)
        if event.button() != Qt.MouseButton.LeftButton:
            return
        if self.windowState() != Qt.WindowNoState:
            return
        if self.bar.underMouse():
            self.__moving = True
            self.__GP = event.globalPos()

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        QMainWindow.mouseReleaseEvent(self, event)
        self.__moving = False

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        QMainWindow.mouseMoveEvent(self, event)
        if self.__moving:
            delta = QPoint(event.globalPos() - self.__GP)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.__GP = event.globalPos()
