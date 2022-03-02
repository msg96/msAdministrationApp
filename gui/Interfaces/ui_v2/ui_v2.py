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

from gui.widgets.msLabel.msLabel import msLabel
from gui.widgets.msLmButton.msLmButton import msLmButton
#############################
####### MODULOS
#############################
from ..subui_login import subui_Login
from gui.widgets.msPanel import msPanel
from gui.widgets.msButton import msButton
from gui.widgets.msForm import msForm
from modulos import customFunctions
from assets.styles import style
#############################

class uiV2(object):
    def start(self, mainWindow :msForm):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"MainWindow")
        centerScreen = QApplication.primaryScreen().availableGeometry()
        myWidth = 940
        myHeight = 500
        mainWindow.setGeometry((centerScreen.width() - myWidth) / 2, (centerScreen.height() -  myHeight) / 2 , 940, 500)
        mainWindow.setMinimumSize(QSize(myWidth, myHeight))
        mainWindow.setMaximumSize(QApplication.primaryScreen().availableGeometry().size())
########    CENTRAL WIDGET ~ APPWINDOW
        self.appWindow = msPanel(mainWindow)
        ####    DEFINE TO MAIN WINDOW APPWINDOW TO CENTRALWIDGET
        mainWindow.setCentralWidget(self.appWindow)
        ####
        self.lastPage = msPanel(self)

        self.appWindow.backgroundColor(style["secondarybg"])
        self.appWindow.border(1, "solid", style["secondarybg"])
        self.appWindow.hoverBorder(2, "solid", style["secondarybg"])
        self.appWindow.borderRadius(style["topleftradius"], 0, 0, 0)
########    HORIZONTAL APP WINDOW [LEFT MODAL AND SUB WINDOW]
        self.appWindowBox = QHBoxLayout(self.appWindow)
        self.appWindowBox.setContentsMargins(0, 0, 0, 0)
        self.appWindowBox.setSpacing(0)
        #####
        self.leftModal = msPanel(self.appWindowBox)
        self.leftModal.borderRadius(style["topleftradius"], 0, 0, 0)
        self.leftModal.backgroundColor(style["secondarybg"])
        self.leftModal.setMinimumWidth(style["leftmodalminwidth"])
        self.leftModal.setMaximumWidth(style["leftmodalminwidth"])
        self.appWindowBox.addWidget(self.leftModal)
        #####
        self.appWindowSub = msPanel(self.appWindowBox)
        self.appWindowBox.addWidget(self.appWindowSub)
########    VERTICAL APP SUB WINDOW [TOP AND CONTENT]
        self.appWindowSubBox = QVBoxLayout(self.appWindowSub)
        self.appWindowSubBox.setContentsMargins(0, 0, 0, 0)
        self.appWindowSubBox.setSpacing(0)
        ####
        self.topBar = msPanel(self.appWindowSub)
        self.topBar.setMinimumSize(QSize(0, style["topbarheight"]))
        self.topBar.setMaximumSize(QSize(9999, style["topbarheight"]))
        self.topBar.backgroundColor(style["secondarybg"])
        self.topBar.borderRadius(style["topleftradius"], 0, 0, 0)
        self.appWindowSubBox.addWidget(self.topBar)
        ####
        self.contentPanel = msPanel(self.appWindowSub)
        self.appWindowSubBox.addWidget(self.contentPanel)
########    HORIZONTAL BOX SPLIT [CONTENT AND RIGHT MODAL]
        self.contentPanelBox = QHBoxLayout(self.contentPanel)
        self.contentPanelBox.setContentsMargins(0, 0, 0, 0)
        self.contentPanelBox.setSpacing(0)
        ####    
        self.mainContent = msPanel(self.contentPanel)
        self.mainContent.backgroundColor(style["primarybg"])
        self.mainContent.borderTop(0, "solid", style["secondarybg"])
        self.mainContent.borderLeft(0, "solid", style["secondarybg"])
        self.contentPanelBox.addWidget(self.mainContent)
########    VERTICAL BOX SPLIT [TITLEPAGES CONTENTPAGES FOOTER]
        self.mainContentBox = QVBoxLayout(self.mainContent)
        self.mainContentBox.setContentsMargins(0, 0, 0, 0)
        self.mainContentBox.setSpacing(0)
        ####
        self.contentPages = msPanel(self.mainContent)
        self.contentPages.borderTop(1, "solid", style["secondarybg"])
        self.contentPages.borderRight(1, "solid", style["secondarybg"])
        self.mainContentBox.addWidget(self.contentPages)
        ####
        self.footer = msPanel(self.mainContent)
        self.footer.setMinimumSize(QSize(0, 33))
        self.footer.setMaximumSize(QSize(9999, 33))
        self.footer.backgroundColor(style["primarybg"])
        self.footer.borderRight(1, "solid", style["secondarybg"])
        self.footer.borderBottom(1, "solid", style["secondarybg"])
        self.footer.flatStyle(True)
        self.mainContentBox.addWidget(self.footer)
        ####
        self.rightModal = msPanel(self.contentPanel)
        self.rightModal.backgroundColor(style["hoverbtns"])
        self.rightModal.borderTop(0, "solid", style["hoverbtns"])
        self.rightModal.setMinimumWidth(0)
        self.rightModal.setMaximumWidth(0)
        self.contentPanelBox.addWidget(self.rightModal)

        #####   SCRIPT PARA PEGAR A PASTA RELATIVA QUE FUNCIONE EM [WINDOWS / LINUX / MAC]
        self.SvgPath = customFunctions.AppGetUniversalPath("assets/svg/")
        #####
        self.MenuIcon = QIcon(customFunctions.AppGetFile(self.SvgPath, "menu_white_48dp.svg"))
        self.MenuLeftOpenIcon = QIcon(customFunctions.AppGetFile(self.SvgPath, "menu_open_white_48dp.svg"))
        self.menuRightOpenIcon = QIcon(customFunctions.AppGetFile(self.SvgPath, "menu_open_white_right_48dp.svg"))


        self.topBarBox = QHBoxLayout(self.topBar)
        self.topBarBox.setContentsMargins(0, 0, 0, 0)
        self.topBarBox.setSpacing(0)
        self.topBarBox.setAlignment(Qt.AlignLeft)
        self.toggleLeftModalBtn = msButton(self.topBar)
        self.toggleLeftModalBtn.setMinimumSize(QSize(33, 33))
        self.toggleLeftModalBtn.setMaximumSize(QSize(33, 33))
        self.toggleLeftModalBtn.backgroundColor(style["secondarybg"])
        self.toggleLeftModalBtn.hoverBackgroundColor(style["hoverbtns"])
        self.toggleLeftModalBtn.border(0, "none", "transparent")
        self.toggleLeftModalBtn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.toggleLeftModalBtn.setIcon(self.MenuIcon)
        self.topBarBox.addWidget(self.toggleLeftModalBtn)
        
########        ANIMATIONS CONFIGS :)
        self.AnimDelay = 200
        self.AnimCurve = QEasingCurve.OutSine
########        LEFT MODAL ANIMATION
        self.leftModalOpen = False
        self.leftModalAnimation = QPropertyAnimation(self.leftModal, b"minimumWidth")
        self.leftModalAnimation.setStartValue(style["leftmodalminwidth"])
        self.leftModalAnimation.setEndValue(style["leftmodalmaxwidth"])
        self.leftModalAnimation.setDuration(self.AnimDelay)
        self.leftModalAnimation.setEasingCurve(self.AnimCurve)
########        RIGHT MODAL ANNIMATION
        self.rightModalOpen = False
        self.rightModalAnimation= QPropertyAnimation(self.rightModal, b"minimumWidth")
        self.rightModalAnimation.setStartValue(0)
        self.rightModalAnimation.setEndValue(200)
        self.rightModalAnimation.setDuration(self.AnimDelay)
        self.rightModalAnimation.setEasingCurve(self.AnimCurve)
########        TITLE FOR TOPBAR
        self.titleProgram = QLabel(self.topBar)
        mainWindow.bar = self.titleProgram
        self.titleProgram.setText("MS Administration")
        self.titleProgram.setIndent(15)
        self.titleProgram.setStyleSheet("color: {};".format(style["textcolor"]))
        self.titleProgram.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding))

########        CREATING BUTTONS TO LOGOUTBTN, MINIMIZE MAXIMIZE AND CLOSE WINDOW
        ####    ICONS
        self.minimizeIcon = QIcon(customFunctions.AppGetFile(self.SvgPath, "minimize_white_48dp.svg"))
        self.maximizeIconOff = QIcon(customFunctions.AppGetFile(self.SvgPath, "fullscreen_white_48dp.svg"))
        self.maximizeIconOn = QIcon(customFunctions.AppGetFile(self.SvgPath, "fullscreen_exit_white_48dp.svg"))
        self.closeIcon = QIcon(customFunctions.AppGetFile(self.SvgPath, "close_white_48dp.svg"))
        self.logOutIcon = QIcon(customFunctions.AppGetFile(self.SvgPath, "logout_white_48dp.svg"))
        ####    LOGOUT BTN
        self.logOutBtn = msButton(self.topBar)
        self.logOutBtn.setIcon(self.logOutIcon)
        self.logOutBtn.setMinimumSize(QSize(33, 33))
        self.logOutBtn.backgroundColor("transparent")
        self.logOutBtn.hoverBorder(0, "solid", style["primarybg"])
        self.logOutBtn.hoverBackgroundColor(style["hoverbtns"])
        self.logOutBtn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        ####    MENU RIGHT MODAL BTN
        self.toggleRightModalBtn = msButton(self.topBar)
        self.toggleRightModalBtn.setMinimumSize(QSize(33, 33))
        self.toggleRightModalBtn.setMaximumSize(QSize(33, 33))
        self.toggleRightModalBtn.backgroundColor(style["secondarybg"])
        self.toggleRightModalBtn.hoverBackgroundColor(style["hoverbtns"])
        self.toggleRightModalBtn.border(0, "none", "transparent")
        self.toggleRightModalBtn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.toggleRightModalBtn.setIcon(self.MenuIcon)
        ####    MINIMIZE BTN
        self.minimizeBtn = msButton(self.topBar)
        self.minimizeBtn.setIcon(self.minimizeIcon)
        self.minimizeBtn.setMinimumSize(QSize(33, 33))
        self.minimizeBtn.backgroundColor("transparent")
        self.minimizeBtn.hoverBorder(0, "solid", style["primarybg"])
        self.minimizeBtn.hoverBackgroundColor(style["hoverbtns"])
        self.minimizeBtn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        ####    MAXIMIZE BTN
        self.maximizeBtn = msButton(self.topBar)
        self.maximizeBtn.setIcon(self.maximizeIconOff)
        self.maximizeBtn.setMinimumSize(QSize(33, 33))
        self.maximizeBtn.backgroundColor("transparent")
        self.maximizeBtn.hoverBorder(0, "solid", style["primarybg"])
        self.maximizeBtn.hoverBackgroundColor(style["hoverbtns"])
        self.maximizeBtn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        ####    CLOSE BTN
        self.closeBtn = msButton(self.topBar)
        self.closeBtn.setIcon(self.closeIcon)
        self.closeBtn.setMinimumSize(QSize(33, 33))
        self.closeBtn.backgroundColor("transparent")
        self.closeBtn.hoverBorder(0, "solid", style["primarybg"])
        self.closeBtn.hoverBackgroundColor("#916c0e17")
        self.closeBtn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        ####    ADD TO CONTROLS
        self.topBarBox.addWidget(self.titleProgram)
        self.topBarBox.addWidget(self.logOutBtn)
        self.topBarBox.addWidget(self.toggleRightModalBtn)
        self.topBarBox.addWidget(self.minimizeBtn)
        self.topBarBox.addWidget(self.maximizeBtn)
        self.topBarBox.addWidget(self.closeBtn)
########        LOGIN PAGE :)
        self.LoginUI = subui_Login()
        self.separator = QHBoxLayout(self.contentPages)
        self.LoginUI.start(self.separator)
        self.separator.addWidget(self.LoginUI.body)
        self.LoginUI.body.setVisible(False)
########        BUTTONS FOR LEFTMODAL
        self.leftMenu = QVBoxLayout(self.leftModal)
        self.leftMenu.setAlignment(Qt.AlignTop)
        self.leftMenu.setSpacing(5)
        self.leftMenu.setContentsMargins(1, 3, 0, 2)
        ####    ICONS
        self.homeIcon = customFunctions.AppGetFile(self.SvgPath, "Home.svg")
        self.configIcon = customFunctions.AppGetFile(self.SvgPath, "settings_white_48dp.svg")
        ####    PROFILE
        self.profile = msPanel(self.leftModal)
        self.leftMenu.addWidget(self.profile)
        self.profile.setMinimumHeight(style["topbarheight"]-6)
        self.byDesign = msLabel(self.profile)
        self.byDesign.setGeometry(0, 0, 150, style["topbarheight"]-6)
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setKerning(True)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.byDesign.setText("designed by: Matheus Santos")
        self.byDesign.setFont(font3)
        self.byDesign.color(style["hoverbtns"])


        ####    HOME BTN
        self.homeBtn = msLmButton(self.leftModal)
        self.leftMenu.addWidget(self.homeBtn, 0, Qt.AlignTop)
        self.homeBtn.myIcon(self.homeIcon)
        self.homeBtn.setText("Home")
        self.homeBtn.padronizerBtnLeftMenu()
        self.homeBtn.active()
        ####    SPACER
        self.leftMenuSpacer = QSpacerItem(50, 50, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.leftMenu.addItem(self.leftMenuSpacer)

        ####    CONFIG BTN
        self.configBtn = msLmButton(self.leftModal)
        self.leftMenu.addWidget(self.configBtn, 0, Qt.AlignBottom)
        self.configBtn.myIcon(self.configIcon)
        self.configBtn.setText("Configurações")
        self.configBtn.padronizerBtnLeftMenu()



