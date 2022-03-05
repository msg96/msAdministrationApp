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
import os
#############################
####### MODULOS
#############################
from modulos import customFunctions
from assets.styles import style
#############################
########        SUB UIS
#############################
from ..subui_login import subui_Login
from ..subui_home import subui_Home
from ..subui_config import subui_Config
#############################
########        WIDGETS
#############################
from gui.widgets.msBoxLayout.msHBoxLayout import msHBoxLayout
from gui.widgets.msBoxLayout.msVBoxLayout import msVBoxLayout
from gui.widgets.msLabel import msLabel
from gui.widgets.msLmButton import msLmButton
from gui.widgets.msPanel import msPanel
from gui.widgets.msButton import msButton
from gui.widgets.msForm import msForm
#############################
########        VARIABLES
#############################
width = 940
height = 500
animationDelay = 200
animationEffect = QEasingCurve.OutElastic
Svgs = {}
#############################
#############################
###
def LoadIconsUrls(Svgs :dict):
        SvgPath = customFunctions.AppGetUniversalPath("assets/svg/")
        for file in os.listdir(SvgPath):
                if file.endswith(".svg"):
                        filename = file.split("/")[-1].replace(".svg", "")
                        Svgs.update({filename: customFunctions.AppGetFile(SvgPath, file)}) 
########        INITI PARAMS FOR DE MSFORM
def initMainWindow(object :msForm) -> QRect:
        if not object.objectName():
            object.setClassName(u"MainWindow")
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
        #####   PROFILE
        class profile(msPanel):
                def __init__(self, parent: QWidget,  menu: QVBoxLayout):
                        super().__init__(parent)
                        menu.addWidget(self)
                        self.byDesign = msLabel(self)
                        self.byDesign.setGeometry(0, 0, 150, style["topbarheight"]-7)
                        self.applyStyles()
                def applyStyles(self):
                        self.setMinimumHeight(style["topbarheight"]-7)
        #####   HOMEBTN
        class homeBtn(msLmButton):
                def __init__(self, parent: QWidget, menu: QVBoxLayout):
                        super().__init__(parent)
                        menu.addWidget(self, 0, Qt.AlignTop)
                        self.myIcon(Svgs['Home'])
                        self.setText("Home")
                        self.active()
        #####   CLOUDBTN
        class cloudBtn(msLmButton):
                def __init__(self, parent: QWidget, menu: QVBoxLayout):
                        super().__init__(parent)
                        menu.addWidget(self, 0, Qt.AlignTop)
                        self.myIcon(Svgs['cloud_upload_white_48dp'])
                        self.setText("Cloud")
        #####   CONFIGBTN
        class configBtn(msLmButton):
                def __init__(self, parent: QWidget, menu: QVBoxLayout):
                        super().__init__(parent)
                        menu.addWidget(self, 0, Qt.AlignBottom)
                        self.myIcon(Svgs['settings_white_48dp'])
                        self.setText("Configurações")
        #####   CREATE ALL COMPONENTS
        def create(self, parent :leftModal):
                self.leftMenu = msVBoxLayout(parent)
                self.leftMenu.setAlignment(Qt.AlignTop)
                self.leftMenu.setSpacing(5)
                self.leftMenu.setContentsMargins(1, 3, 0, 2)
                ####    PROFILE
                self.profile = self.profile(parent, self.leftMenu)
                ####    MENU BUTTONS
                self.homeBtn = self.homeBtn(parent, self.leftMenu)
                self.cloudBtn = self.cloudBtn(parent, self.leftMenu)
                self.leftMenuSpacer = QSpacerItem(50, 50, QSizePolicy.Expanding, QSizePolicy.Expanding)
                self.leftMenu.addSpacerItem(self.leftMenuSpacer)
                ####    CONFIG BTN
                self.configBtn = self.configBtn(parent, self.leftMenu)
                ####    APPLY STYLE TO ALL MENU COMPONENTS
                self.applyStyles()
########
        def applyStyles(self):
                for i in self.__dict__:
                        try:
                                i.applyStyles()
                        except: 
                                pass
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
                self.setMinimumWidth(0)
                self.setMaximumWidth(0)
                self.Animation= QPropertyAnimation(self, b"minimumWidth")
                self.Animation.setDuration(animationDelay)
                self.Animation.setEasingCurve(animationEffect)
                self.applyStyles()
        def applyStyles(self):
                self.backgroundColor(style["hoverbtns"])
                self.borderTop(0, "solid", style["hoverbtns"])
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
                self.organizer = msHBoxLayout(self)
                # self.organizer.setContentsMargins(10, 10, 10, 10)
                self.pages = [QWidget]
                self.applyStyles()
        def addPage(self, object: QWidget):
                self.organizer.addWidget(object)
                self.pages.append(object)
                object.setVisible(False)
        def showPage(self, pageName):
                for page in self.pages:
                        try:
                                if page.objectName() == pageName:
                                        page.setVisible(True)
                                else:
                                        page.setVisible(False)
                        except:
                                pass
        def applyStyles(self):
                self.borderTop(1, "solid", style["secondarybg"])
                self.borderRight(1, "solid", style["secondarybg"])
########        FOOTER WIDGET
class footer(msPanel):
        def __init__(self, parent: QWidget):
                super(footer, self).__init__(parent)
                self.setMinimumSize(QSize(0, 33))
                self.setMaximumSize(QSize(9999, 33))
                self.setVisible(False)
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
        self.appWindowBox = msHBoxLayout(self.appWindow)
        ####
########        SET SOME CHILDS TO APPWINDOWBOX
        self.leftModal = leftModal(self.appWindowBox)
        self.appWindowSub = appWindowSub(self.appWindowBox)
        ####    ADD CHILDS TO APPWINDOWBOX
        self.appWindowBox.addWidget(self.leftModal)
        self.appWindowBox.addWidget(self.appWindowSub)
        ####
########        BOX FOR ALL CONTENT ELSE LEFTMODAL
        self.bodyBox = msVBoxLayout(self.appWindowSub)
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
        self.contentPanelBox = msHBoxLayout(self.contentPanel)
########        SET SOME CHILDS TO CONTENTPANELBOX
        self.mainContent = mainContent(self.contentPanel)
        self.rightModal = rightModal(self.contentPanel)
        ####    ADD CHILDS TO CONTENTPANELBOX 
        self.contentPanelBox.addWidget(self.mainContent)
        self.contentPanelBox.addWidget(self.rightModal)
########        SET SOME BOX TO RECEIVE CONTENTPAGES AND FOOTER
        self.mainContentBox = msVBoxLayout(self.mainContent)
########        SET SOME CHILDS TO MAINCONTENTBOX
        self.contentPages = contentPages(self.mainContent)
        self.footer = footer(self.mainContent)
        ####    ADD CHILDS TO MAINCONTENTBOX
        self.mainContentBox.addWidget(self.contentPages)
        self.mainContentBox.addWidget(self.footer)
        ####
########        SET SOME BOX ON  TOPBAR
        self.topBarBox = msHBoxLayout(self.topBar)
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
########        SET SOME PAGES TO CONTENTPAGES
        self.homePage = subui_Home()
        self.configPage = subui_Config()
        ####    START PAGES
        self.homePage.start(self.contentPages)
        self.configPage.start(self.contentPages)
        ####    ADD PAGES IN CONTENT PAGES
        self.contentPages.addPage(self.homePage.body)
        self.contentPages.addPage(self.configPage.body)
        
