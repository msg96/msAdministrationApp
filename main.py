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
########    IMPORTS
###########################################################################################################################
import sys
from gui.Interfaces.ui_v2.ui_v2 import uiV2
from required import *
###########################################################################################################################
########    CUSTOM WIDGETS AND QTDESIGNEDS IMPORTS
###########################################################################################################################
###########################################################################################################################
########    CLASS FOR OUR MAIN FORM APPLICATION
###########################################################################################################################
class myapp(msForm):
    def __init__(self):
        super().__init__()
        self.appWindow = uiV2()
        self.appWindow.start(self)

        self.appWindow.toggleLeftModalBtn.clicked.connect(self.toggleLeftModalClick)
        self.appWindow.toggleRightModalBtn.clicked.connect(self.toggleRightModalClick)
        self.appWindow.closeBtn.clicked.connect(self.closeBtnClick)
        self.appWindow.minimizeBtn.clicked.connect(self.minimizeBtnClick)
        self.appWindow.maximizeBtn.clicked.connect(self.maximizeBtnClick)
        self.myGrip = msGrip(self)
        self.show()

    def attCorner(self):
        if self.windowState() == Qt.WindowMaximized:
            if not self.appWindow.leftModalOpen:
                self.appWindow.toggleLeftModalBtn.borderRadius(0, 0, 0, 0)
                self.appWindow.leftModal.borderRadius(0, 0, 0, 0)
                self.appWindow.appWindow.borderRadius(0, 0, 0, 0)
                self.appWindow.topBar.borderRadius(0, 0, 0, 0)
            else:
                self.appWindow.toggleLeftModalBtn.borderRadius(0, 15, 0, 0)
                self.appWindow.leftModal.borderRadius(0, 0, 0, 0)
                self.appWindow.appWindow.borderRadius(0, 0, 0, 0)
                self.appWindow.topBar.borderRadius(0, 0, 0, 0)
        else:
            if not self.appWindow.leftModalOpen:
                self.appWindow.toggleLeftModalBtn.borderRadius(15, 0, 0, 0)
                self.appWindow.leftModal.borderRadius(15, 0, 0, 0)
                self.appWindow.appWindow.borderRadius(15, 0, 0, 0)
                self.appWindow.topBar.borderRadius(15, 0, 0, 0)
            else:
                self.appWindow.toggleLeftModalBtn.borderRadius(0, 15, 0, 0)
                self.appWindow.leftModal.borderRadius(15, 0, 0, 0)
                self.appWindow.appWindow.borderRadius(15, 0, 0, 0)
                self.appWindow.topBar.borderRadius(15, 0, 0, 0)

    def toggleLeftModalClick(self):
        if self.appWindow.leftModalAnimation.state() != self.appWindow.leftModalAnimation.Stopped:
            return
        if self.appWindow.leftModalOpen:
            self.appWindow.leftModalOpen = False
            self.appWindow.toggleLeftModalBtn.setIcon(self.appWindow.MenuIcon)
            self.appWindow.toggleLeftModalBtn.backgroundColor("#050505")
            self.appWindow.toggleLeftModalBtn.hoverBackgroundColor("#66111111")
            self.appWindow.leftModalAnimation.setDirection(self.appWindow.leftModalAnimation.Backward)
            self.appWindow.leftModalAnimation.start()
        else:
            self.appWindow.leftModalOpen = True
            self.appWindow.toggleLeftModalBtn.setIcon(self.appWindow.MenuLeftOpenIcon)
            self.appWindow.toggleLeftModalBtn.backgroundColor("#111111")
            self.appWindow.toggleLeftModalBtn.hoverBackgroundColor("#AA111111")
            self.appWindow.leftModalAnimation.setDirection(self.appWindow.leftModalAnimation.Forward)
            self.appWindow.leftModalAnimation.start()
        self.attCorner()
        
    def toggleRightModalClick(self):
        if self.appWindow.rightModalOpen:
            self.appWindow.rightModalOpen = False
            self.appWindow.toggleRightModalBtn.setIcon(self.appWindow.MenuIcon)
            self.appWindow.toggleRightModalBtn.backgroundColor("#090909")
            self.appWindow.toggleRightModalBtn.hoverBackgroundColor("#66111111")
            self.appWindow.toggleRightModalBtn.borderRadius(15, 0, 0, 0)
            self.appWindow.rightModalAnimation.setDirection(self.appWindow.rightModalAnimation.Backward)
            self.appWindow.rightModalAnimation.start()
            
        else:
            self.appWindow.rightModalOpen = True
            self.appWindow.toggleRightModalBtn.setIcon(self.appWindow.menuRightOpenIcon)
            self.appWindow.toggleRightModalBtn.backgroundColor("#111111")
            self.appWindow.toggleRightModalBtn.hoverBackgroundColor("#AA111111")
            self.appWindow.toggleRightModalBtn.borderRadius(15, 0, 0, 0)
            self.appWindow.rightModalAnimation.setDirection(self.appWindow.rightModalAnimation.Forward)
            self.appWindow.rightModalAnimation.start()

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        msForm.eventFilter(self, watched, event)
        
    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        msForm.mouseDoubleClickEvent(self, event)
        
        self.attCorner()

    def resizeEvent(self, event: QResizeEvent) -> None:
        msForm.resizeEvent(self, event)
        if self.isMaximized():
            self.myGrip.setVisible(False)
        else:
            self.myGrip.setVisible(True)

        if self.windowState() == Qt.WindowMaximized:
            self.appWindow.maximizeBtn.setIcon(self.appWindow.maximizeIconOn)
        elif self.windowState() == Qt.WindowNoState:
            self.appWindow.maximizeBtn.setIcon(self.appWindow.maximizeIconOff)
        self.myGrip.updateSize()

    
    def closeBtnClick(self):
        self.close()

    def minimizeBtnClick(self):
        self.setWindowState(Qt.WindowMinimized)

    def maximizeBtnClick(self):
        if self.windowState() == Qt.WindowMaximized:
            self.setWindowState(Qt.WindowNoState)
        elif self.windowState() == Qt.WindowNoState:
            self.setWindowState(Qt.WindowMaximized)

    def event(self, event: QEvent) -> None:
        if event.type() == event.WindowStateChange:
            self.anim = QPropertyAnimation(self, b"windowOpacity")
            self.anim.setDuration(self.appWindow.AnimDelay)
            self.old_ = self.windowOpacity()
            self.anim.setStartValue(self.old_)
            self.anim.setEndValue(0)
            self.anim.setEasingCurve(QEasingCurve.Linear)
            self.anim.finished.connect(self.backopacity)
            self.anim.start()

        QMainWindow.event(self, event)
        return True

    def backopacity(self):
        self.setWindowOpacity(self.old_)

from teste import subApp
testes = False

if __name__ == "__main__":
    if not testes:
        app = QApplication(sys.argv)
        myApp = myapp()
        try:
            sys.exit(app.exec())
        except:
            print("Some error ocurred!.")
            exit()
    else:
        subApp()