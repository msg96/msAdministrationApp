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
from assets.styles import style
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
        self.loged = False
        self.__back1 = self.geometry()
        self.__back2 = self.minimumSize()
        self.__back3 = self.maximumSize()
        self.centerScreen = QApplication.primaryScreen().availableGeometry()
        self.appWindow.toggleLeftModalBtn.clicked.connect(self.toggleLeftModalClick)
        self.appWindow.toggleRightModalBtn.clicked.connect(self.toggleRightModalClick)
        self.appWindow.closeBtn.clicked.connect(self.closeBtnClick)
        self.appWindow.minimizeBtn.clicked.connect(self.minimizeBtnClick)
        self.appWindow.maximizeBtn.clicked.connect(self.maximizeBtnClick)
        self.appWindow.LoginUI.loginBtn.clicked.connect(self.loginBtnClick)
        self.appWindow.logOutBtn.clicked.connect(self.logoutBtnClick)
        self.appWindow.homeBtn.clicked.connect(self.homeBtnClick)
        self.checkeLogin()
        self.myGrip = msGrip(self)
        self.show()
        self.user = 0


    def checkeLogin(self):
        self.appWindow.leftModal.setVisible(self.loged)
        self.appWindow.rightModal.setVisible(self.loged)
        self.appWindow.toggleLeftModalBtn.setVisible(self.loged)
        self.appWindow.toggleRightModalBtn.setVisible(self.loged)
        self.appWindow.maximizeBtn.setEnabled(self.loged)
        self.appWindow.LoginUI.body.setVisible(not self.loged)
        self.appWindow.logOutBtn.setVisible(self.loged)
        if not self.loged:
            self.__back1 = self.geometry()
            self.__back2 = self.minimumSize()
            self.__back3 = self.maximumSize()
            self.setMinimumSize(550, 500)
            self.setMaximumSize(550, 500)
            self.setGeometry((self.centerScreen.width() - 550) / 2, (self.centerScreen.height() -  500) / 2 , 550, 500)
        else:
            self.setMinimumSize(self.__back2)
            self.setMaximumSize(self.__back3)
            self.setGeometry(self.__back1)


    def loginBtnClick(self):
        con = auth.login(login=self.appWindow.LoginUI.loginTxt.text(), password=self.appWindow.LoginUI.passwordTxt.text())
        if con and con[4] < 4:
            self.loged = True
            self.user = con
            self.checkeLogin()
        else:
            if self.loged:
                self.loged = False
            if not con:
                self.LoginFailed(2000, "Ocorreu um Erro ao logar!.")
            elif con[4] == 4:
                self.LoginFailed(2000, "Conta Bloqueada, entre em contato com o administrador!.")
            else:
                self.LoginFailed(2000, "Ocorreu um Erro ao logar!.")
        
        self.appWindow.LoginUI.loginTxt.setText("")
        self.appWindow.LoginUI.passwordTxt.setText("")

    def logoutBtnClick(self):
        self.loged = False
        self.checkeLogin()


#######     DISPLAY ERROR ON NOT HAVE MATCHED USER O PASS
    def LoginFailed(self, delayMs, displaytext):
        self.appWindow.LoginUI.displayLb.setText(displaytext)
        self.__old = self.appWindow.LoginUI.displayLb.windowOpacity()
        self.appWindow.LoginUI.displayLb.setWindowOpacity(1)
        self.Annimation = QPropertyAnimation(self.appWindow.LoginUI.displayLb, b"windowOpacity")
        self.Annimation.setDuration(delayMs)
        self.Annimation.setStartValue(self.__old)
        self.Annimation.setEndValue(0)
        self.Annimation.finished.connect(self.__EndFailed)
        self.Annimation.setEasingCurve(QEasingCurve.OutInBounce)
        self.Annimation.start()
#    
    def __EndFailed(self):
        self.appWindow.LoginUI.displayLb.setText("")
        self.appWindow.LoginUI.displayLb.setWindowOpacity(self.__old)

    def attCorner(self):
        if self.windowState() == Qt.WindowMaximized:
            if not self.appWindow.leftModalOpen:
                self.appWindow.leftModal.borderRadius(0, 0, 0, 0)
                self.appWindow.appWindow.borderRadius(0, 0, 0, 0)
            else:
                self.appWindow.leftModal.borderRadius(0, 0, 0, 0)
                self.appWindow.appWindow.borderRadius(0, 0, 0, 0)
        else:
            if not self.appWindow.leftModalOpen:
                self.appWindow.leftModal.borderRadius(style["topleftradius"], 0, 0, 0)
                self.appWindow.appWindow.borderRadius(style["topleftradius"], 0, 0, 0)
            else:
                self.appWindow.leftModal.borderRadius(style["topleftradius"], 0, 0, 0)
                self.appWindow.appWindow.borderRadius(style["topleftradius"], 0, 0, 0)


    def toggleLeftModalClick(self):
        if self.appWindow.leftModalAnimation.state() != self.appWindow.leftModalAnimation.Stopped:
            return
        if self.appWindow.leftModalOpen:
            self.appWindow.leftModalOpen = False
            self.appWindow.toggleLeftModalBtn.setIcon(self.appWindow.MenuIcon)
            self.appWindow.toggleLeftModalBtn.backgroundColor(style["secondarybg"])
            self.appWindow.toggleLeftModalBtn.hoverBackgroundColor(style["hoverbtns"])
            self.appWindow.leftModalAnimation.setDirection(self.appWindow.leftModalAnimation.Backward)
            self.appWindow.leftModalAnimation.start()
        else:
            self.appWindow.leftModalOpen = True
            self.appWindow.toggleLeftModalBtn.setIcon(self.appWindow.MenuLeftOpenIcon)
            self.appWindow.toggleLeftModalBtn.backgroundColor(style["secondarybg"])
            self.appWindow.toggleLeftModalBtn.hoverBackgroundColor(style["hoverbtns"])
            self.appWindow.leftModalAnimation.setDirection(self.appWindow.leftModalAnimation.Forward)
            self.appWindow.leftModalAnimation.start()
        self.attCorner()
        
    def toggleRightModalClick(self):
        if self.appWindow.rightModalOpen:
            self.appWindow.rightModalOpen = False
            self.appWindow.toggleRightModalBtn.setIcon(self.appWindow.MenuIcon)
            self.appWindow.toggleRightModalBtn.backgroundColor(style["secondarybg"])
            self.appWindow.toggleRightModalBtn.hoverBackgroundColor(style["hoverbtns"])
            self.appWindow.rightModalAnimation.setDirection(self.appWindow.rightModalAnimation.Backward)
            self.appWindow.rightModalAnimation.start()     
        else:
            self.appWindow.rightModalOpen = True
            self.appWindow.toggleRightModalBtn.setIcon(self.appWindow.menuRightOpenIcon)
            self.appWindow.toggleRightModalBtn.backgroundColor(style["hoverbtns"])
            self.appWindow.toggleRightModalBtn.hoverBackgroundColor(style["hoverbtns"])
            self.appWindow.rightModalAnimation.setDirection(self.appWindow.rightModalAnimation.Forward)
            self.appWindow.rightModalAnimation.start()

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        msForm.eventFilter(self, watched, event)
        
    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        if not self.loged: return
        if event.button() != Qt.LeftButton: return
        if self.bar.underMouse():
            self.maximizeBtnClick()
           
    def resizeEvent(self, event: QResizeEvent) -> None:
        msForm.resizeEvent(self, event)
        if self.isMaximized():
            self.myGrip.setVisible(False)
        else:
            self.myGrip.setVisible(self.loged)

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
        if not self.loged: return
        if self.windowState() == Qt.WindowMaximized:
            self.setWindowState(Qt.WindowNoState)
        elif self.windowState() == Qt.WindowNoState:
            self.setWindowState(Qt.WindowMaximized)
        self.attCorner()

    def event(self, event: QEvent) -> None:
        if event.type() == event.WindowStateChange:
            self.anim = QPropertyAnimation(self, b"windowOpacity")
            self.anim.setDuration(self.appWindow.AnimDelay)
            self.old_ = self.windowOpacity()
            self.anim.setStartValue(self.old_)
            self.anim.setEndValue(0)
            self.anim.setEasingCurve(self.appWindow.AnimCurve)
            self.anim.finished.connect(self.backopacity)
            self.anim.start()

        QMainWindow.event(self, event)
        return True

    def backopacity(self):
        self.setWindowOpacity(self.old_)

    def homeBtnClick(self):
        if self.appWindow.homeBtn.actived: return
        self.appWindow.homeBtn.active()
from teste import subApp
testes = False

if __name__ == "__main__":
    if not testes:
        app = QApplication(sys.argv)
        myApp = myapp()
        try:
            sys.exit(app.exec())
        except:
            exit()
    else:
        subApp()