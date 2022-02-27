###########################################################################################################################
########    PYSIDE6 IMPORTS                             ~   * IMPORTANT
###########################################################################################################################
from typing import MappingView
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from gui.widgets.msGrip.msGrip import msGrip
#############################
####### MODULOS
from gui.widgets.msPanel import msPanel
from gui.widgets.msButton import msButton
from gui.widgets.msLoginForm import msLoginForm
#############################

class uiV2(object):
    def start(self, mainWindow :msLoginForm):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"MainWindow")
        centerScreen = QApplication.primaryScreen().availableGeometry()
        myWidth = 940
        myHeight = 500
        mainWindow.setGeometry((centerScreen.width() - myWidth) / 2, (centerScreen.height() -  myHeight) / 2 , 940, 500)
########    CENTRAL WIDGET ~ APPWINDOW
        self.appWindow = msPanel(mainWindow)
        ####    DEFINE TO MAIN WINDOW APPWINDOW TO CENTRALWIDGET
        mainWindow.setCentralWidget(self.appWindow)
        ####
        self.appWindow.backgroundColor("#050505")
        self.appWindow.border(0, "solid", "#DD353535")
        self.appWindow.hoverBorder(0, "solid", "#DD404040")
        self.appWindow.borderRadius(15, 0, 0, 0)
########    HORIZONTAL APP WINDOW [LEFT MODAL AND SUB WINDOW]
        self.appWindowBox = QHBoxLayout(self.appWindow)
        self.appWindowBox.setContentsMargins(0, 0, 0, 0)
        self.appWindowBox.setSpacing(0)
        #####
        self.leftModal = msPanel(self.appWindowBox)
        self.leftModal.borderRadius(15, 0, 0, 0)
        self.leftModal.backgroundColor("#111111")
        self.leftModal.setMinimumWidth(0)
        self.leftModal.setMaximumWidth(0)
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
        self.topBar.setMinimumSize(QSize(0, 33))
        self.topBar.setMaximumSize(QSize(9999, 33))
        self.topBar.backgroundColor("#050505")
        mainWindow.bar = self.topBar
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
        self.mainContent.backgroundColor("#101010")
        self.mainContent.borderTop(1, "solid", "#050505")
        self.mainContent.borderLeft(1, "solid", "#050505")
        self.contentPanelBox.addWidget(self.mainContent)
########    VERTICAL BOX SPLIT [TITLEPAGES CONTENTPAGES FOOTER]
        self.mainContentBox = QVBoxLayout(self.mainContent)
        self.mainContentBox.setContentsMargins(0, 0, 0, 0)
        self.mainContentBox.setSpacing(0)
        ####
        self.titlePages = msPanel(self.mainContent)
        self.titlePages.backgroundColor("#090909")
        self.titlePages.setMinimumSize(QSize(0, 33))
        self.titlePages.setMaximumSize(QSize(9999, 33))
        self.mainContentBox.addWidget(self.titlePages)
        ####
        self.contentPages = msPanel(self.mainContent)
        self.contentPages.borderTop(1, "solid", "#050505")
        self.contentPages.borderRight(1, "solid", "#050505")
        self.mainContentBox.addWidget(self.contentPages)
        ####
        self.footer = msPanel(self.mainContent)
        self.footer.setMinimumSize(QSize(0, 33))
        self.footer.setMaximumSize(QSize(9999, 33))
        self.footer.backgroundColor("#101010")
        self.footer.borderRight(1, "solid", "#050505")
        self.footer.flatStyle(True)
        self.mainContentBox.addWidget(self.footer)
        ####
        self.rightModal = msPanel(self.contentPanel)
        self.rightModal.backgroundColor("#111111")
        self.rightModal.borderTop(1, "solid", "#050505")
        self.rightModal.setMinimumWidth(0)
        self.rightModal.setMaximumWidth(0)
        self.contentPanelBox.addWidget(self.rightModal)



        self.MenuIcon = QIcon("C:/Users/sagossi/Desktop/projects/msAdministrationApp/assets/svg/menu_white_48dp.svg")
        self.MenuLeftOpenIcon = QIcon("C:/Users/sagossi/Desktop/projects/msAdministrationApp/assets/svg/menu_open_white_48dp.svg")
        self.menuRightOpenIcon = QIcon("C:/Users/sagossi/Desktop/projects/msAdministrationApp/assets/svg/menu_open_white_right_48dp.svg")


        self.topBarBox = QHBoxLayout(self.topBar)
        self.topBarBox.setContentsMargins(0, 0, 0, 0)
        self.topBarBox.setSpacing(0)
        self.topBarBox.setAlignment(Qt.AlignLeft)
        self.toggleLeftModalBtn = msButton(self.topBar)
        self.toggleLeftModalBtn.setMinimumSize(QSize(33, 33))
        self.toggleLeftModalBtn.setMaximumSize(QSize(33, 33))
        self.toggleLeftModalBtn.backgroundColor("#050505")
        self.toggleLeftModalBtn.hoverBackgroundColor("#66111111")
        self.toggleLeftModalBtn.border(0, "none", "transparent")
        self.topBar.borderRadius(15, 0, 0, 0)
        self.toggleLeftModalBtn.borderRadius(15, 0, 0, 0)
        self.toggleLeftModalBtn.setIcon(self.MenuIcon)
        self.topBarBox.addWidget(self.toggleLeftModalBtn)
        

        self.titlePagesBox = QHBoxLayout(self.titlePages)
        self.titlePagesBox.setContentsMargins(0, 0, 0, 0)
        self.titlePagesBox.setSpacing(0)
        self.titlePagesBox.setAlignment(Qt.AlignRight)
        self.toggleRightModalBtn = msButton(self.titlePages)
        self.toggleRightModalBtn.setMinimumSize(QSize(33, 33))
        self.toggleRightModalBtn.setMaximumSize(QSize(33, 33))
        self.toggleRightModalBtn.backgroundColor("#090909")
        self.toggleRightModalBtn.hoverBackgroundColor("#66111111")
        self.toggleRightModalBtn.border(0, "none", "transparent")
        self.toggleRightModalBtn.borderRadius(15, 0, 0, 0)
        self.toggleRightModalBtn.setIcon(self.MenuIcon)
        self.titlePagesBox.addWidget(self.toggleRightModalBtn)

        self.leftModalOpen = False
        self.leftModalAnimation = QPropertyAnimation(self.leftModal, b"minimumWidth")
        self.leftModalAnimation.setStartValue(0)
        self.leftModalAnimation.setEndValue(200)
        self.leftModalAnimation.setDuration(500)
        self.leftModalAnimation.setEasingCurve(QEasingCurve.OutElastic)

        self.rightModalOpen = False
        self.rightModalAnimation= QPropertyAnimation(self.rightModal, b"minimumWidth")
        self.rightModalAnimation.setStartValue(0)
        self.rightModalAnimation.setEndValue(200)
        self.rightModalAnimation.setDuration(500)
        self.rightModalAnimation.setEasingCurve(QEasingCurve.OutElastic)



        self.leftGrip = msGrip(self.appWindow, "left")
        self.topGrip = msGrip(self.appWindow, "top")
        self.rightGrip = msGrip(self.appWindow, "right")
        self.BottomGrip = msGrip(self.appWindow, "bottom")

