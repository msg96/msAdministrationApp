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
#############################
from assets.styles import style
from gui.widgets.msButton.msButton import msButton
from gui.widgets.msLabel.msLabel import msLabel
from gui.widgets.msPanel import msPanel
from gui.widgets.msTxtImput import MsTxtImput
from modulos import customFunctions

class subui_Login(object):
    def start (self, parent :QObject):
        self.parent = parent
        self.schemeColor = style
        self.body = msPanel(self.parent)
        self.body.backgroundColor(self.schemeColor["contentpagesbg"])
        self.body.setMinimumSize(400, 400)
        self.body.setMaximumSize(400, 400)
        self.body.setGeometry(0, 0, 400, 400)
        self.bodyBox = QVBoxLayout(self.body)
        self.bodyBox.setAlignment( Qt.AlignHCenter | Qt.AlignTop)
        self.bodyBox.setContentsMargins(0, 0, 0, 0)
        self.bodyBox.setSpacing(15)
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setKerning(True)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.logo = msButton(self.body)
        self.icon = QIcon(customFunctions.AppGetFile(customFunctions.AppGetUniversalPath("assets/svg"), "manage_accounts_white_48dp.svg"))
        self.bodyBox.addWidget(self.logo, 0, Qt.AlignVCenter | Qt.AlignHCenter)
        self.logo.setIcon(self.icon)
        self.logo.setIconSize(QSize(self.logo.size().width() / 3, self.logo.size().height() / 3))
        self.logo.borderRadius(50, 50, 50, 50)
        self.logo.setMinimumSize(QSize(150, 150))
        self.logo.setMaximumSize(QSize(150, 150))
        self.logo.setFocusPolicy(Qt.FocusPolicy.NoFocus)


        self.displayLb = msLabel(self.body)
        self.bodyBox.addWidget(self.displayLb, 0, Qt.AlignVCenter | Qt.AlignHCenter)
        self.displayLb.setAlignment(Qt.AlignCenter)
        self.displayLb.setFont(font3)
        self.displayLb.color("#916c0e17")
        self.displayLb.setFocusPolicy(Qt.FocusPolicy.NoFocus)


        self.loginTxt = MsTxtImput(self.body)
        self.bodyBox.addWidget(self.loginTxt, 0, Qt.AlignVCenter | Qt.AlignHCenter)

        self.loginTxt.setMinimumSize(QSize(350, 27))
        self.loginTxt.setMaximumSize(QSize(350, 27))
        self.loginTxt.setFocus(Qt.FocusReason.NoFocusReason)
        self.loginTxt.setMaxLength(200)
        self.loginTxt.setInputMethodHints(Qt.ImhSensitiveData)
        self.loginTxt.setContextMenuPolicy(Qt.NoContextMenu)
        self.loginTxt.setPlaceholderText("Usuername or Email")
        self.loginTxt.backgroundColor("Transparent")
        self.loginTxt.color("#7D7D7D")
        self.loginTxt.flatStyle(True)
        self.loginTxt.hoverFlatStyle(True)
        self.loginTxt.border(1, "solid", "#33696969")
        self.loginTxt.borderRadius(5, 5, 5, 5)
        self.loginTxt.hoverBackgroundColor("#11696969")
        self.loginTxt.hoverColor("#4D4D4D")
        self.loginTxt.focusColor("#ADADAD")
        self.loginTxt.focusBorderBottom(1, "solid", "#99696969")
        



        self.passwordTxt = MsTxtImput(self.body)
        self.bodyBox.addWidget(self.passwordTxt, 0, Qt.AlignVCenter | Qt.AlignHCenter)
        self.passwordTxt.setMinimumSize(QSize(350, 27))
        self.passwordTxt.setMaximumSize(QSize(350, 27))
        self.passwordTxt.setPlaceholderText("Password")
        self.passwordTxt.setInputMethodHints(Qt.ImhSensitiveData | Qt.ImhHiddenText | Qt.ImhNoAutoUppercase | Qt.ImhNoPredictiveText)
        self.passwordTxt.setContextMenuPolicy(Qt.NoContextMenu)
        self.passwordTxt.setMaxLength(32)
        self.passwordTxt.setEchoMode(self.passwordTxt.EchoMode.Password)
        self.passwordTxt.backgroundColor("Transparent")
        self.passwordTxt.color("#7D7D7D")
        self.passwordTxt.flatStyle(True)
        self.passwordTxt.hoverFlatStyle(True)
        self.passwordTxt.border(1, "solid", "#33696969")
        self.passwordTxt.borderRadius(5, 5, 5, 5)
        self.passwordTxt.hoverBackgroundColor("#11696969")
        self.passwordTxt.hoverColor("#4D4D4D")
        self.passwordTxt.focusColor("#ADADAD")
        self.passwordTxt.focusBorderBottom(1, "solid", "#99696969")


        
        self.loginBtn = msButton(self.body)
        self.loginBtn.setText("Logar")
        self.bodyBox.addWidget(self.loginBtn, 0, Qt.AlignVCenter | Qt.AlignHCenter)
        self.loginBtn.setMaximumSize(QSize(150, 27))
        self.loginBtn.setMinimumSize(QSize(150, 27))
        self.loginBtn.color("#7D7D7D")
        self.loginBtn.flatStyle(True)
        self.loginBtn.border(1, "solid", "#33696969")
        self.loginBtn.borderRadius(5, 5, 5, 5)
        self.loginBtn.hoverBackgroundColor("#11696969")
        self.loginBtn.hoverColor("#4D4D4D")
        self.loginBtn.focusColor("#ADADAD")
        self.loginBtn.focusBorderBottom(1, "solid", "#99696969")
