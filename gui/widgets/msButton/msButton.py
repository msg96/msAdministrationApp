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
class msButton(QPushButton):
    def __init__(self, parent :QWidget):
        super(msButton, self).__init__()
        if not self.objectName():
            self.setObjectName(str(hash(self)))
        try:
            self.setParent(parent)
            self.setGeometry(parent.geometry())
        except:
            pass
########    PARAMETERS 
        self.styled = {
        "background-color": "",             "color": "",                    "flat-style": False,
        "border-left-width": 0,             "border-left-style": "",        "border-left-color": "",
        "border-right-width": 0,            "border-right-style": "",       "border-right-color": "",
        "border-top-width": 0,              "border-top-style": "",         "border-top-color": "",
        "border-bottom-width": 0,           "border-bottom-style": "",      "border-bottom-color": "",
        "border-top-left-radius": 0,        "border-top-right-radius": 0,   "border-bottom-right-radius": 0,        "border-bottom-left-radius": 0
        }
        ####    HOVER
        self.hoverStyled = {
        "background-color": "",             "color": "",                    "flat-style": False,
        "border-left-width": 0,             "border-left-style": "",        "border-left-color": "",
        "border-right-width": 0,            "border-right-style": "",       "border-right-color": "",
        "border-top-width": 0,              "border-top-style": "",         "border-top-color": "",
        "border-bottom-width": 0,           "border-bottom-style": "",      "border-bottom-color": "",
        "border-top-left-radius": 0,        "border-top-right-radius": 0,   "border-bottom-right-radius": 0,        "border-bottom-left-radius": 0
        }
        ####    PRESS
        self.pressStyled = {
        "background-color": "",             "color": "",                    "flat-style": False,
        "border-left-width": 0,             "border-left-style": "",        "border-left-color": "",
        "border-right-width": 0,            "border-right-style": "",       "border-right-color": "",
        "border-top-width": 0,              "border-top-style": "",         "border-top-color": "",
        "border-bottom-width": 0,           "border-bottom-style": "",      "border-bottom-color": "",
        "border-top-left-radius": 0,        "border-top-right-radius": 0,   "border-bottom-right-radius": 0,        "border-bottom-left-radius": 0
        }
########
        self.updateStyles()
########        
###########################################################################################################################################
########    METHODS FOR THIS OBJECT
###########################################################################################################################################
####    SET CLASS NAME :)
    def setClassName(self, name :str):
        if self.objectName() != name:
            self.setObjectName(name)
            self.updateStyles()
####    BACKGROUND CHANGE COLOR   
    def backgroundColor(self, color :str):
        self.styled["background-color"] = color
        self.updateStyles()
    ####    HOVER
    def hoverBackgroundColor(self, color :str):
        self.hoverStyled["background-color"] = color
        self.updateStyles()
    ####    PRESS
    def pressBackgroundColor(self, color :str):
        self.pressStyled["background-color"] = color
        self.updateStyles()
####    FLATSTYLE CHANGE
    def flatStyle(self, value :bool):
        self.styled["flat-style"] = value
        self.updateStyles()
    ####    HOVER
    def hoverFlatStyle(self, value :bool):
        self.hoverStyled["flat-style"] = value
        self.updateStyles()
    ####    PRESS
    def pressFlatStyle(self, value :bool):
        self.pressStyled["flat-style"] = value
        self.updateStyles()
####    BORDER PARAMS
    def border(self, width :int, style :str, color :str):
        self.styled["border-left-width"] = self.styled["border-right-width"] = self.styled["border-top-width"] = self.styled["border-bottom-width"] = width
        self.styled["border-left-style"] = self.styled["border-right-style"] = self.styled["border-top-style"] = self.styled["border-bottom-style"] = style
        self.styled["border-left-color"] = self.styled["border-right-color"] = self.styled["border-top-color"] = self.styled["border-bottom-color"] = color
        self.updateStyles()
    ####    HOVER
    def hoverBorder(self, width :int, style :str, color :str):
        self.hoverStyled["border-left-width"] = self.hoverStyled["border-right-width"] = self.hoverStyled["border-top-width"] = self.hoverStyled["border-bottom-width"] = width
        self.hoverStyled["border-left-style"] = self.hoverStyled["border-right-style"] = self.hoverStyled["border-top-style"] = self.hoverStyled["border-bottom-style"] = style
        self.hoverStyled["border-left-color"] = self.hoverStyled["border-right-color"] = self.hoverStyled["border-top-color"] = self.hoverStyled["border-bottom-color"] = color
        self.updateStyles()
    ####    PRESS
    def pressBorder(self, width :int, style :str, color :str):
        self.pressStyled["border-left-width"] = self.pressStyled["border-right-width"] = self.pressStyled["border-top-width"] = self.pressStyled["border-bottom-width"] = width
        self.pressStyled["border-left-style"] = self.pressStyled["border-right-style"] = self.pressStyled["border-top-style"] = self.pressStyled["border-bottom-style"] = style
        self.pressStyled["border-left-color"] = self.pressStyled["border-right-color"] = self.pressStyled["border-top-color"] = self.pressStyled["border-bottom-color"] = color
        self.updateStyles()
####    BORDERLEFT CHANGE PARAMS
    def borderLeft(self, width :int, style :str, color :str):
        self.styled["border-left-width"] = width
        self.styled["border-left-style"] = style
        self.styled["border-left-color"] = color
        self.updateStyles()
    ####    HOVER
    def hoverBorderLeft(self, width :int, style :str, color :str):
        self.hoverStyled["border-left-width"] = width
        self.hoverStyled["border-left-style"] = style
        self.hoverStyled["border-left-color"] = color
        self.updateStyles()
    ####    PRESS
    def pressBorderLeft(self, width :int, style :str, color :str):
        self.pressStyled["border-left-width"] = width
        self.pressStyled["border-left-style"] = style
        self.pressStyled["border-left-color"] = color
        self.updateStyles()
####    BORDERRIGHT CHANGE PARAMS
    def borderRight(self, width :int, style :str, color :str):
        self.styled["border-right-width"] = width
        self.styled["border-right-style"] = style
        self.styled["border-right-color"] = color
        self.updateStyles()
    ####    HOVER
    def hoverBorderRight(self, width :int, style :str, color :str):
        self.hoverStyled["border-right-width"] = width
        self.hoverStyled["border-right-style"] = style
        self.hoverStyled["border-right-color"] = color
        self.updateStyles()
    ####    PRESS
    def pressBorderRight(self, width :int, style :str, color :str):
        self.pressStyled["border-right-width"] = width
        self.pressStyled["border-right-style"] = style
        self.pressStyled["border-right-color"] = color
        self.updateStyles()
####    BORDERTOP CHANGE PARAMS
    def borderTop(self, width :int, style :str, color :str):
        self.styled["border-top-width"] = width
        self.styled["border-top-style"] = style
        self.styled["border-top-color"] = color
        self.updateStyles()
    ####    HOVER
    def hoverBorderTop(self, width :int, style :str, color :str):
        self.hoverStyled["border-top-width"] = width
        self.hoverStyled["border-top-style"] = style
        self.hoverStyled["border-top-color"] = color
        self.updateStyles()
    ####    PRESS
    def pressBorderTop(self, width :int, style :str, color :str):
        self.pressStyled["border-top-width"] = width
        self.pressStyled["border-top-style"] = style
        self.pressStyled["border-top-color"] = color
        self.updateStyles()
####    BORDER BOTTOM CHANGE PARAMS
    def borderBottom(self, width :int, style :str, color :str):
        self.styled["border-bottom-width"] = width
        self.styled["border-bottom-style"] = style
        self.styled["border-bottom-color"] = color
        self.updateStyles()
    ####    HOVER
    def hoverBorderBottom(self, width :int, style :str, color :str):
        self.hoverStyled["border-bottom-width"] = width
        self.hoverStyled["border-bottom-style"] = style
        self.hoverStyled["border-bottom-color"] = color
        self.updateStyles()
    ####    PRESS
    def pressBorderBottom(self, width :int, style :str, color :str):
        self.pressStyled["border-bottom-width"] = width
        self.pressStyled["border-bottom-style"] = style
        self.pressStyled["border-bottom-color"] = color
        self.updateStyles()
####    BORDER RADIUS CHANGE PARAMS
    def borderRadius(self, topleft :int, topright :int, bottomright :int, bottomleft :int):
        self.styled["border-top-left-radius"] =     topleft
        self.styled["border-top-right-radius"] =    topright
        self.styled["border-bottom-right-radius"] = bottomright
        self.styled["border-bottom-left-radius"] =  bottomleft
        self.updateStyles()
    ####    HOVER
    def hoverBorderRadius(self, topleft :int, topright :int, bottomright :int, bottomleft :int):
        self.hoverStyled["border-top-left-radius"] = topleft
        self.hoverStyled["border-top-right-radius"] = topright
        self.hoverStyled["border-bottom-right-radius"] = bottomright
        self.hoverStyled["border-bottom-left-radius"] =  bottomleft
        self.updateStyles()
    ####    PRESS
    def pressBorderRadius(self, topleft :int, topright :int, bottomright :int, bottomleft :int):
        self.pressStyled["border-top-left-radius"] =     topleft
        self.pressStyled["border-top-right-radius"] =    topright
        self.pressStyled["border-bottom-right-radius"] = bottomright
        self.pressStyled["border-bottom-left-radius"] =  bottomleft
        self.updateStyles()       
####    UPDATE STYLESHEETS
    def updateStyles(self):
########    DEFINE SOME CHECKS TO STYLING   ####
        ####
        objectType = self.__class__.__name__
########    SOME PARAMS TO FLAT OPTIONS
        flatColor = "#02010101"
        backgroundColor      = self.styled["background-color"]      if not self.styled["flat-style"]      else flatColor
        hoverBackgroundColor = self.hoverStyled["background-color"] if not self.hoverStyled["flat-style"] else flatColor
        pressBackgroundColor = self.pressStyled["background-color"] if not self.pressStyled["flat-style"] else flatColor
########
##########################################################################################################################################
########    APPEND STYLE TO AN STRING
##########################################################################################################################################   
        style = "{}#{} {{\n".format(objectType, self.objectName())
        #
        if self.styled["background-color"] != "":           style += "background-color: {};\n".format(backgroundColor)
        if self.styled["color"] != "":                      style += "color: {};\n".format(self.styled["color"])
        if self.styled["border-left-width"]:                style += "border-left-width: {}px;\n".format(self.styled["border-left-width"])
        if self.styled["border-left-style"] != "":          style += "border-left-style: {};\n".format(self.styled["border-left-style"])
        if self.styled["border-left-color"] != "":          style += "border-left-color: {};\n".format(self.styled["border-left-color"])
        if self.styled["border-right-width"]:               style += "border-right-width: {}px;\n".format(self.styled["border-right-width"])
        if self.styled["border-right-style"] != "":         style += "border-right-style: {};\n".format(self.styled["border-right-style"])
        if self.styled["border-right-color"] != "":         style += "border-right-color: {};\n".format(self.styled["border-right-color"])
        if self.styled["border-top-width"]:                 style += "border-top-width: {}px;\n".format(self.styled["border-top-width"])
        if self.styled["border-top-style"] != "":           style += "border-top-style: {};\n".format(self.styled["border-top-style"])
        if self.styled["border-top-color"] != "":           style += "border-top-color: {};\n".format(self.styled["border-top-color"])
        if self.styled["border-bottom-width"]:              style += "border-bottom-width: {}px;\n".format(self.styled["border-bottom-width"])
        if self.styled["border-bottom-style"] != "":        style += "border-bottom-style: {};\n".format(self.styled["border-bottom-style"])
        if self.styled["border-bottom-color"] != "":        style += "border-bottom-color: {};\n".format(self.styled["border-bottom-color"])
        if self.styled["border-top-left-radius"]:           style += "border-top-left-radius: {}px;\n".format(self.styled["border-top-left-radius"])
        if self.styled["border-top-right-radius"]:          style += "border-top-right-radius: {}px;\n".format(self.styled["border-top-right-radius"])
        if self.styled["border-bottom-right-radius"]:       style += "border-bottom-right-radius: {}px;\n".format(self.styled["border-bottom-right-radius"])
        if self.styled["border-bottom-left-radius"]:        style += "border-bottom-left-radius: {}px;\n".format(self.styled["border-bottom-left-radius"])
        #
        style += "\n}\n"
###########################################################################################################################################
########    APEEND HOVER STYLE TO AN STRING
###########################################################################################################################################
        hoverStyle = "{}#{}:hover {{\n".format(objectType, self.objectName())
        #
        if self.hoverStyled["background-color"] != "":              hoverStyle += "background-color: {};\n".format(hoverBackgroundColor)
        if self.hoverStyled["color"] != "":                         hoverStyle += "color: {};\n".format(self.hoverStyled["color"])
        if self.hoverStyled["border-left-width"]:                   hoverStyle += "border-left-width: {}px;\n".format(self.hoverStyled["border-left-width"])
        if self.hoverStyled["border-left-style"] != "":             hoverStyle += "border-left-style: {};\n".format(self.hoverStyled["border-left-style"])
        if self.hoverStyled["border-left-color"] != "":             hoverStyle += "border-left-color: {};\n".format(self.hoverStyled["border-left-color"])
        if self.hoverStyled["border-right-width"]:                  hoverStyle += "border-right-width: {}px;\n".format(self.hoverStyled["border-right-width"])
        if self.hoverStyled["border-right-style"] != "":            hoverStyle += "border-right-style: {};\n".format(self.hoverStyled["border-right-style"])
        if self.hoverStyled["border-right-color"] != "":            hoverStyle += "border-right-color: {};\n".format(self.hoverStyled["border-right-color"])
        if self.hoverStyled["border-top-width"]:                    hoverStyle += "border-top-width: {}px;\n".format(self.hoverStyled["border-top-width"])
        if self.hoverStyled["border-top-style"] != "":              hoverStyle += "border-top-style: {};\n".format(self.hoverStyled["border-top-style"])
        if self.hoverStyled["border-top-color"] != "":              hoverStyle += "border-top-color: {};\n".format(self.hoverStyled["border-top-color"])
        if self.hoverStyled["border-bottom-width"]:                 hoverStyle += "border-bottom-width: {}px;\n".format(self.hoverStyled["border-bottom-width"])
        if self.hoverStyled["border-bottom-style"] != "":           hoverStyle += "border-bottom-style: {};\n".format(self.hoverStyled["border-bottom-style"])
        if self.hoverStyled["border-bottom-color"] != "":           hoverStyle += "border-bottom-color: {};\n".format(self.hoverStyled["border-bottom-color"])
        if self.hoverStyled["border-top-left-radius"]:              hoverStyle += "border-top-left-radius: {}px;\n".format(self.hoverStyled["border-top-left-radius"])
        if self.hoverStyled["border-top-right-radius"]:             hoverStyle += "border-top-right-radius: {}px;\n".format(self.hoverStyled["border-top-right-radius"])
        if self.hoverStyled["border-bottom-right-radius"]:          hoverStyle += "border-bottom-right-radius: {}px;\n".format(self.hoverStyled["border-bottom-right-radius"])
        if self.hoverStyled["border-bottom-left-radius"]:           hoverStyle += "border-bottom-left-radius: {}px;\n".format(self.hoverStyled["border-bottom-left-radius"])
        #
        hoverStyle += "\n}\n"
###########################################################################################################################################
########    APPEND PRESS STYLE TO AN STRING
###########################################################################################################################################
        pressStyle = "{}#{}:pressed {{\n".format(objectType, self.objectName())
        #
        if self.pressStyled["background-color"] != "":               pressStyle += "background-color: {};\n".format(pressBackgroundColor)
        if self.pressStyled["color"] != "":                          pressStyle += "color: {};\n".format(self.pressStyled["color"])
        if self.pressStyled["border-left-width"]:                    pressStyle += "border-left-width: {}px;\n".format(self.pressStyled["border-left-width"])
        if self.pressStyled["border-left-style"] != "":              pressStyle += "border-left-style: {};\n".format(self.pressStyled["border-left-style"])
        if self.pressStyled["border-left-color"] != "":              pressStyle += "border-left-color: {};\n".format(self.pressStyled["border-left-color"])
        if self.pressStyled["border-right-width"]:                   pressStyle += "border-right-width: {}px;\n".format(self.pressStyled["border-right-width"])
        if self.pressStyled["border-right-style"] != "":             pressStyle += "border-right-style: {};\n".format(self.pressStyled["border-right-style"])
        if self.pressStyled["border-right-color"] != "":             pressStyle += "border-right-color: {};\n".format(self.pressStyled["border-right-color"])
        if self.pressStyled["border-top-width"]:                     pressStyle += "border-top-width: {}px;\n".format(self.pressStyled["border-top-width"])
        if self.pressStyled["border-top-style"] != "":               pressStyle += "border-top-style: {};\n".format(self.pressStyled["border-top-style"])
        if self.pressStyled["border-top-color"] != "":               pressStyle += "border-top-color: {};\n".format(self.pressStyled["border-top-color"])
        if self.pressStyled["border-bottom-width"]:                  pressStyle += "border-bottom-width: {}px;\n".format(self.pressStyled["border-bottom-width"])
        if self.pressStyled["border-bottom-style"] != "":            pressStyle += "border-bottom-style: {};\n".format(self.pressStyled["border-bottom-style"])
        if self.pressStyled["border-bottom-color"] != "":            pressStyle += "border-bottom-color: {};\n".format(self.pressStyled["border-bottom-color"])
        if self.pressStyled["border-top-left-radius"]:               pressStyle += "border-top-left-radius: {}px;\n".format(self.pressStyled["border-top-left-radius"])
        if self.pressStyled["border-top-right-radius"]:              pressStyle += "border-top-right-radius: {}px;\n".format(self.pressStyled["border-top-right-radius"])
        if self.pressStyled["border-bottom-right-radius"]:           pressStyle += "border-bottom-right-radius: {}px;\n".format(self.pressStyled["border-bottom-right-radius"])
        if self.pressStyled["border-bottom-left-radius"]:            pressStyle += "border-bottom-left-radius: {}px;\n".format(self.pressStyled["border-bottom-left-radius"])
        #
        pressStyle += "\n}\n"
###########################################################################################################################################
########    CONCATENED STYLES AND APPLY TO OUR OBJECT
###########################################################################################################################################
        resStyle = style + hoverStyle + pressStyle
        self.setStyleSheet(resStyle)
####
    def enterEvent(self, event: QEnterEvent) -> None:
        QWidget.enterEvent(self, event)
        self.repaint()
    def leaveEvent(self, event: QEvent) -> None:
        QWidget.leaveEvent(self, event)
        self.repaint()
    def paintEvent(self, event: QPaintEvent) -> None:
        QPushButton.paintEvent(self, event)
