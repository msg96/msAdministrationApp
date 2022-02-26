###########################################################################################################################
########    IMPORTS
###########################################################################################################################
import sys
from required import *
###########################################################################################################################
########    CUSTOM WIDGETS AND QTDESIGNEDS IMPORTS
###########################################################################################################################
#from gui.widgets import  msLoginForm
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
        self.__oldOpacity = self.windowOpacity()
        ######################
        #
        self.perform()
        self.UI.ErroMsg.setWindowOpacity(1)
        self.p = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        x = (self.p.x() - (self.width() / 2))
        y = (self.p.y() - (self.height() / 2))
        self.move(x,y)
        self._piri = self.geometry()
        self.bar = self.UI.TopBarCenter
        self.AnniDuration = 300
        self.onAnni = False
        self.cookie = {'0':'0'}
        ###################################################################################################################
        ###########     DEFINA COMO TRUE SE QUISER COMEÇAR LOGADO PARA TESTAR A INTERFACE           #######################
        ###################################################################################################################
        self.logado = True
        ###################################################################################################################
        self.setWindowOpacity(1)
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

        self.Annimation =  QPropertyAnimation(self, b"geometry")
        self.Annimation.setStartValue(QRect(0-(self.width()/2),0-(self.height()/2),0,0))
        self.Annimation.setEndValue(QRect(self.geometry().x(),self.geometry().y(),self.geometry().width(),self.geometry().height()))
        self.Annimation.setDuration(500)
        self.Annimation.setEasingCurve(QEasingCurve.OutCirc)
        self.onAnni = True
        self.Annimation.finished.connect(self.__endAnni)
        self.Annimation.start()

    def __endAnni(self):
         self.onAnni = False
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
        self.setWindowState(Qt.WindowMinimized)
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
        self.UI.MaximizeBtn.setChecked(not self.UI.MaximizeBtn.isChecked())
        self.Maxmizeme()
#
###########################################################################################################################
########    MAXIMIZE EVENT                                      ~   NEED BETTER EFFECTS
###########################################################################################################################
    def Maxmizeme(self):
        if not self.logado:
            return
        if not self.UI.MaximizeBtn.isChecked():
            self.setWindowState(Qt.WindowNoState)
        else:
            self.setWindowState(Qt.WindowMaximized)
#
###########################################################################################################################
########    CLOSE EVENT                                         ~   NEED BETTER EFFECTS
###########################################################################################################################
    def Closeme(self):
        self.Annimation = QPropertyAnimation(self, b"geometry")
        self.Annimation.setEndValue(QRect(0-(self.width()/2),0-(self.height()/2),0,0))
        self.Annimation.setStartValue(QRect(self.geometry().x(),self.geometry().y(),self.geometry().width(),self.geometry().height()))
        self.Annimation.setDuration(self.AnniDuration)
        self.Annimation.setEasingCurve(QEasingCurve.BezierSpline)
        self.onAnni = True
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
        if self.onAnni:
            return
        if self.UI.LeftModal.minimumWidth()  == 0:
            self.UI.ToggleLeftBtn.setObjectName("ToggleLeftBtnOpen")
            self.UI.ToggleLeftBtn.setChecked(True)
            self.UI.TopBar.setObjectName("TopBarOpen")
            self.Annimation = QPropertyAnimation(self.UI.LeftModal, b"minimumWidth")
            self.Annimation.setStartValue(0)
            self.Annimation.setEndValue(200)
            self.Annimation.setDuration(self.AnniDuration)
            self.Annimation.setEasingCurve(QEasingCurve.BezierSpline)
            self.Annimation.finished.connect(self._afterToggleClick)
            self.onAnni = True
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
            self.onAnni = True
            self.Annimation.finished.connect(self._afterToggleClick)
            self.Annimation.start()
#
###########################################################################################################################
########    CLICK TOGGLERIGHTBNT                                ~   NEED BETTER EFFECTS
###########################################################################################################################
    def RightMenuTogglerClick(self):    
        if self.onAnni:
            return
        if self.UI.RightModal.minimumWidth()  == 0:
            self.UI.ToggleRightBtn.setObjectName("ToggleRightBtnOpen")
            self.UI.ToggleRightBtn.setChecked(True)
            self.Annimation = QPropertyAnimation(self.UI.RightModal, b"minimumWidth")
            self.Annimation.setStartValue(0)
            self.Annimation.setEndValue(200)
            self.Annimation.setDuration(self.AnniDuration)
            self.Annimation.setEasingCurve(QEasingCurve.BezierSpline)
            self.onAnni = True
            self.Annimation.finished.connect(self._afterToggleClick)
            self.Annimation.start()
        else:
            self.UI.ToggleRightBtn.setObjectName("ToggleRightBtn")
            self.UI.ToggleRightBtn.setChecked(False)
            self.Annimation = QPropertyAnimation(self.UI.RightModal, b"minimumWidth")
            self.Annimation.setStartValue(200)
            self.Annimation.setEndValue(0)
            self.Annimation.setDuration(self.AnniDuration)
            self.Annimation.setEasingCurve(QEasingCurve.BezierSpline)
            self.onAnni = True
            self.Annimation.finished.connect(self._afterToggleClick)
            self.Annimation.start()
#
    def _afterToggleClick(self):
        self.perform()
        self.onAnni = False
#
###########################################################################################################################
########    UPDATE STYLE EVENTS                                 ~   NEED REFACTORING    ~   IMPORTANT
###########################################################################################################################
    def perform(self):
        if self.windowState() == Qt.WindowMaximized:
            self.UI.TopBar.setObjectName("TopBarOpen")
            self.UI.LeftModal.setObjectName("LeftModalMax")
        else:
            if self.UI.LeftModal.width() != 0:
                self.UI.TopBar.setObjectName("TopBar")
            else:
                self.UI.TopBar.setObjectName("TopBarOpen")
            
            self.UI.LeftModal.setObjectName("LeftModal")
#
###########################################################################################################################
########    LOGIN METHOD
###########################################################################################################################
    def LoginBtnClick(self):
        con = auth.login(login=self.UI.UsernameLb.text(), password=self.UI.PasswordLb.text())
        if con and con[0] < 4:
            self.cookie.update({'privilege': con[0]})
            self.cookie.update({'usuario': con[1]})
            self.__saveOP = self.windowOpacity()
            self.Annimation = QPropertyAnimation(self, b"windowOpacity")
            self.Annimation.setDuration(self.AnniDuration)
            self.Annimation.setStartValue(self.__saveOP)
            self.Annimation.setEndValue(0)
            self.Annimation.finished.connect(self.__EndSucess)
            self.Annimation.setEasingCurve(QEasingCurve.OutInBounce)
            self.Annimation.start()
        else:
            if self.logado:
                self.logado = False
            if not con:
                self.LoginFailed(2000, "Ocorreu um Erro ao logar!.")
            elif con[0] == 4:
                self.LoginFailed(2000, "Conta Bloqueada, entre em contato com o administrador!.")
            else:
                self.LoginFailed(2000, "Ocorreu um Erro ao logar!.")
#   
    def __EndSucess(self):
        self.logado = True
        self.CheckLogin()
        self.Annimation = QPropertyAnimation(self, b"windowOpacity")
        self.Annimation.setDuration(self.AnniDuration)
        self.Annimation.setStartValue(0)
        self.Annimation.setEndValue(self.__saveOP)
        self.Annimation.setEasingCurve(QEasingCurve.OutInBounce)
        self.Annimation.start()
#
#######     DISPLAY ERROR ON NOT HAVE MATCHED USER O PASS
    def LoginFailed(self, delayMs, displaytext):
        self.UI.ErroMsg.setText(displaytext)
        self.__old = self.UI.ErroMsg.windowOpacity()
        self.UI.ErroMsg.setWindowOpacity(1)
        self.Annimation = QPropertyAnimation(self.UI.ErroMsg, b"windowOpacity")
        self.Annimation.setDuration(delayMs)
        self.Annimation.setStartValue(self.__old)
        self.Annimation.setEndValue(0)
        self.Annimation.finished.connect(self.__EndFailed)
        self.Annimation.setEasingCurve(QEasingCurve.OutInBounce)
        self.Annimation.start()
#    
    def __EndFailed(self):
        self.UI.ErroMsg.setText("")
        self.UI.ErroMsg.setWindowOpacity(self.__old)
#
    def paintEvent(self, event: QPaintEvent) -> None:
        self.setStyleSheet(GetStyle("uniColors"))
        self.update()
        msLoginForm.paintEvent(self, event)
#########################################################################
########    MAIN LOOP APPLICATION                               ~   V1.1
###########################################################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    loginApp = loginApp()
    try:
        sys.exit(app.exec())
    except:
        pass
