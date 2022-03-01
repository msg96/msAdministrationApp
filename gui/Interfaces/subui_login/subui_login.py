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
        self.bodyBox.setAlignment( Qt.AlignVCenter | Qt.AlignTop)
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
        self.displayLb = QLabel(self.body)
        self.bodyBox.addWidget(self.displayLb, 0, Qt.AlignVCenter | Qt.AlignHCenter)
        self.displayLb.setText("Algo deu errado ao logar!")
        self.displayLb.setAlignment(Qt.AlignCenter)
        self.displayLb.setFont(font3)
        self.displayLb.setStyleSheet("color: whitesmoke;")
        self.loginTxt = QLineEdit(self.body)
        self.bodyBox.addWidget(self.loginTxt, 0, Qt.AlignVCenter | Qt.AlignHCenter)
        self.loginTxt.setMinimumSize(QSize(350, 27))
        self.loginTxt.setMaximumSize(QSize(350, 27))
        self.passwordTxt = QLineEdit(self.body)
        self.bodyBox.addWidget(self.passwordTxt, 0, Qt.AlignVCenter | Qt.AlignHCenter)
        self.passwordTxt.setMinimumSize(QSize(350, 27))
        self.passwordTxt.setMaximumSize(QSize(350, 27))
        self.loginBtn = msButton(self.body)
        self.loginBtn.setText("Logar")
        self.loginBtn.color("#7D7D7D")
        self.loginBtn.flatStyle(True)
        self.loginBtn.border(1, "DASHED", "#33696969")
        self.loginBtn.borderRadius(5, 5, 5, 5)
        self.loginBtn.hoverBackgroundColor("#11696969")
        self.loginBtn.hoverColor("#4D4D4D")
        self.bodyBox.addWidget(self.loginBtn, 0, Qt.AlignVCenter | Qt.AlignHCenter)
        self.loginBtn.setMaximumSize(QSize(150, 27))
        self.loginBtn.setMinimumSize(QSize(150, 27))



