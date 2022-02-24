# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_1mTXoNj.ui'
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
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)
import assets.svg.icons_rc as icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(940, 607)
        MainWindow.setMinimumSize(QSize(940, 600))
        MainWindow.setMaximumSize(QSize(50000, 50000))
        MainWindow.setStyleSheet(u"* { background-color: transparent; color: #B2B2B2; }\n"
"#MainWindow, #centralwidget { background-color: transparent; }\n"
"#TopBar { background-color: #050505; border-top-left-radius:10px;}\n"
"#TopBarOpen { background-color: #050505; border-top-left-radius:0px; }\n"
"#LeftModal { background-color: #111111; border-top-left-radius: 10px; border-bottom-left-radius: 15px; }\n"
"#LeftModalMax { background-color: #111111; border-top-left-radius: 0px; border-bottom-left-radius: 0px; }\n"
"#RightModal { background-color: #111111; border-top: 1px solid #050505;}\n"
"#ContentPanel {background-color: #101010; border-top: 1px solid #050505; border-left: 1px solid #050505; }\n"
"#ContentPages {border-right: 1px solid #050505; border-top: 1px solid #050505;}\n"
"#ContentTitles { background-color: #090909 ; }\n"
"/* Toggle buttons */\n"
"#ToggleLeftBtn { background-color: #050505; border: none;\n"
"border-top-left-radius: 10px; border-bottom-left-radius: 0px;\n"
"border-top-right-radius: 0px; border-bottom-right-radius: 0p"
                        "x;}\n"
"#ToggleLeftBtn:hover { background-color: #91111111; border: none; }\n"
"#ToggleLeftBtnOpen { background-color: #111111; border: none; \n"
"border-top-left-radius: 0px; border-bottom-left-radius: 0px;\n"
"border-top-right-radius: 10px; border-bottom-right-radius: 0px; }\n"
"#ToggleLeftBtnOpen:hover { background-color: #91111111; border: none; }\n"
"/**/\n"
"#ToggleRightBtn { background-color: #090909; border: none;\n"
"border-top-left-radius: 0px; border-bottom-left-radius: 0px;\n"
"border-top-right-radius: 0px; border-bottom-right-radius: 0px;}\n"
"#ToggleRightBtn:hover  { background-color: #91111111; border: none; }\n"
"#ToggleRightBtnOpen { background-color: #111111; border:none;\n"
"border-top-left-radius: 10px; border-bottom-left-radius: 0px;\n"
" border-top-right-radius: 0px; border-bottom-right-radius: 0px; }\n"
"#ToggleRightBtnOpen:hover { background-color: #91111111; border: none; }\n"
"/*	*/\n"
"/*  windows state buttons */\n"
"#MinimizeBtn, #MaximizeBtn, #CloseBtn { background-color: transpar"
                        "ent; border: none; }\n"
"#MinimizeBtn:hover, #MaximizeBtn:hover, #CloseBtn:hover {	border-bottom: 1px solid #111111;}\n"
"#MinimizeBtn:hover, #MaximizeBtn:hover { background-color: #101010; }\n"
"#CloseBtn:hover { background-color: #916c0e17; }\n"
"/*	*/\n"
"#Body { border-radius: 15px; border: 3px solid #11696969; }\n"
"#Body:hover {  border: 1px solid #44696969; }\n"
"#MoveGrip { background-color: #11696969; border-radius: 5px; }\n"
"#MoveGrip:hover { background-color: #44696969; }\n"
"#TitleLb { color: #2D2D2D}\n"
"#TitleLb:hover {color: #303030;}\n"
"\n"
"#ErroMsg {Color: #916c0e17; }\n"
"#UsernameLb, #PasswordLb, #LoginBtn { border-radius: 5px; border: 1px solid #33696969; color: #7D7D7D;}\n"
"#UsernameLb:focus, #PasswordLb:focus, #LoginBtn:focus { color: #ADADAD; border-bottom: 1px solid #99696969; }\n"
"#StayConnectBox { color: #5D5D5D }\n"
"#StayConnectBox:checked { color: #7D7D7D;  }\n"
"#StayConnectBox:focus { border-bottom: 1px solid #99696969; }\n"
"#LoginBtn:hover {background-color: #11696969; col"
                        "or: #4D4D4D;}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftModal = QFrame(self.centralwidget)
        self.LeftModal.setObjectName(u"LeftModal")
        self.LeftModal.setMaximumSize(QSize(0, 16777215))
        self.LeftModal.setFrameShape(QFrame.NoFrame)
        self.LeftModal.setFrameShadow(QFrame.Plain)
        self.LeftModal.setLineWidth(0)

        self.horizontalLayout.addWidget(self.LeftModal)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Plain)
        self.Content.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.Content)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TopBar = QFrame(self.Content)
        self.TopBar.setObjectName(u"TopBar")
        self.TopBar.setMinimumSize(QSize(0, 33))
        self.TopBar.setMaximumSize(QSize(16777215, 33))
        self.TopBar.setFrameShape(QFrame.NoFrame)
        self.TopBar.setFrameShadow(QFrame.Plain)
        self.TopBar.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.TopBar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ToggleLeftBtn = QPushButton(self.TopBar)
        self.ToggleLeftBtn.setObjectName(u"ToggleLeftBtn")
        self.ToggleLeftBtn.setMinimumSize(QSize(33, 33))
        self.ToggleLeftBtn.setMaximumSize(QSize(33, 33))
        icon = QIcon()
        icon.addFile(u":/svg/menu_white_48dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/svg/menu_open_white_48dp.svg", QSize(), QIcon.Normal, QIcon.On)
        self.ToggleLeftBtn.setIcon(icon)
        self.ToggleLeftBtn.setCheckable(True)
        self.ToggleLeftBtn.setChecked(False)
        self.ToggleLeftBtn.setFlat(True)

        self.horizontalLayout_3.addWidget(self.ToggleLeftBtn)

        self.TopBarCenter = QFrame(self.TopBar)
        self.TopBarCenter.setObjectName(u"TopBarCenter")
        self.TopBarCenter.setFrameShape(QFrame.StyledPanel)
        self.TopBarCenter.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.TopBarCenter)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.TitleProgram = QLabel(self.TopBarCenter)
        self.TitleProgram.setObjectName(u"TitleProgram")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleProgram.sizePolicy().hasHeightForWidth())
        self.TitleProgram.setSizePolicy(sizePolicy)
        self.TitleProgram.setMinimumSize(QSize(0, 33))
        self.TitleProgram.setMaximumSize(QSize(16777215, 33))
        font = QFont()
        font.setFamilies([u"Microsoft Sans Serif"])
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.TitleProgram.setFont(font)
        self.TitleProgram.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.TitleProgram.setMargin(0)
        self.TitleProgram.setIndent(10)
        self.TitleProgram.setOpenExternalLinks(False)

        self.horizontalLayout_6.addWidget(self.TitleProgram)


        self.horizontalLayout_3.addWidget(self.TopBarCenter)

        self.PanelWindowState = QFrame(self.TopBar)
        self.PanelWindowState.setObjectName(u"PanelWindowState")
        self.PanelWindowState.setMinimumSize(QSize(99, 0))
        self.PanelWindowState.setMaximumSize(QSize(99, 16777215))
        self.PanelWindowState.setFrameShape(QFrame.NoFrame)
        self.PanelWindowState.setFrameShadow(QFrame.Raised)
        self.PanelWindowState.setLineWidth(0)
        self.horizontalLayout_4 = QHBoxLayout(self.PanelWindowState)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.MinimizeBtn = QPushButton(self.PanelWindowState)
        self.MinimizeBtn.setObjectName(u"MinimizeBtn")
        self.MinimizeBtn.setMinimumSize(QSize(33, 33))
        self.MinimizeBtn.setMaximumSize(QSize(33, 33))
        icon1 = QIcon()
        icon1.addFile(u":/svg/minimize_white_48dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.MinimizeBtn.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.MinimizeBtn)

        self.MaximizeBtn = QPushButton(self.PanelWindowState)
        self.MaximizeBtn.setObjectName(u"MaximizeBtn")
        self.MaximizeBtn.setMinimumSize(QSize(33, 33))
        self.MaximizeBtn.setMaximumSize(QSize(33, 33))
        icon2 = QIcon()
        icon2.addFile(u":/svg/fullscreen_white_48dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/svg/fullscreen_exit_white_48dp.svg", QSize(), QIcon.Normal, QIcon.On)
        self.MaximizeBtn.setIcon(icon2)
        self.MaximizeBtn.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.MaximizeBtn)

        self.CloseBtn = QPushButton(self.PanelWindowState)
        self.CloseBtn.setObjectName(u"CloseBtn")
        self.CloseBtn.setMinimumSize(QSize(33, 33))
        self.CloseBtn.setMaximumSize(QSize(33, 33))
        icon3 = QIcon()
        icon3.addFile(u":/svg/close_white_48dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.CloseBtn.setIcon(icon3)

        self.horizontalLayout_4.addWidget(self.CloseBtn)


        self.horizontalLayout_3.addWidget(self.PanelWindowState)


        self.verticalLayout.addWidget(self.TopBar)

        self.frame_2 = QFrame(self.Content)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ContentPanel = QFrame(self.frame_2)
        self.ContentPanel.setObjectName(u"ContentPanel")
        self.ContentPanel.setFrameShape(QFrame.NoFrame)
        self.ContentPanel.setFrameShadow(QFrame.Plain)
        self.ContentPanel.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.ContentPanel)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ContentTitles = QFrame(self.ContentPanel)
        self.ContentTitles.setObjectName(u"ContentTitles")
        self.ContentTitles.setMinimumSize(QSize(0, 33))
        self.ContentTitles.setMaximumSize(QSize(16777215, 33))
        self.ContentTitles.setFrameShape(QFrame.NoFrame)
        self.ContentTitles.setFrameShadow(QFrame.Plain)
        self.ContentTitles.setLineWidth(0)
        self.horizontalLayout_5 = QHBoxLayout(self.ContentTitles)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.ContentTiltesPanel = QFrame(self.ContentTitles)
        self.ContentTiltesPanel.setObjectName(u"ContentTiltesPanel")
        self.ContentTiltesPanel.setFrameShape(QFrame.StyledPanel)
        self.ContentTiltesPanel.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.ContentTiltesPanel)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.TitlePages = QLabel(self.ContentTiltesPanel)
        self.TitlePages.setObjectName(u"TitlePages")
        sizePolicy.setHeightForWidth(self.TitlePages.sizePolicy().hasHeightForWidth())
        self.TitlePages.setSizePolicy(sizePolicy)
        self.TitlePages.setMinimumSize(QSize(0, 33))
        self.TitlePages.setMaximumSize(QSize(16777215, 33))
        self.TitlePages.setFont(font)
        self.TitlePages.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.TitlePages)


        self.horizontalLayout_5.addWidget(self.ContentTiltesPanel)

        self.ToggleRightBtn = QPushButton(self.ContentTitles)
        self.ToggleRightBtn.setObjectName(u"ToggleRightBtn")
        self.ToggleRightBtn.setMinimumSize(QSize(33, 33))
        self.ToggleRightBtn.setMaximumSize(QSize(33, 33))
        icon4 = QIcon()
        icon4.addFile(u":/svg/menu_white_48dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/svg/menu_open_white_right_48dp.svg", QSize(), QIcon.Normal, QIcon.On)
        self.ToggleRightBtn.setIcon(icon4)
        self.ToggleRightBtn.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.ToggleRightBtn)


        self.verticalLayout_2.addWidget(self.ContentTitles)

        self.ContentPages = QFrame(self.ContentPanel)
        self.ContentPages.setObjectName(u"ContentPages")
        self.ContentPages.setFrameShape(QFrame.StyledPanel)
        self.ContentPages.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.ContentPages)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.Paginas = QStackedWidget(self.ContentPages)
        self.Paginas.setObjectName(u"Paginas")
        self.LoginPage = QWidget()
        self.LoginPage.setObjectName(u"LoginPage")
        self.horizontalLayout_9 = QHBoxLayout(self.LoginPage)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame = QFrame(self.LoginPage)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.WinPanel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setLineWidth(10)
        self.horizontalLayout_12 = QHBoxLayout(self.frame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(450, 500))
        self.frame_3.setMaximumSize(QSize(450, 500))
        self.frame_3.setFrameShape(QFrame.WinPanel)
        self.frame_3.setFrameShadow(QFrame.Sunken)
        self.frame_3.setLineWidth(10)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 50))
        self.frame_4.setMaximumSize(QSize(16777215, 50))
        self.frame_4.setFrameShape(QFrame.WinPanel)
        self.frame_4.setFrameShadow(QFrame.Sunken)
        self.frame_4.setLineWidth(10)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.MoveGrip = QFrame(self.frame_4)
        self.MoveGrip.setObjectName(u"MoveGrip")
        self.MoveGrip.setMinimumSize(QSize(0, 10))
        self.MoveGrip.setMaximumSize(QSize(16777215, 10))
        self.MoveGrip.setFrameShape(QFrame.WinPanel)
        self.MoveGrip.setFrameShadow(QFrame.Sunken)
        self.MoveGrip.setLineWidth(10)

        self.verticalLayout_4.addWidget(self.MoveGrip)

        self.TitleLb = QLabel(self.frame_4)
        self.TitleLb.setObjectName(u"TitleLb")
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        font1.setPointSize(20)
        self.TitleLb.setFont(font1)
        self.TitleLb.setFrameShape(QFrame.WinPanel)
        self.TitleLb.setFrameShadow(QFrame.Sunken)
        self.TitleLb.setLineWidth(10)
        self.TitleLb.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.TitleLb)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 200))
        self.frame_5.setMaximumSize(QSize(16777215, 200))
        self.frame_5.setFrameShape(QFrame.WinPanel)
        self.frame_5.setFrameShadow(QFrame.Sunken)
        self.frame_5.setLineWidth(10)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.LogoImg = QFrame(self.frame_5)
        self.LogoImg.setObjectName(u"LogoImg")
        self.LogoImg.setMinimumSize(QSize(154, 154))
        self.LogoImg.setMaximumSize(QSize(154, 154))
        self.LogoImg.setContextMenuPolicy(Qt.NoContextMenu)
        self.LogoImg.setFrameShape(QFrame.WinPanel)
        self.LogoImg.setFrameShadow(QFrame.Sunken)
        self.LogoImg.setLineWidth(10)
        self.horizontalLayout_13 = QHBoxLayout(self.LogoImg)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.Logo = QPushButton(self.LogoImg)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setEnabled(False)
        self.Logo.setMinimumSize(QSize(154, 154))
        self.Logo.setMaximumSize(QSize(154, 154))
        font2 = QFont()
        font2.setKerning(False)
        self.Logo.setFont(font2)
        self.Logo.setFocusPolicy(Qt.NoFocus)
        self.Logo.setContextMenuPolicy(Qt.NoContextMenu)
        self.Logo.setLayoutDirection(Qt.LeftToRight)
        icon5 = QIcon()
        icon5.addFile(u":/svg/manage_accounts_white_48dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Logo.setIcon(icon5)
        self.Logo.setIconSize(QSize(120, 120))
#if QT_CONFIG(shortcut)
        self.Logo.setShortcut(u"")
#endif // QT_CONFIG(shortcut)
        self.Logo.setCheckable(False)
        self.Logo.setFlat(True)

        self.horizontalLayout_13.addWidget(self.Logo, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_10.addWidget(self.LogoImg)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.WinPanel)
        self.frame_6.setFrameShadow(QFrame.Sunken)
        self.frame_6.setLineWidth(10)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(30, 0, 30, 0)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.WinPanel)
        self.frame_7.setFrameShadow(QFrame.Sunken)
        self.frame_7.setLineWidth(10)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.FormPanel = QFrame(self.frame_7)
        self.FormPanel.setObjectName(u"FormPanel")
        self.FormPanel.setFrameShape(QFrame.WinPanel)
        self.FormPanel.setFrameShadow(QFrame.Sunken)
        self.FormPanel.setLineWidth(10)
        self.verticalLayout_7 = QVBoxLayout(self.FormPanel)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 15)
        self.ErroMsg = QLabel(self.FormPanel)
        self.ErroMsg.setObjectName(u"ErroMsg")
        self.ErroMsg.setEnabled(True)
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setKerning(True)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.ErroMsg.setFont(font3)
        self.ErroMsg.setContextMenuPolicy(Qt.NoContextMenu)
        self.ErroMsg.setFrameShape(QFrame.WinPanel)
        self.ErroMsg.setFrameShadow(QFrame.Sunken)
        self.ErroMsg.setLineWidth(10)
        self.ErroMsg.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.ErroMsg)

        self.UsernameLb = QLineEdit(self.FormPanel)
        self.UsernameLb.setObjectName(u"UsernameLb")
        self.UsernameLb.setEnabled(True)
        self.UsernameLb.setMinimumSize(QSize(0, 27))
        self.UsernameLb.setMaximumSize(QSize(16777215, 27))
        font4 = QFont()
        font4.setFamilies([u"Times New Roman"])
        font4.setPointSize(12)
        font4.setStyleStrategy(QFont.PreferAntialias)
        self.UsernameLb.setFont(font4)
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

        self.verticalLayout_7.addWidget(self.UsernameLb)

        self.PasswordLb = QLineEdit(self.FormPanel)
        self.PasswordLb.setObjectName(u"PasswordLb")
        self.PasswordLb.setEnabled(True)
        self.PasswordLb.setMinimumSize(QSize(0, 27))
        self.PasswordLb.setMaximumSize(QSize(16777215, 27))
        self.PasswordLb.setFont(font4)
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

        self.verticalLayout_7.addWidget(self.PasswordLb)

        self.StayConnectBox = QCheckBox(self.FormPanel)
        self.StayConnectBox.setObjectName(u"StayConnectBox")
        self.StayConnectBox.setMinimumSize(QSize(140, 0))
        self.StayConnectBox.setMaximumSize(QSize(140, 16777215))
        font5 = QFont()
        font5.setFamilies([u"Microsoft Sans Serif"])
        font5.setPointSize(10)
        font5.setStyleStrategy(QFont.PreferAntialias)
        self.StayConnectBox.setFont(font5)
        self.StayConnectBox.setTabletTracking(True)
        self.StayConnectBox.setFocusPolicy(Qt.TabFocus)
        self.StayConnectBox.setContextMenuPolicy(Qt.NoContextMenu)
#if QT_CONFIG(shortcut)
        self.StayConnectBox.setShortcut(u"")
#endif // QT_CONFIG(shortcut)
        self.StayConnectBox.setCheckable(True)
        self.StayConnectBox.setChecked(True)
        self.StayConnectBox.setTristate(False)

        self.verticalLayout_7.addWidget(self.StayConnectBox)

        self.LoginBtn = QPushButton(self.FormPanel)
        self.LoginBtn.setObjectName(u"LoginBtn")
        self.LoginBtn.setMinimumSize(QSize(150, 27))
        self.LoginBtn.setMaximumSize(QSize(450, 500))
        self.LoginBtn.setMouseTracking(True)
        self.LoginBtn.setTabletTracking(True)
        self.LoginBtn.setFocusPolicy(Qt.TabFocus)
        self.LoginBtn.setContextMenuPolicy(Qt.NoContextMenu)

        self.verticalLayout_7.addWidget(self.LoginBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_5.addWidget(self.FormPanel)


        self.horizontalLayout_11.addWidget(self.frame_7)


        self.verticalLayout_3.addWidget(self.frame_6)


        self.horizontalLayout_12.addWidget(self.frame_3)


        self.horizontalLayout_9.addWidget(self.frame)

        self.Paginas.addWidget(self.LoginPage)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(411, 208, 49, 16))
        self.Paginas.addWidget(self.page_2)

        self.horizontalLayout_8.addWidget(self.Paginas)


        self.verticalLayout_2.addWidget(self.ContentPages)


        self.horizontalLayout_2.addWidget(self.ContentPanel)

        self.RightModal = QFrame(self.frame_2)
        self.RightModal.setObjectName(u"RightModal")
        self.RightModal.setMaximumSize(QSize(0, 16777215))
        self.RightModal.setFrameShape(QFrame.NoFrame)
        self.RightModal.setFrameShadow(QFrame.Plain)
        self.RightModal.setLineWidth(0)

        self.horizontalLayout_2.addWidget(self.RightModal)


        self.verticalLayout.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Paginas.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ToggleLeftBtn.setText("")
        self.TitleProgram.setText(QCoreApplication.translate("MainWindow", u"MS Administration", None))
        self.MinimizeBtn.setText("")
        self.MaximizeBtn.setText("")
        self.CloseBtn.setText("")
        self.TitlePages.setText("")
        self.ToggleRightBtn.setText("")
        self.TitleLb.setText(QCoreApplication.translate("MainWindow", u"MS Adiministration", None))
        self.Logo.setText("")
        self.ErroMsg.setText("")
        self.UsernameLb.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio ou Email", None))
        self.PasswordLb.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.StayConnectBox.setText(QCoreApplication.translate("MainWindow", u"Manter Conectado ?", None))
        self.LoginBtn.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Page 2", None))
    # retranslateUi

