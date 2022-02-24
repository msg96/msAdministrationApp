###########################################################################################################################
########    IMPORTS
###########################################################################################################################
import sys
from gui import widgets
import modulos
from required import *
###########################################################################################################################
########    CUSTOM WIDGETS AND QTDESIGNEDS IMPORTS
###########################################################################################################################
from gui.widgets import  msLoginForm


###########################################################################################################################
########    CLASS FOR OUR MAIN FORM APPLICATION
###########################################################################################################################
class loginApp(msLoginForm):
    def __init__(self):
        super().__init__()

###########################################################################################################################
########    SETTING INITIALIZATION PARAMETERS
###########################################################################################################################
########                        e##########################################################################################
        # CHAMADA DO MAINFORM #     
        self.UI = uiMain()
        self.UI.setupUi(self)
        ######################
        #
        self.UI.ErroMsg.setWindowOpacity(1)
        self.p = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        x = (self.p.x() - (self.width() / 2))
        y = (self.p.y() - (self.height() / 2))
        self.move(x,y)
        self.bar = self.UI.TopBarCenter
        self.AnniDuration = 300
        self.logado = False
        self.setWindowOpacity(0.97)
#
###########################################################################################################################
########    FIRST CHECK IF LOGEDIN
###########################################################################################################################
        self.CheckLogin()
#
###########################################################################################################################
########    SETTING CLICK EVENTS
###########################################################################################################################
        self.UI.MinimizeBtn.clicked.connect(self.Minimizeme)
        self.UI.MaximizeBtn.clicked.connect(self.Maxmizeme)
        self.UI.CloseBtn.clicked.connect(self.Closeme)
        self.UI.ToggleLeftBtn.clicked.connect(self.LeftMenuTogglerClick)
        self.UI.ToggleRightBtn.clicked.connect(self.RightMenuTogglerClick)
        self.UI.LoginBtn.clicked.connect(self.LoginBtnClick)
#
###########################################################################################################################
########    SHOW APP SCREEN
###########################################################################################################################
        self.show()
#
###########################################################################################################################
########    LOAD ANNIMATION FOR FIRST DISPLAY SCREEN
###########################################################################################################################
        self.Annimation =  QPropertyAnimation(self, b"windowOpacity")
        self.Annimation.setStartValue(0)
        self.Annimation.setEndValue(self.windowOpacity())
        self.Annimation.setDuration(500)
        self.Annimation.setEasingCurve(QEasingCurve.OutBack)
        self.Annimation.start()
#
###########################################################################################################################
########    EVENT TO CHECK LOGIN                                ~    NEED REFACTORING
###########################################################################################################################
    def CheckLogin(self):
        self.p = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        gin = QRect()
        if not self.logado:
            self.UI.MaximizeBtn.setEnabled(False)
            self.UI.centralwidget.setMinimumWidth(500)
            self.UI.centralwidget.setMinimumHeight(600)
            self.UI.centralwidget.setMaximumWidth(500)
            self.UI.centralwidget.setMaximumHeight(600)
            x = (self.p.x() - (500 / 2))
            y = (self.p.y() - (600 / 2))
            self.move(x,y)
            gin.setRect(x,y,500, 600)
            #self.setGeometry(0,0,500, 600)
            self.UI.ToggleLeftBtn.setVisible(False)
            self.UI.ToggleRightBtn.setVisible(False)
            self.UI.Paginas.setCurrentIndex(0)
            self.UI.TitlePages.setText("Login")
         
        else:
            self.UI.MaximizeBtn.setEnabled(True)
            self.UI.centralwidget.setMinimumWidth(900)
            self.UI.centralwidget.setMinimumHeight(550)
            self.UI.centralwidget.setMaximumWidth(9999)
            self.UI.centralwidget.setMaximumHeight(9999)
            x = (self.p.x() - (900 / 2))
            y = (self.p.y() - (550 / 2))
            self.move(x, y)
            gin.setRect(x,y,900, 550)
            #self.setGeometry(0,0,900, 550)
            self.UI.ToggleLeftBtn.setVisible(True)
            self.UI.ToggleRightBtn.setVisible(True)
            self.UI.TitlePages.setText("Inicio")
            self.UI.Paginas.setCurrentIndex(1)

        self.Annimation = QPropertyAnimation(self, b"geometry")
        self.Annimation.setStartValue(self.geometry())
        self.Annimation.setEndValue(gin)
        self.Annimation.setDuration(self.AnniDuration)
        self.Annimation.setEasingCurve(QEasingCurve.Linear)
        self.Annimation.start()
#
###########################################################################################################################
########    MINIMIZE EVENT                                      ~   NEED BETTER EFFECTS
###########################################################################################################################
    def Minimizeme(self):
        self.__backop = self.geometry()
        self.Annimation = QPropertyAnimation(self, b"geometry")
        self.Annimation.setStartValue(self.geometry())
        self.xxz = QScreen.availableGeometry(QApplication.primaryScreen()).x() / 2
        self.yyz = QScreen.availableGeometry(QApplication.primaryScreen()).y() 
        self.Annimation.setEndValue(QRect(self.width(),self.height(),0,0))
        self.Annimation.setDuration(self.AnniDuration)
        self.Annimation.setEasingCurve(QEasingCurve.BezierSpline)
        self.Annimation.start()
        self.Annimation.finished.connect(self.__afterMin)
#
    def __afterMin(self):
        self.setWindowState(Qt.WindowMinimized)
        self.setGeometry(self.__backop)
#
###########################################################################################################################
########    DOUBLE CLICK EVENT
###########################################################################################################################
    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        msLoginForm.mouseDoubleClickEvent(self, event)
        if event.button() != Qt.MouseButton.LeftButton:
            return
        if not self.bar.underMouse():
            return
        self.Maxmizeme()
#
###########################################################################################################################
########    MAXIMIZE EVENT                                      ~   NEED BETTER EFFECTS
###########################################################################################################################
    def Maxmizeme(self):
        if not self.logado:
            return
        self.__backop = self.windowOpacity()
        self.Annimation = QPropertyAnimation(self, b"windowOpacity")
        self.Annimation.setStartValue(self.__backop)
        self.Annimation.setEndValue(0)
        self.Annimation.setDuration(self.AnniDuration)
        self.Annimation.setEasingCurve(QEasingCurve.BezierSpline)
        self.Annimation.start()
        self.Annimation.finished.connect(self.__afterMax)
#
    def __afterMax(self):
        if self.windowState() == Qt.WindowMaximized:
            self.setWindowState(Qt.WindowNoState)
            self.UI.MaximizeBtn.setChecked(False)
        else:
            self.setWindowState(Qt.WindowMaximized)
            self.UI.MaximizeBtn.setChecked(True)
        self.Annimation = QPropertyAnimation(self, b"windowOpacity")
        self.Annimation.setStartValue(0)
        self.Annimation.setEndValue(self.__backop)
        self.Annimation.setDuration(self.AnniDuration)
        self.Annimation.setEasingCurve(QEasingCurve.BezierSpline)
        self.Annimation.start()
        self.perform()
#
###########################################################################################################################
########    CLOSE EVENT                                         ~   NEED BETTER EFFECTS
###########################################################################################################################
    def Closeme(self):
        self.__backop = self.windowOpacity()
        self.Annimation = QPropertyAnimation(self, b"windowOpacity")
        self.Annimation.setStartValue(self.__backop)
        self.Annimation.setEndValue(0)
        self.Annimation.setDuration(self.AnniDuration)
        self.Annimation.setEasingCurve(QEasingCurve.BezierSpline)
        self.Annimation.start()
        self.Annimation.finished.connect(self.__afterClose)
#
    def __afterClose(self):
        self.close()
#
###########################################################################################################################
########    CLICK TOGGLELEFTBTN                                 ~   NEED BETTER EFFECTS
###########################################################################################################################
    def LeftMenuTogglerClick(self):
        if self.UI.LeftModal.minimumWidth()  == 0:
            self.UI.ToggleLeftBtn.setObjectName("ToggleLeftBtnOpen")
            self.UI.ToggleLeftBtn.setChecked(True)
            self.UI.TopBar.setObjectName("TopBarOpen")
            self.Annimation = QPropertyAnimation(self.UI.LeftModal, b"minimumWidth")
            self.Annimation.setStartValue(0)
            self.Annimation.setEndValue(200)
            self.Annimation.setDuration(self.AnniDuration)
            self.Annimation.setEasingCurve(QEasingCurve.BezierSpline)
            self.Annimation.start()
        else:
            self.UI.ToggleLeftBtn.setObjectName("ToggleLeftBtn")
            self.UI.ToggleLeftBtn.setChecked(False)
            self.UI.TopBar.setObjectName("TopBar")
            self.Annimation = QPropertyAnimation(self.UI.LeftModal, b"minimumWidth")
            self.Annimation.setStartValue(200)
            self.Annimation.setEndValue(0)
            self.Annimation.setDuration(self.AnniDuration)
            self.Annimation.setEasingCurve(QEasingCurve.BezierSpline)
            self.Annimation.start()
        self.perform()
#
###########################################################################################################################
########    CLICK TOGGLERIGHTBNT                                ~   NEED BETTER EFFECTS
###########################################################################################################################
    def RightMenuTogglerClick(self):
        if self.UI.RightModal.minimumWidth()  == 0:
            self.UI.ToggleRightBtn.setObjectName("ToggleRightBtnOpen")
            self.UI.ToggleRightBtn.setChecked(True)
            self.Annimation = QPropertyAnimation(self.UI.RightModal, b"minimumWidth")
            self.Annimation.setStartValue(0)
            self.Annimation.setEndValue(200)
            self.Annimation.setDuration(self.AnniDuration)
            self.Annimation.setEasingCurve(QEasingCurve.BezierSpline)
            self.Annimation.start()
        else:
            self.UI.ToggleRightBtn.setObjectName("ToggleRightBtn")
            self.UI.ToggleRightBtn.setChecked(False)
            self.Annimation = QPropertyAnimation(self.UI.RightModal, b"minimumWidth")
            self.Annimation.setStartValue(200)
            self.Annimation.setEndValue(0)
            self.Annimation.setDuration(self.AnniDuration)
            self.Annimation.setEasingCurve(QEasingCurve.BezierSpline)
            self.Annimation.start()
        self.perform
#
###########################################################################################################################
########    UPDATE STYLE EVENTS                                 ~   NEED REFACTORING    ~   IMPORTANT
###########################################################################################################################
    def perform(self):
        if self.windowState() == Qt.WindowMaximized:
            self.UI.TopBar.setObjectName("TopBarOpen")
            self.UI.LeftModal.setObjectName("LeftModalMax")
        else:
            self.UI.LeftModal.setObjectName("LeftModal")
            if self.UI.LeftModal.width() != 0:
                self.UI.TopBar.setObjectName("TopBar") 
            else:
                self.UI.TopBar.setObjectName("TopBarOpen")

        self.setStyleSheet(self.styleSheet())
        self.update()
#
###########################################################################################################################
########    LOGIN METHOD
###########################################################################################################################
    def LoginBtnClick(self):
        if auth.login(username=self.UI.UsernameLb.text(), password=self.UI.PasswordLb.text()):
            self.logado = True
            self.CheckLogin()
        else:
         
            if self.logado:
                self.logado = False
            self.LoginFailed(2000)
#######     DISPLAY ERROR ON NOT HAVE MATCHED USER O PASS
    def LoginFailed(self, delayMs):
        self.UI.ErroMsg.setText("Ocorreu um Erro ao logar!.")
        self.__old = self.UI.ErroMsg.windowOpacity()
        self.UI.ErroMsg.setWindowOpacity(1)
        self.Annimation = QPropertyAnimation(self.UI.ErroMsg, b"windowOpacity")
        self.Annimation.setDuration(delayMs)
        self.Annimation.setStartValue(self.__old)
        self.Annimation.setEndValue(0)
        self.Annimation.finished.connect(self.__EndFailed)
        self.Annimation.setEasingCurve(QEasingCurve.OutInBounce)
        self.Annimation.start()
    def __EndFailed(self):
        self.UI.ErroMsg.setText("")
        self.UI.ErroMsg.setWindowOpacity(self.__old)
#
###########################################################################################################################
########    MAIN LOOP APPLICATION                               ~   V1.1
###########################################################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    loginApp = loginApp()

    try:
        sys.exit(app.exec())
    except:
        pass

