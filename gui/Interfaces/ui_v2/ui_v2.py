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
from fileinput import close
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
###########################################################################################################################
#############################
####### MODULOS
#############################
import os
from gui.widgets.msLabel.msLabel import msLabel
from gui.widgets.msLmButton.msLmButton import msLmButton
from gui.widgets.msBoxLayout.msHBoxLayout import msHBoxLayout
from gui.widgets.msBoxLayout.msVBoxLayout import msVBoxLayout
from ..subui_login import subui_Login
from gui.widgets.msPanel import msPanel
from gui.widgets.msButton import msButton
from gui.widgets.msForm import msForm
from modulos import customFunctions
from assets.styles import style
#############################
#############################
####### VARIABLES
#############################
width = 940
height = 500
animationDelay = 200
animationEffect = QEasingCurve.OutElastic
Svgs = {}
#############################
def LoadIconsUrls(Svgs :dict):
        SvgPath = customFunctions.AppGetUniversalPath("assets/svg/")
        for file in os.listdir(SvgPath):
                if file.endswith(".svg"):
                        filename = file.split("/")[-1].replace(".svg", "")
                        Svgs.update({filename: customFunctions.AppGetFile(SvgPath, file)}) 

def initMainWindow(object :msForm) -> QRect:
        if not object.objectName():
            object.setObjectName(u"MainWindow")
        centerScreen = QApplication.primaryScreen().availableGeometry()
        geometry_ = QRect((centerScreen.width() - width) / 2, (centerScreen.height() -  height) / 2 , width, height)
        object.setGeometry(geometry_)
        object.setMinimumSize(QSize(width, height))
        object.setMaximumSize(9999, 9999)
        return geometry_
########        APPWINDOW WIDGET
class appWindow(msPanel):
        def __init__(self, parent: msForm):
                super(appWindow, self).__init__(parent)
                self.setGeometry(initMainWindow(parent))
                ######  DEFINE THIS FRAME TO CENTRAL WIDGET
                parent.setCentralWidget(self)
                self.applyStyles()
        def applyStyles(self):
                self.backgroundColor(style["secondarybg"])
                self.border(1, "solid", style["secondarybg"])
                self.hoverBorder(2, "solid", style["secondarybg"])
                self.borderRadius(style["topleftradius"], 0, 0, 0)
########        LEFTMODAL WIDGET
class leftModal(msPanel):
        def __init__(self, parent: QWidget):
                super(leftModal, self).__init__(parent)
                self.leftMenu = leftMenu()
                self.leftMenu.create(self)
                self.isOpen = False
                self.Animation = QPropertyAnimation(self, b"minimumWidth")
                self.Animation.setDuration(animationDelay)
                self.Animation.setEasingCurve(animationEffect)
                self.applyStyles()
        def applyStyles(self):
                self.borderRadius(style["topleftradius"], 0, 0, 0)
                self.backgroundColor(style["secondarybg"])
                self.setMinimumWidth(style["leftmodalminwidth"])
                self.setMaximumWidth(style["leftmodalminwidth"])
                self.Animation.setStartValue(style["leftmodalminwidth"])
                self.Animation.setEndValue(style["leftmodalmaxwidth"])
        def toggle(self, btn :msButton):
                if self.Animation.state() != self.Animation.Stopped: return
                if self.isOpen:
                        self.isOpen = False
                        btn.setIcon(QIcon(Svgs['menu_white_48dp']))
                        btn.backgroundColor(style["secondarybg"])
                        btn.hoverBackgroundColor(style["hoverbtns"])
                        self.Animation.setDirection(self.Animation.Backward)
                        self.Animation.start()
                else:
                        self.isOpen = True
                        btn.setIcon(QIcon(Svgs['menu_open_white_48dp']))
                        btn.backgroundColor(style["secondarybg"])
                        btn.hoverBackgroundColor(style["hoverbtns"])
                        self.Animation.setDirection(self.Animation.Forward)
                        self.Animation.start()
########        LEFTMENU WIDGET
class leftMenu(object):
        def create(self, parent :leftModal):
                self.leftMenu = QVBoxLayout(parent)
                self.leftMenu.setAlignment(Qt.AlignTop)
                self.leftMenu.setSpacing(5)
                self.leftMenu.setContentsMargins(1, 3, 0, 2)
                ####    PROFILE
                self.profile = msPanel(parent)
                self.leftMenu.addWidget(self.profile)
                self.profile.setMinimumHeight(style["topbarheight"]-7)
                self.byDesign = msLabel(self.profile)
                self.byDesign.setGeometry(0, 0, 150, style["topbarheight"]-7)
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
                self.homeBtn = msLmButton(parent)
                self.leftMenu.addWidget(self.homeBtn, 0, Qt.AlignTop)
                self.homeBtn.myIcon(Svgs['Home'])
                self.homeBtn.setText("Home")
                self.homeBtn.active()
                ####    SPACER
                self.leftMenuSpacer = QSpacerItem(50, 50, QSizePolicy.Expanding, QSizePolicy.Expanding)
                self.leftMenu.addItem(self.leftMenuSpacer)
                ####    CONFIG BTN
                self.configBtn = msLmButton(parent)
                self.leftMenu.addWidget(self.configBtn, 0, Qt.AlignBottom)
                self.configBtn.myIcon(Svgs['settings_white_48dp'])
                self.configBtn.setText("Configurações")
########        APPWINDOWSUB WIDGET
class appWindowSub(msPanel):
        def __init__(self, parent: QWidget):
                super(appWindowSub, self).__init__(parent)
                self.applyStyles()
        def applyStyles(self):
                self.backgroundColor(style['primarybg'])
                pass
########        TOPBAR WIDGET
class topBar(msPanel):
        def __init__(self, parent: QWidget):
                super(topBar, self).__init__(parent)
                self.applyStyles()
        def applyStyles(self):
                self.setMinimumSize(QSize(0, style["topbarheight"]))
                self.setMaximumSize(QSize(9999, style["topbarheight"]))
                self.backgroundColor(style["secondarybg"])
                self.borderRadius(style["topleftradius"], 0, 0, 0)
########        CONTENTPANEL WIDGET
class contentPanel(msPanel):
        def __init__(self, parent: QWidget):
                super(contentPanel, self).__init__(parent)
                self.applyStyles()
        def applyStyles(self):
                pass
########        MAINCONTENT WIDGET
class mainContent(msPanel):
        def __init__(self, parent: QWidget):
                super(mainContent, self).__init__(parent)
                self.applyStyles()
        def applyStyles(self):
                self.backgroundColor(style["primarybg"])
                self.borderTop(0, "solid", style["secondarybg"])
                self.borderLeft(0, "solid", style["secondarybg"])
########        RIGHTMODAL WIDGET
class rightModal(msPanel):
        def __init__(self, parent: QWidget):
                super(rightModal, self).__init__(parent)
                self.isOpen = False
                self.Animation= QPropertyAnimation(self, b"minimumWidth")
                self.Animation.setDuration(animationDelay)
                self.Animation.setEasingCurve(animationEffect)
                self.applyStyles()
        def applyStyles(self):
                self.backgroundColor(style["hoverbtns"])
                self.borderTop(0, "solid", style["hoverbtns"])
                self.setMinimumWidth(0)
                self.setMaximumWidth(0)
                self.Animation.setStartValue(0)
                self.Animation.setEndValue(200)
        def toggle(self, btn :msButton):
                if self.Animation.state() != self.Animation.Stopped: return
                if self.isOpen:
                        self.isOpen = False
                        btn.setIcon(QIcon(Svgs['menu_white_48dp']))
                        btn.backgroundColor(style["secondarybg"])
                        btn.hoverBackgroundColor(style["hoverbtns"])
                        self.Animation.setDirection(self.Animation.Backward)
                        self.Animation.start()     
                else:
                        self.isOpen = True
                        btn.setIcon(QIcon(Svgs['menu_open_white_right_48dp']))
                        btn.backgroundColor(style["hoverbtns"])
                        btn.hoverBackgroundColor(style["hoverbtns"])
                        self.Animation.setDirection(self.Animation.Forward)
                        self.Animation.start()
########        CONTENTPAGES WIDGET
class contentPages(msPanel):
        def __init__(self, parent: QWidget):
                super(contentPages, self).__init__(parent)
                self.applyStyles()
        def applyStyles(self):
                self.borderTop(1, "solid", style["secondarybg"])
                self.borderRight(1, "solid", style["secondarybg"])
########        FOOTER WIDGET
class footer(msPanel):
        def __init__(self, parent: QWidget):
                super(footer, self).__init__(parent)
                self.setMinimumSize(QSize(0, 33))
                self.setMaximumSize(QSize(9999, 33))
                self.applyStyles()
        def applyStyles(self):
                self.backgroundColor(style["primarybg"])
                self.borderRight(1, "solid", style["secondarybg"])
                self.borderBottom(1, "solid", style["secondarybg"])
                self.flatStyle(True)
########        TOGGLEMODALEFTBTN WIDGET
class toggleModalLeftBtn(msButton):
        def __init__(self, parent: QWidget):
                super(toggleModalLeftBtn, self).__init__(parent)
                self.setMinimumSize(QSize(33, 33))   
                self.setMaximumSize(QSize(33, 33))
                self.setIcon(QIcon(Svgs['menu_white_48dp']))
                self.applyStyles()
        def applyStyles(self):
                self.backgroundColor(style["secondarybg"])
                self.hoverBackgroundColor(style["hoverbtns"])
                self.border(0, "none", "transparent")
########        TITLEPROGRAM WIDGET
class titleProgram(msLabel):
        def __init__(self, parent: QWidget, mainWindow :msForm):
                super(titleProgram, self).__init__(parent)          
                mainWindow.bar = self
                self.setText(mainWindow.windowTitle())
                self.setIndent(15)
                self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding))
                self.applyStyles()
        def applyStyles(self):
                self.color(style["textcolor"])
########        LOGOUTBTNN WIDGET
class logOutBtn(msButton):
        def __init__(self, parent: QWidget):
                super(logOutBtn, self).__init__(parent)
                self.setIcon(QIcon(Svgs['logout_white_48dp']))
                self.setMinimumSize(QSize(33, 33))
                self.applyStyles()
        def applyStyles(self):
                self.backgroundColor("transparent")
                self.hoverBorder(0, "solid", style["primarybg"])
                self.hoverBackgroundColor(style["hoverbtns"])
########        TOGGLEMODALRIGHTBTN WIDGET
class toggleModalRightBtn(msButton):
        def __init__(self, parent: QWidget):
                super(toggleModalRightBtn, self).__init__(parent)
                self.setMinimumSize(QSize(33, 33))
                self.setMaximumSize(QSize(33, 33))
                self.setIcon(QIcon(Svgs['menu_white_48dp']))
                self.applyStyles()
        def applyStyles(self):
                self.backgroundColor(style["secondarybg"])
                self.hoverBackgroundColor(style["hoverbtns"])
                self.border(0, "none", "transparent")
########        MINIMIZEBTN WIDGET
class minimizeBtn(msButton):
        def __init__(self, parent: QWidget):
                super(minimizeBtn, self).__init__(parent)
                self.setIcon(QIcon(Svgs['minimize_white_48dp']))
                self.setMinimumSize(QSize(33, 33))
                self.applyStyles()
        def applyStyles(self):
                self.backgroundColor("transparent")
                self.hoverBorder(0, "solid", style["primarybg"])
                self.hoverBackgroundColor(style["hoverbtns"])
########        MAXIMIZEBTN WIDGET
class maximizeBtn(msButton):
        def __init__(self, parent: QWidget):
                super(maximizeBtn, self).__init__(parent)
                self.setIcon(QIcon(Svgs['fullscreen_white_48dp']))
                self.setMinimumSize(QSize(33, 33))
                self.applyStyles()
        def applyStyles(self):
                self.backgroundColor("transparent")
                self.hoverBorder(0, "solid", style["primarybg"])
                self.hoverBackgroundColor(style["hoverbtns"])
########        CLOSEBTN WIDGET
class closeBtn(msButton):
        def __init__(self, parent: QWidget):
                super(closeBtn, self).__init__(parent)
                self.setIcon(QIcon(Svgs['close_white_48dp']))
                self.setMinimumSize(QSize(33, 33))
                self.hoverBackgroundColor("#916c0e17")
                self.applyStyles()
        def applyStyles(self):
                self.backgroundColor("transparent")
                self.hoverBorder(0, "solid", style["primarybg"])           
########

#####   PRINCIPAL CLASS OBJECT
class uiV2(object):
    def start(self, mainWindow :msForm):
        LoadIconsUrls(Svgs)
########        SOME PARAMS OF GLOBAL TO INSIDE THE CLASS
        self.Svgs = Svgs
        self.AnimDelay = animationDelay
        self.AnimCurve = animationEffect
########        START CLASS APPWINDOW
        self.appWindow = appWindow(mainWindow)
        ####
########        SET SOME BOX FOR APPWINDOW USE CHILDS
        self.appWindowBox = QHBoxLayout(self.appWindow)
        self.appWindowBox.setContentsMargins(0, 0, 0, 0)
        self.appWindowBox.setSpacing(0)
        ####
########        SET SOME CHILDS TO APPWINDOWBOX
        self.leftModal = leftModal(self.appWindowBox)
        self.appWindowSub = appWindowSub(self.appWindowBox)
        ####    ADD CHILDS TO APPWINDOWBOX
        self.appWindowBox.addWidget(self.leftModal)
        self.appWindowBox.addWidget(self.appWindowSub)
        ####
########        BOX FOR ALL CONTENT ELSE LEFTMODAL
        self.bodyBox = QVBoxLayout(self.appWindowSub)
        self.bodyBox.setContentsMargins(0, 0, 0, 0)
        self.bodyBox.setSpacing(0)
########        SET SOME CHILDS TO BODYBOX
        self.topBar = topBar(self.appWindowSub)
        self.contentPanel = contentPanel(self.appWindowSub)
        self.LoginUI = subui_Login()
        self.LoginUI.start(self.appWindowSub)
        self.LoginUI.body.setVisible(False)
        ####    ADD CHILDS TO BODYBOX
        self.bodyBox.addWidget(self.topBar)
        self.bodyBox.addWidget(self.contentPanel)
        self.bodyBox.addWidget(self.LoginUI.body, 0, Qt.AlignVCenter | Qt.AlignHCenter)
        ####
########        SET SOME BOX TO RECEIVE OUR CONTENT AND RIGHTMODAL
        self.contentPanelBox = QHBoxLayout(self.contentPanel)
        self.contentPanelBox.setContentsMargins(0, 0, 0, 0)
        self.contentPanelBox.setSpacing(0)
########        SET SOME CHILDS TO CONTENTPANELBOX
        self.mainContent = mainContent(self.contentPanel)
        self.rightModal = rightModal(self.contentPanel)
        ####    ADD CHILDS TO CONTENTPANELBOX 
        self.contentPanelBox.addWidget(self.mainContent)
        self.contentPanelBox.addWidget(self.rightModal)
########        SET SOME BOX TO RECEIVE CONTENTPAGES AND FOOTER
        self.mainContentBox = QVBoxLayout(self.mainContent)
        self.mainContentBox.setContentsMargins(0, 0, 0, 0)
        self.mainContentBox.setSpacing(0)
########        SET SOME CHILDS TO MAINCONTENTBOX
        self.contentPages = contentPages(self.mainContent)
        self.footer = footer(self.mainContent)
        ####    ADD CHILDS TO MAINCONTENTBOX
        self.mainContentBox.addWidget(self.contentPages)
        self.mainContentBox.addWidget(self.footer)
        ####
########        SET SOME BOX ON  TOPBAR
        self.topBarBox = QHBoxLayout(self.topBar)
        self.topBarBox.setContentsMargins(0, 0, 0, 0)
        self.topBarBox.setSpacing(0)
        self.topBarBox.setAlignment(Qt.AlignLeft)
        ####    SET SOME CHILDS TO TOPBARBOX
        self.toggleLeftModalBtn = toggleModalLeftBtn(self.topBar)
        self.titleProgram = titleProgram(self.topBar, mainWindow)
        self.logOutBtn = logOutBtn(self.topBar)
        self.toggleRightModalBtn = toggleModalRightBtn(self.topBar)
        self.minimizeBtn = minimizeBtn(self.topBar)
        self.maximizeBtn = maximizeBtn(self.topBar)
        self.closeBtn = closeBtn(self.topBar)
        ####    ADD CHILDS TO TOPBARBOX
        self.topBarBox.addWidget(self.toggleLeftModalBtn)       
        self.topBarBox.addWidget(self.titleProgram)
        self.topBarBox.addWidget(self.logOutBtn)
        self.topBarBox.addWidget(self.toggleRightModalBtn)
        self.topBarBox.addWidget(self.minimizeBtn)
        self.topBarBox.addWidget(self.maximizeBtn)
        self.topBarBox.addWidget(self.closeBtn)
########
