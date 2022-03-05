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
###########################################################################################################################
########    MODULES
###########################################################################################################################
from assets.styles import style
from modulos.msVariables import Svgs
###########################################################################################################################
########    WIDGETS
###########################################################################################################################
from gui.widgets.msBoxLayout.msVBoxLayout import msVBoxLayout
from gui.widgets.msButton import msButton
from gui.widgets.msLabel import msLabel
from gui.widgets.msPanel import msPanel
from gui.widgets.msSVGRender import msSVGRender
from gui.widgets.msTxtImput import MsTxtImput
###########################################################################################################################
###########################################################################################################################
#####   BODY WIDGET
class body(msPanel):
    def __init__(self, parent: QWidget):
        super(body, self).__init__(parent)
        self.applyStyles()
    def applyStyles(self):
        self.backgroundColor(style["primarybg"])
#####   LOGO WIDGET
class logo(msSVGRender):
    def __init__(self, parent: str, File=Svgs['manage_accounts_white_48dp'], largura=150, altura=150, cor=style['logintxt']):
        super(logo, self).__init__(parent, File, largura, altura, cor)
        self.applyStyles()
    def applyStyles(self):
        self.cor(style['logintxt'])
#####   DISPLAYLB WIDGET
class displayLb(msLabel):
    def __init__(self, parent: QWidget):
        super(displayLb, self).__init__(parent)
        self.MyFont = QFont()
        self.MyFont.setFamilies([u"Times New Roman"])
        self.MyFont.setPointSize(12)
        self.MyFont.setBold(False)
        self.MyFont.setItalic(False)
        self.MyFont.setKerning(True)
        self.MyFont.setStyleStrategy(QFont.PreferAntialias)
        self.setAlignment(Qt.AlignCenter)
        self.setFont(self.MyFont)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.applyStyles()
    def applyStyles(self):
        self.color(style["logintxt"])
#####   LOGINTXT WIDGET
class loginTxt(MsTxtImput):
    def __init__(self, parent: QObject) -> None:
        super(loginTxt, self).__init__(parent)
        self.setMinimumSize(QSize(350, 27))
        self.setMaximumSize(QSize(350, 27))
        self.setFocus(Qt.FocusReason.NoFocusReason)
        self.setMaxLength(200)
        self.setInputMethodHints(Qt.ImhSensitiveData)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.setPlaceholderText("Usuername or Email")
        self.applyStyles()
    def applyStyles(self):
        self.backgroundColor("Transparent")
        self.color(style["logintxt"])
        self.flatStyle(True)
        self.hoverFlatStyle(True)
        self.border(1, "solid", style["hoverbtns"])
        self.borderRadius(5, 5, 5, 5)
        self.hoverBackgroundColor("transparent")
        self.hoverColor(style["logintxthover"])
        self.focusColor(style["displaycolor"])
        self.focusBorderBottom(1, "solid", style["logintxthover"])
#####   PASSWORDTXT WIDGET
class passwordTxt(MsTxtImput):
    def __init__(self, parent :QObject) -> None:
        super(passwordTxt, self).__init__(parent)
        self.setMinimumSize(QSize(350, 27))
        self.setMaximumSize(QSize(350, 27))
        self.setPlaceholderText("Password")
        self.setInputMethodHints(Qt.ImhSensitiveData | Qt.ImhHiddenText | Qt.ImhNoAutoUppercase | Qt.ImhNoPredictiveText)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.setMaxLength(32)
        self.setEchoMode(self.EchoMode.Password)
        self.applyStyles()
    def applyStyles(self):
        self.backgroundColor("Transparent")
        self.backgroundColor("Transparent")
        self.color(style["logintxt"])
        self.flatStyle(True)
        self.hoverFlatStyle(True)
        self.border(1, "solid", style["hoverbtns"])
        self.borderRadius(5, 5, 5, 5)
        self.hoverBackgroundColor("transparent")
        self.hoverColor(style["logintxthover"])
        self.focusColor(style["displaycolor"])
        self.focusBorderBottom(1, "solid", style["logintxthover"])
#####   LOGINBTN WIDGET
class loginBtn(msButton):
    def __init__(self, parent: QWidget):
        super(loginBtn, self).__init__(parent)
        self.setText("Logar")
        self.setMaximumSize(QSize(150, 27))
        self.setMinimumSize(QSize(150, 27))
        self.setAutoDefault(True)
        self.setDefault(True)
        self.applyStyles()
    def applyStyles(self):
        self.color(style["logintxt"])
        self.flatStyle(True)
        self.hoverFlatStyle(True)
        self.border(1, "solid", style["logintxthover"])
        self.borderRadius(5, 5, 5, 5)
        self.hoverBackgroundColor("transparent")
        self.hoverColor(style["logintxthover"])
        self.focusColor(style["displaycolor"])
        self.focusBorderBottom(1, "solid", style["displaycolor"])
         ####
#########   SUBUI_lOGIN
class subui_Login(object):
    def start (self, parent :QObject):
        self.parent = parent
########    DEFINE OUR PRINCIPAL FRAME ON LOGIN UI
        self.body = body(self.parent)
########    SET SOME BOX FOR OUR BODY
        self.bodyBox = msVBoxLayout(self.body)
        self.bodyBox.setAlignment( Qt.AlignHCenter | Qt.AlignTop)
        self.bodyBox.setSpacing(15)
########    SET SOME CHILDS TO BODY
        self.logo = logo(self.body)
        self.displayLb = displayLb(self.body)
        self.loginTxt = loginTxt(self.body)
        self.passwordTxt = passwordTxt(self.body)
        self.loginBtn = loginBtn(self.body)
        ####    ADD CHILDS TO BODY
        self.bodyBox.addWidget(self.logo, 0, Qt.AlignVCenter | Qt.AlignHCenter)
        self.bodyBox.addWidget(self.displayLb, 0, Qt.AlignVCenter | Qt.AlignHCenter)
        self.bodyBox.addWidget(self.loginTxt, 0, Qt.AlignVCenter | Qt.AlignHCenter)
        self.bodyBox.addWidget(self.passwordTxt, 0, Qt.AlignVCenter | Qt.AlignHCenter)
        self.bodyBox.addWidget(self.loginBtn, 0, Qt.AlignVCenter | Qt.AlignHCenter)
########    APPLY STYLES FOR ALL COMPONENTS
    def applyStyles(self):
        for i in self.__dict__:
            try:
                i.applyStyles()
            except: 
                pass
