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
from re import S
from required import *
import sys
import modulos
from assets.styles import style
from modulos.msVariables import Svgs
###########################################################################################################################
########    CUSTOM WIDGETS AND QTDESIGNEDS IMPORTS
###########################################################################################################################
from gui.Interfaces.ui_v2 import uiV2
###########################################################################################################################
########    CLASS FOR OUR MAIN FORM APPLICATION
###########################################################################################################################
class myapp(msForm):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MS Administration")
        self.appWindow = uiV2()
        self.appWindow.start(self)
        self.lMenu = self.appWindow.leftModal.leftMenu
        self.ApplyStyleClick()
        self.loged = True
        self.__back1 = self.geometry()
        self.__back2 = self.minimumSize()
        self.__back3 = self.maximumSize()
        self.centerScreen = QApplication.primaryScreen().availableGeometry()
        # self.homeBtnClick()
        self.configBtnClick()
###########################################################################################################################
########    SET CLICK EVENTS
###########################################################################################################################
        self.appWindow.toggleLeftModalBtn.clicked.connect(self.toggleLeftModalClick)
        self.appWindow.toggleRightModalBtn.clicked.connect(self.toggleRightModalClick)
        self.appWindow.closeBtn.clicked.connect(self.closeBtnClick)
        self.appWindow.minimizeBtn.clicked.connect(self.minimizeBtnClick)
        self.appWindow.maximizeBtn.clicked.connect(self.maximizeBtnClick)
        self.appWindow.LoginUI.loginBtn.clicked.connect(self.loginBtnClick)
        self.appWindow.logOutBtn.clicked.connect(self.logoutBtnClick)
###########################################################################################################################
########    LEFT MENU
###########################################################################################################################
        self.lMenu.homeBtn.clicked.connect(self.homeBtnClick)
        self.lMenu.cloudBtn.clicked.connect(self.CcloudBtnClick)
        self.lMenu.configBtn.clicked.connect(self.configBtnClick)
###########################################################################################################################
########    CONFIG
        self.lmConfig = self.appWindow.configPage.leftMenu
###########################################################################################################################
        self.lmConfig.styleBtn.clicked.connect(self.styleBtnClick)
        self.lmConfig.secondBtn.clicked.connect(self.interopBtnClick)
###########################################################################################################################
###########################################################################################################################
        self.checkeLogin()
        self.myGrip = msGrip(self)
        self.show()
        self.user = 0


    def checkeLogin(self):
        self.appWindow.leftModal.setVisible(self.loged)
        self.appWindow.toggleLeftModalBtn.setVisible(self.loged)
        self.appWindow.toggleRightModalBtn.setVisible(self.loged)
        self.appWindow.maximizeBtn.setEnabled(self.loged)
        self.appWindow.LoginUI.body.setVisible(not self.loged)
        self.appWindow.contentPanel.setVisible(self.loged)
        self.appWindow.logOutBtn.setVisible(self.loged)
        if not self.loged:
            self.__back1 = self.geometry()
            self.__back2 = self.minimumSize()
            self.__back3 = self.maximumSize()
            self.setMinimumSize(550, 500)
            self.setMaximumSize(550, 500)
            self.setGeometry((self.centerScreen.width() - 550) / 2, (self.centerScreen.height() -  500) / 2 , 550, 500)
            self.appWindow.LoginUI.loginTxt.setFocus(Qt.FocusReason.TabFocusReason)
        else:
            self.setMinimumSize(self.__back2)
            self.setMaximumSize(self.__back3)
            self.setGeometry(self.__back1)
            self.homeBtnClick()

    def loginBtnClick(self):
        con = auth.login(login=self.appWindow.LoginUI.loginTxt.text(), password=self.appWindow.LoginUI.passwordTxt.text())
        hwnd_ = cripter.digest(hwnd.getHWND())
        if con and con[4] < 4 and hwnd_ in con[6]:
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
            elif not hwnd_ in con[6]:
                self.LoginFailed(2000, "Computador n??o autorizado.")
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
            if not self.appWindow.leftModal.isOpen:
                self.appWindow.leftModal.borderRadius(0, 0, 0, 0)
                self.appWindow.appWindow.borderRadius(0, 0, 0, 0)
            else:
                self.appWindow.leftModal.borderRadius(0, 0, 0, 0)
                self.appWindow.appWindow.borderRadius(0, 0, 0, 0)
        else:
            if not self.appWindow.leftModal.isOpen:
                self.appWindow.leftModal.borderRadius(style["topleftradius"], 0, 0, 0)
                self.appWindow.appWindow.borderRadius(style["topleftradius"], 0, 0, 0)
            else:
                self.appWindow.leftModal.borderRadius(style["topleftradius"], 0, 0, 0)
                self.appWindow.appWindow.borderRadius(style["topleftradius"], 0, 0, 0)

    def toggleLeftModalClick(self):
        self.appWindow.leftModal.toggle(self.appWindow.toggleLeftModalBtn)
        self.attCorner()
        
    def toggleRightModalClick(self):
        self.appWindow.rightModal.toggle(self.appWindow.toggleRightModalBtn)

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
            self.appWindow.maximizeBtn.setIcon(QIcon(Svgs['fullscreen_exit_white_48dp']))
        elif self.windowState() == Qt.WindowNoState:
            self.appWindow.maximizeBtn.setIcon(QIcon(Svgs['fullscreen_white_48dp']))
        self.myGrip.updateSize()
###########################################################################################################################
########    CLICK EVENTS
###########################################################################################################################
########    CLOSE
    def closeBtnClick(self):
        self.close()
########    MINIMIZE
    def minimizeBtnClick(self):
        self.setWindowState(Qt.WindowMinimized)
########    MAXIMIZE
    def maximizeBtnClick(self):
        if not self.loged: return
        if self.windowState() == Qt.WindowMaximized:
            self.setWindowState(Qt.WindowNoState)
        elif self.windowState() == Qt.WindowNoState:
            self.setWindowState(Qt.WindowMaximized)
        self.attCorner()
########    LEFTMENU HOMEBTN
    def homeBtnClick(self):
        if self.lMenu.homeBtn.actived: return
        self.lMenu.homeBtn.active()
        self.pageSelector("home")
########    LEFTMENU CLOUDBTN
    def CcloudBtnClick(self):
        if self.lMenu.cloudBtn.actived: return
        self.lMenu.cloudBtn.active()
        self.pageSelector("cloud")
########    LEFTMENU CONFIGBTN  
    def configBtnClick(self):
        if self.lMenu.configBtn.actived: return
        self.lMenu.configBtn.active()
        self.pageSelector("config")
########    CONFIG  STYLEBTN
    def styleBtnClick(self):
        if self.lmConfig.styleBtn.actived: return
        self.lmConfig.styleBtn.active()
        self.appWindow.configPage.content.displayPage("theme")
########    CONFIG  INTEROPBTN
    def interopBtnClick(self):
        if self.lmConfig.secondBtn.actived: return
        self.lmConfig.secondBtn.active()
        self.appWindow.configPage.content.displayPage("interop")

###########################################################################################################################
###########################################################################################################################
###########################################################################################################################


    def pageSelector(self, pageName):
        self.appWindow.contentPages.showPage(pageName)
        

    def ApplyStyleClick(self):      
        for i in self.appWindow.__dict__:
            try:
                i.applyStyles()
            except: 
                pass


from teste import subApp
testes = False

def loaders():
    modulos.LoadJsonStyle()
   

if __name__ == "__main__":
    if not testes:
        loaders()
        app = QApplication(sys.argv)
        app.setAttribute(Qt.AA_EnableHighDpiScaling)
        app.setAttribute(Qt.AA_UseHighDpiPixmaps)
        myApp = myapp()
        try:
            sys.exit(app.exec())
        except:
            exit()
    else:
        subApp()
        