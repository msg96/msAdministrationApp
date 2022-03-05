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
from gui.Interfaces.subui_config.pages.interop import interopPage

from modulos.msVariables import Svgs
###########################################################################################################################
########    WIDGETS
###########################################################################################################################
from gui.Interfaces.subui_config.pages import stylePage
from gui.widgets.msBoxLayout.msHBoxLayout import msHBoxLayout
from gui.widgets.msBoxLayout.msVBoxLayout import msVBoxLayout
from gui.widgets.msButton import msButton
from gui.widgets.msClmButton import msClmButton
from gui.widgets.msPanel import msPanel
###########################################################################################################################
############    
###########################################################################################################################
#####   BODY
class body(msPanel):
    def __init__(self, parent: QWidget):
        super(body, self).__init__(parent)
        self.setObjectName("config")
        self.setMinimumSize(680 - style['leftmodalmaxwidth'], 434)
        self.setMaximumSize(9999,9999)
        self.dependency1 = []
        self.dependency2 = None
        self.applyStyles()
    def applyStyles(self):
        self.backgroundColor(style['primarybg'])
    def showEvent(self, event: QShowEvent) -> None:
        QWidget.showEvent(self, event)
        try:
            self.dependency1[0].active()
            self.dependency2(self.dependency1[0].objectName())
        except:
            pass

#####   LEFTMENU
class leftMenu(msPanel):
#########   SET CLASS FOR EACH BUTTON INSIDE MENU CLASS
    class styleBtn(msClmButton):
        def __init__(self, parent: QWidget):
            super(leftMenu.styleBtn, self).__init__(parent)
            self.setText("Theme")
            self.applyStyles()
        def applyStyles(self):
            pass
    class secondBtn(msClmButton):
        def __init__(self, parent: QWidget):
            super(leftMenu.secondBtn, self).__init__(parent)
            self.setText("Interop")
            self.applyStyles()
        def applyStyles(self):
            pass
#########   INIT THE LEFTMENU
    def __init__(self, parent: QWidget):
        super(leftMenu, self).__init__(parent)
        self.menuItem = []
        self.setMinimumWidth(150)
        self.setMaximumWidth(150)
        self.organizer = msVBoxLayout(self)
        self.organizer.setContentsMargins(5, 5, 5, 5)
        self.organizer.setSpacing(10)
        self.organizer.setAlignment(Qt.AlignTop)
        ####    SET SOME BUTTONS
        self.styleBtn = self.styleBtn(self)
        self.secondBtn = self.secondBtn(self)
        ####    ADD THE BUTTONS TO LEFTMENU
        self.addMenuItem(self.styleBtn, "theme")
        self.addMenuItem(self.secondBtn, "Interop")
        ####    CALL APPLYSTYLES
        self.menuItem[0].active()
        self.applyStyles()

    def addMenuItem(self, object :msButton, objName :str):
        if object in self.menuItem: return
        object.setObjectName(objName)
        object.updateStyles()
        self.menuItem.append(object)
        self.organizer.addWidget(object)

    def applyStyles(self):
#############   STYLES FOR THE LEFTMENU
        self.backgroundColor("transparent")
        self.borderRight(1, "solid", style['separators'])
############    STYLES FOR ALL BUTTONS
        for i in self.__dict__:
            try:
                    i.applyStyles()
            except: 
                    pass
#####   CONTENT
class content(msPanel):
    def __init__(self, parent: QWidget):
        super(content, self).__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.Pages = []
        self.organizer = msHBoxLayout(self)
        self.stylePage = stylePage(self)
        self.interopPage = interopPage(self)
        self.addPage(self.stylePage, "theme")
        self.addPage(self.interopPage, "interop")
        self.Pages[0].show()


    def addPage(self, object :QWidget, objName :str):
        if object in self.Pages: return
        object.setObjectName(objName)
        object.updateStyles()
        object.hide()
        self.Pages.append(object)
        self.organizer.addWidget(object)

    def displayPage(self, objectName: str):
        for page in self.Pages:
            try:
                if page.objectName() == objectName:
                    page.show()
                else:
                    page.hide()
            except:
                pass


class subui_Config(object):
    def start(self, parent: QObject):
        self.parent = parent
        self.body = body(self.parent)
########    SET BOX TO THE BODY
        self.bodyBox = msHBoxLayout(self.body)
        self.bodyBox.setContentsMargins(10, 10, 10, 10)
########    SET SOME CHILDS TO BODYBOX
        self.leftMenu = leftMenu(self.body)
        self.content = content(self.body)
        ####    ADD CHILDS TO BODYBOX
        self.bodyBox.addWidget(self.leftMenu)
        self.bodyBox.addWidget(self.content)
        self.body.dependency1 = self.leftMenu.menuItem
        self.body.dependency2 = self.content.displayPage
        ####
        
########    SET STYLES TO ALL WIDGETS
    def applyStyles(self):
        for i in self.__dict__:
            try:
                i.applyStyles()
            except: 
                pass

