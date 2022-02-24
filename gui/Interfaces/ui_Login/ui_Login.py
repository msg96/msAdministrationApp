# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_ui_1BptfQm.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 500)
        MainWindow.setMinimumSize(QSize(450, 500))
        MainWindow.setMaximumSize(QSize(450, 500))
        font = QFont()
        font.setFamilies([u"Microsoft Sans Serif"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"#MainWindow, #widget { background-color:  transparent; }\n"
"* { background-color: #171717; color: #2D2D2D; }\n"
"#Body { border-radius: 15px; border: 3px solid #11696969; }\n"
"#Body:hover {  border: 1px solid #44696969; }\n"
"#MoveGrip { background-color: #11696969; border-radius: 5px; }\n"
"#MoveGrip:hover { background-color: #44696969; }\n"
"#TitleLb:hover {color: #303030;}\n"
"\n"
"#LogoImg {border-radius: 75px; border: 1px solid #4D4D4D; background-color: #11696969;}\n"
"\n"
"#ErroMsg {Color: #916c0e17; }\n"
"#UsernameLb, #PasswordLb, #LoginBtn { border-radius: 5px; border: 1px solid #11696969; }\n"
"#UsernameLb:focus, #PasswordLb:focus, #LoginBtn:focus { color: #4D4D4D; border-bottom: 1px solid #77696969; }\n"
"#StayConnectBox:checked { color: #4D4D4D;  }\n"
"#StayConnectBox:focus { border-bottom: 1px solid #77696969; }\n"
"#LoginBtn:hover {background-color: #11696969; color: #4D4D4D;}\n"
"\n"
"")
        self.widget = QWidget(MainWindow)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Body = QFrame(self.widget)
        self.Body.setObjectName(u"Body")
        self.Body.setFrameShape(QFrame.StyledPanel)
        self.Body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.Body)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_2 = QFrame(self.Body)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 50))
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.MoveGrip = QFrame(self.frame_3)
        self.MoveGrip.setObjectName(u"MoveGrip")
        self.MoveGrip.setMinimumSize(QSize(0, 10))
        self.MoveGrip.setMaximumSize(QSize(16777215, 10))
        self.MoveGrip.setFrameShape(QFrame.NoFrame)
        self.MoveGrip.setFrameShadow(QFrame.Raised)
        self.MoveGrip.setLineWidth(0)

        self.verticalLayout_3.addWidget(self.MoveGrip)

        self.TitleLb = QLabel(self.frame_3)
        self.TitleLb.setObjectName(u"TitleLb")
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        font1.setPointSize(20)
        self.TitleLb.setFont(font1)
        self.TitleLb.setFrameShape(QFrame.NoFrame)
        self.TitleLb.setLineWidth(0)
        self.TitleLb.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.TitleLb)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 200))
        self.frame_4.setMaximumSize(QSize(16777215, 200))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.LogoImg = QFrame(self.frame_4)
        self.LogoImg.setObjectName(u"LogoImg")
        self.LogoImg.setMinimumSize(QSize(154, 154))
        self.LogoImg.setMaximumSize(QSize(154, 154))
        self.LogoImg.setContextMenuPolicy(Qt.NoContextMenu)
        self.LogoImg.setFrameShape(QFrame.NoFrame)
        self.LogoImg.setFrameShadow(QFrame.Raised)
        self.LogoImg.setLineWidth(0)

        self.horizontalLayout.addWidget(self.LogoImg)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(30, 0, 30, 0)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_7.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.FormPanel = QFrame(self.frame_7)
        self.FormPanel.setObjectName(u"FormPanel")
        self.FormPanel.setFrameShape(QFrame.NoFrame)
        self.FormPanel.setFrameShadow(QFrame.Raised)
        self.FormPanel.setLineWidth(0)
        self.verticalLayout_5 = QVBoxLayout(self.FormPanel)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 15)
        self.ErroMsg = QLabel(self.FormPanel)
        self.ErroMsg.setObjectName(u"ErroMsg")
        self.ErroMsg.setEnabled(True)
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.ErroMsg.setFont(font2)
        self.ErroMsg.setContextMenuPolicy(Qt.NoContextMenu)
        self.ErroMsg.setFrameShape(QFrame.NoFrame)
        self.ErroMsg.setLineWidth(0)
        self.ErroMsg.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.ErroMsg)

        self.UsernameLb = QLineEdit(self.FormPanel)
        self.UsernameLb.setObjectName(u"UsernameLb")
        self.UsernameLb.setEnabled(True)
        self.UsernameLb.setMinimumSize(QSize(0, 27))
        self.UsernameLb.setMaximumSize(QSize(16777215, 27))
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(12)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.UsernameLb.setFont(font3)
        self.UsernameLb.setMouseTracking(True)
        self.UsernameLb.setTabletTracking(True)
        self.UsernameLb.setFocusPolicy(Qt.StrongFocus)
        self.UsernameLb.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.UsernameLb.setAcceptDrops(True)
        self.UsernameLb.setInputMethodHints(Qt.ImhSensitiveData)
        self.UsernameLb.setMaxLength(200)
        self.UsernameLb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.UsernameLb.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.UsernameLb.setClearButtonEnabled(False)

        self.verticalLayout_5.addWidget(self.UsernameLb)

        self.PasswordLb = QLineEdit(self.FormPanel)
        self.PasswordLb.setObjectName(u"PasswordLb")
        self.PasswordLb.setEnabled(True)
        self.PasswordLb.setMinimumSize(QSize(0, 27))
        self.PasswordLb.setMaximumSize(QSize(16777215, 27))
        self.PasswordLb.setFont(font3)
        self.PasswordLb.setMouseTracking(True)
        self.PasswordLb.setTabletTracking(True)
        self.PasswordLb.setFocusPolicy(Qt.StrongFocus)
        self.PasswordLb.setContextMenuPolicy(Qt.NoContextMenu)
        self.PasswordLb.setAcceptDrops(False)
        self.PasswordLb.setMaxLength(200)
        self.PasswordLb.setEchoMode(QLineEdit.Password)
        self.PasswordLb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.PasswordLb.setReadOnly(False)
        self.PasswordLb.setClearButtonEnabled(False)

        self.verticalLayout_5.addWidget(self.PasswordLb)

        self.StayConnectBox = QCheckBox(self.FormPanel)
        self.StayConnectBox.setObjectName(u"StayConnectBox")
        self.StayConnectBox.setMinimumSize(QSize(140, 0))
        self.StayConnectBox.setMaximumSize(QSize(140, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Microsoft Sans Serif"])
        font4.setPointSize(10)
        font4.setStyleStrategy(QFont.PreferAntialias)
        self.StayConnectBox.setFont(font4)
        self.StayConnectBox.setTabletTracking(True)
        self.StayConnectBox.setFocusPolicy(Qt.TabFocus)
        self.StayConnectBox.setContextMenuPolicy(Qt.NoContextMenu)
#if QT_CONFIG(shortcut)
        self.StayConnectBox.setShortcut(u"")
#endif // QT_CONFIG(shortcut)
        self.StayConnectBox.setCheckable(True)
        self.StayConnectBox.setChecked(True)
        self.StayConnectBox.setTristate(False)

        self.verticalLayout_5.addWidget(self.StayConnectBox)

        self.LoginBtn = QPushButton(self.FormPanel)
        self.LoginBtn.setObjectName(u"LoginBtn")
        self.LoginBtn.setMinimumSize(QSize(150, 27))
        self.LoginBtn.setMaximumSize(QSize(150, 27))
        self.LoginBtn.setMouseTracking(True)
        self.LoginBtn.setTabletTracking(True)
        self.LoginBtn.setFocusPolicy(Qt.TabFocus)
        self.LoginBtn.setContextMenuPolicy(Qt.NoContextMenu)

        self.verticalLayout_5.addWidget(self.LoginBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_4.addWidget(self.FormPanel)


        self.horizontalLayout_2.addWidget(self.frame_7)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.verticalLayout_6.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.Body)

        MainWindow.setCentralWidget(self.widget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.TitleLb.setText(QCoreApplication.translate("MainWindow", u"MS Adiministration", None))
        self.ErroMsg.setText(QCoreApplication.translate("MainWindow", u"Erro ao tentar logar!.", None))
        self.UsernameLb.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio ou Email", None))
        self.PasswordLb.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.StayConnectBox.setText(QCoreApplication.translate("MainWindow", u"Manter Conectado ?", None))
        self.LoginBtn.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
    # retranslateUi

