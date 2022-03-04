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
class msPanel(QFrame):
    def __init__(self, parent :QWidget):
        super(msPanel, self).__init__()
        if not self.objectName():
            self.setObjectName(str(hash(self)))
        try:
            self.setParent(parent)
            self.setGeometry(parent.geometry())
        except:
            pass
########    PARAMETERS 
        self.styled = {
        "background-color": "",             "color": "",                    "flat-style": False,                    "text-align": "",
        "border-left-width": 0,             "border-left-style": "",        "border-left-color": "",                "vertical-align": "",
        "border-right-width": 0,            "border-right-style": "",       "border-right-color": "",
        "border-top-width": 0,              "border-top-style": "",         "border-top-color": "",
        "border-bottom-width": 0,           "border-bottom-style": "",      "border-bottom-color": "",
        "border-top-left-radius": 0,        "border-top-right-radius": 0,   "border-bottom-right-radius": 0,        "border-bottom-left-radius": 0,
        "padding-left": 0,                  "padding-right":0,              "padding-top": 0,                       "padding-bottom": 0
        }
        ####    HOVER
        self.hoverStyled = self.styled.copy()
        ####    PRESS
        self.pressStyled = self.styled.copy()
        ####    FOCUS 
        self.focusStyled = self.styled.copy()
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
    ####    FOCUS
    def focusBackgroundColor(self, color :str):
        self.focusStyled["background-color"] = color
        self.updateStyles()
####    CHANGE TEXT COLOR
    def color(self, color :str):
        self.styled["color"] = color
        self.updateStyles()
    ####    HOVER
    def hoverColor(self, color :str):
        self.hoverStyled["color"] = color
        self.updateStyles()
    ####    PRESS
    def pressColor(self, color :str):
        self.pressStyled["color"] = color
        self.updateStyles()
    ####    FOCUS
    def focusColor(self, color :str):
        self.focusStyled["color"] = color
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
    ####    FOCUS
    def focusFlatStyle(self, value :bool):
        self.focusStyled["flat-style"] = value
        self.updateStyles()
####    TEXTALIGN
    def textAlign(self, value :str):
        self.styled["text-align"] = value
        self.updateStyles()
    ####    HOVER
    def hoverTextAlign(self, value :str):
        self.hoverStyled["text-align"] = value
        self.updateStyles()
    ####    PRESS
    def pressTextAlign(self, value :str):
        self.pressStyled["text-align"] = value
        self.updateStyles()
    ####    FOCUS
    def focusTextAlign(self, value :str):
        self.focusStyled["text-align"] = value
        self.updateStyles()
####    VERTICALALIGN
    def verticalAlign(self, value :str):
        self.styled["vertical-align"] = value
        self.updateStyles()
    ####    HOVER
    def hoverVerticalAlign(self, value :str):
        self.hoverStyled["vertical-align"] = value
        self.updateStyles()
    ####    PRESS
    def pressVerticalAlign(self, value :str):
        self.pressStyled["vertical-align"] = value
        self.updateStyles()
    ####    FOCUS
    def focusVerticalAlign(self, value :str):
        self.focusStyled["vertical-align"] = value
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
    ####    FOCUS
    def focusBorder(self, width :int, style :str, color :str):
        self.focusStyled["border-left-width"] = self.focusStyled["border-right-width"] = self.focusStyled["border-top-width"] = self.focusStyled["border-bottom-width"] = width
        self.focusStyled["border-left-style"] = self.focusStyled["border-right-style"] = self.focusStyled["border-top-style"] = self.focusStyled["border-bottom-style"] = style
        self.focusStyled["border-left-color"] = self.focusStyled["border-right-color"] = self.focusStyled["border-top-color"] = self.focusStyled["border-bottom-color"] = color
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
    ####    FOCUS
    def focusBorderLeft(self, width :int, style :str, color :str):
        self.focusStyled["border-left-width"] = width
        self.focusStyled["border-left-style"] = style
        self.focusStyled["border-left-color"] = color
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
    ####    FOCUS
    def focusBorderRight(self, width :int, style :str, color :str):
        self.focusStyled["border-right-width"] = width
        self.focusStyled["border-right-style"] = style
        self.focusStyled["border-right-color"] = color
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
    ####    FOCUS
    def focusBorderTop(self, width :int, style :str, color :str):
        self.focusStyled["border-top-width"] = width
        self.focusStyled["border-top-style"] = style
        self.focusStyled["border-top-color"] = color
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
    ####    FOCUS
    def focusBorderBottom(self, width :int, style :str, color :str):
        self.focusStyled["border-bottom-width"] = width
        self.focusStyled["border-bottom-style"] = style
        self.focusStyled["border-bottom-color"] = color
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
    ####    FOCUS
    def focusBorderRadius(self, topleft :int, topright :int, bottomright :int, bottomleft :int):
        self.focusStyled["border-top-left-radius"] =     topleft
        self.focusStyled["border-top-right-radius"] =    topright
        self.focusStyled["border-bottom-right-radius"] = bottomright
        self.focusStyled["border-bottom-left-radius"] =  bottomleft
        self.updateStyles()
####    PADDING CHANGE PARAMS
    def padding(self, top :int, right :int, bottom :int, left :int):
        self.styled["padding-top"] = top
        self.styled["padding-right"] = right
        self.styled["padding-bottom"] = bottom
        self.styled["padding-left"] = left
        self.updateStyles()
    ####    HOVER
    def hoverPadding(self, top :int, right :int, bottom :int, left :int):
        self.hoverStyled["padding-top"] = top
        self.hoverStyled["padding-right"] = right
        self.hoverStyled["padding-bottom"] = bottom
        self.hoverStyled["padding-left"] = left
        self.updateStyles()
    ####    PRESS
    def pressPadding(self, top :int, right :int, bottom :int, left :int):
        self.pressStyled["padding-top"] = top
        self.pressStyled["padding-right"] = right
        self.pressStyled["padding-bottom"] = bottom
        self.pressStyled["padding-left"] = left
        self.updateStyles()
    ####    FOCUS
    def focusPadding(self, top :int, right :int, bottom :int, left :int):
        self.focusStyled["padding-top"] = top
        self.focusStyled["padding-right"] = right
        self.focusStyled["padding-bottom"] = bottom
        self.focusStyled["padding-left"] = left
        self.updateStyles()
####    PADDING LEFT CHANGE PARAMS
    def paddingLeft(self, value :int):
        self.styled["padding-left"] = value
        self.updateStyles()
    ####    HOVER
    def hoverPaddingLeft(self, value :int):
        self.hoverStyled["padding-left"] = value
        self.updateStyles()
    ####    PRESS
    def pressPaddingLeft(self, value :int):
        self.pressStyled["padding-left"] = value
        self.updateStyles()
    ####    FOCUS
    def focusPaddingLeft(self, value :int):
        self.focusStyled["padding-left"] = value
        self.updateStyles()
####    PADDING RIGHT CHANGE PARAMS
    def paddingRight(self, value :int):
        self.styled["padding-right"] = value
        self.updateStyles()
    ####    HOVER
    def hoverPaddingRight(self, value :int):
        self.hoverStyled["padding-right"] = value
        self.updateStyles()
    ####    PRESS
    def pressPaddingRight(self, value :int):
        self.pressStyled["padding-right"] = value
        self.updateStyles()
    ####    FOCUS
    def focusPaddingRight(self, value :int):
        self.focusStyled["padding-right"] = value
        self.updateStyles()
####    PADDING TOP CHANGE PARAMS
    def paddingTop(self, value :int):
        self.styled["padding-top"] = value
        self.updateStyles()
    ####    HOVER
    def hoverPaddingTop(self, value :int):
        self.hoverStyled["padding-top"] = value
        self.updateStyles()
    ####    PRESS
    def pressPaddingTop(self, value :int):
        self.pressStyled["padding-top"] = value
        self.updateStyles()
    ####    FOCUS
    def focusPaddingTop(self, value :int):
        self.focusStyled["padding-top"] = value
        self.updateStyles()
####    PADDING BOTTOM CHANGE PARAMS
    def paddingBottom(self, value :int):
        self.styled["padding-bottom"] = value
        self.updateStyles()
    ####    HOVER
    def hoverPaddingBottom(self, value :int):
        self.hoverStyled["padding-bottom"] = value
        self.updateStyles()
    ####    PRESS
    def pressPaddingBottom(self, value :int):
        self.pressStyled["padding-bottom"] = value
        self.updateStyles()
    ####    FOCUS
    def focusPaddingBottom(self, value :int):
        self.focusStyled["padding-bottom"] = value
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
        focusBackgroundColor = self.focusStyled["background-color"] if not self.focusStyled["flat-style"] else flatColor
########
##########################################################################################################################################
########    APPEND STYLE TO AN STRING
##########################################################################################################################################   
        style_ = "{}#{} {{\n".format(objectType, self.objectName())
        #
        if self.styled["background-color"] != "":          style_ += "background-color: {};\n".format(backgroundColor)
        if self.styled["color"] != "":                     style_ += "color: {};\n".format(self.styled["color"])
        if self.styled["text-align"] != "":                style_ += "text-align: {};\n".format(self.styled["text-align"])
        if self.styled["vertical-align"] != "":            style_ += "vertical-align: {};\n".format(self.styled["vertical-align"])
        if self.styled["border-left-width"]:               style_ += "border-left-width: {}px;\n".format(self.styled["border-left-width"])
        if self.styled["border-left-style"] != "":         style_ += "border-left-style: {};\n".format(self.styled["border-left-style"])
        if self.styled["border-left-color"] != "":         style_ += "border-left-color: {};\n".format(self.styled["border-left-color"])
        if self.styled["border-right-width"]:              style_ += "border-right-width: {}px;\n".format(self.styled["border-right-width"])
        if self.styled["border-right-style"] != "":        style_ += "border-right-style: {};\n".format(self.styled["border-right-style"])
        if self.styled["border-right-color"] != "":        style_ += "border-right-color: {};\n".format(self.styled["border-right-color"])
        if self.styled["border-top-width"]:                style_ += "border-top-width: {}px;\n".format(self.styled["border-top-width"])
        if self.styled["border-top-style"] != "":          style_ += "border-top-style: {};\n".format(self.styled["border-top-style"])
        if self.styled["border-top-color"] != "":          style_ += "border-top-color: {};\n".format(self.styled["border-top-color"])
        if self.styled["border-bottom-width"]:             style_ += "border-bottom-width: {}px;\n".format(self.styled["border-bottom-width"])
        if self.styled["border-bottom-style"] != "":       style_ += "border-bottom-style: {};\n".format(self.styled["border-bottom-style"])
        if self.styled["border-bottom-color"] != "":       style_ += "border-bottom-color: {};\n".format(self.styled["border-bottom-color"])
        if self.styled["border-top-left-radius"]:          style_ += "border-top-left-radius: {}px;\n".format(self.styled["border-top-left-radius"])
        if self.styled["border-top-right-radius"]:         style_ += "border-top-right-radius: {}px;\n".format(self.styled["border-top-right-radius"])
        if self.styled["border-bottom-right-radius"]:      style_ += "border-bottom-right-radius: {}px;\n".format(self.styled["border-bottom-right-radius"])
        if self.styled["border-bottom-left-radius"]:       style_ += "border-bottom-left-radius: {}px;\n".format(self.styled["border-bottom-left-radius"])
        if self.styled["padding-left"]:                    style_ += "padding-left: {}px;\n".format(self.styled["padding-left"])
        if self.styled["padding-right"]:                   style_ += "padding-right: {}px;\n".format(self.styled["padding-right"])
        if self.styled["padding-top"]:                     style_ += "padding-top: {}px;\n".format(self.styled["padding-top"])
        if self.styled["padding-bottom"]:                  style_ += "padding-bottom: {}px;\n".format(self.styled["padding-bottom"])
        #
        style_ += "\n}\n"
###########################################################################################################################################
########    APEEND HOVER STYLE TO AN STRING
###########################################################################################################################################
        hoverStyle = "{}#{}:hover {{\n".format(objectType, self.objectName())
        #
        if self.hoverStyled["background-color"] != "":              hoverStyle += "background-color: {};\n".format(hoverBackgroundColor)
        if self.hoverStyled["color"] != "":                         hoverStyle += "color: {};\n".format(self.hoverStyled["color"])
        if self.hoverStyled["text-align"] != "":                    hoverStyle += "text-align: {};\n".format(self.hoverStyled["text-align"])
        if self.hoverStyled["vertical-align"] != "":                hoverStyle += "vertical-align: {};\n".format(self.hoverStyled["vertical-align"])
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
        if self.hoverStyled["padding-left"]:                        hoverStyle += "padding-left: {}px;\n".format(self.hoverStyled["padding-left"])
        if self.hoverStyled["padding-right"]:                       hoverStyle += "padding-right: {}px;\n".format(self.hoverStyled["padding-right"])
        if self.hoverStyled["padding-top"]:                         hoverStyle += "padding-top: {}px;\n".format(self.hoverStyled["padding-top"])
        if self.hoverStyled["padding-bottom"]:                      hoverStyle += "padding-bottom: {}px;\n".format(self.hoverStyled["padding-bottom"])
        #
        hoverStyle += "\n}\n"
###########################################################################################################################################
########    APPEND PRESS STYLE TO AN STRING
###########################################################################################################################################
        pressStyle = "{}#{}:pressed {{\n".format(objectType, self.objectName())
        #
        if self.pressStyled["background-color"] != "":               pressStyle += "background-color: {};\n".format(pressBackgroundColor)
        if self.pressStyled["color"] != "":                          pressStyle += "color: {};\n".format(self.pressStyled["color"])
        if self.pressStyled["text-align"] != "":                     pressStyle += "text-align: {};\n".format(self.pressStyled["text-align"])
        if self.pressStyled["vertical-align"] != "":                 pressStyle += "vertical-align: {};\n".format(self.pressStyled["vertical-align"])
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
        if self.pressStyled["padding-left"]:                         pressStyle += "padding-left: {}px;\n".format(self.pressStyled["padding-left"])
        if self.pressStyled["padding-right"]:                        pressStyle += "padding-right: {}px;\n".format(self.pressStyled["padding-right"])
        if self.pressStyled["padding-top"]:                          pressStyle += "padding-top: {}px;\n".format(self.pressStyled["padding-top"])
        if self.pressStyled["padding-bottom"]:                       pressStyle += "padding-bottom: {}px;\n".format(self.pressStyled["padding-bottom"])
        #
        pressStyle += "\n}\n"
###########################################################################################################################################
########    APPEND FOCUS STYLE TO AN STRING
###########################################################################################################################################
        focusStyle = "{}#{}:focus {{\n".format(objectType, self.objectName())
        #
        if self.focusStyled["background-color"] != "":               focusStyle += "background-color: {};\n".format(focusBackgroundColor)
        if self.focusStyled["color"] != "":                          focusStyle += "color: {};\n".format(self.focusStyled["color"])
        if self.focusStyled["text-align"] != "":                     focusStyle += "text-align: {};\n".format(self.focusStyled["text-align"])
        if self.focusStyled["vertical-align"] != "":                 focusStyle += "vertical-align: {};\n".format(self.focusStyled["vertical-align"])
        if self.focusStyled["border-left-width"]:                    focusStyle += "border-left-width: {}px;\n".format(self.focusStyled["border-left-width"])
        if self.focusStyled["border-left-style"] != "":              focusStyle += "border-left-style: {};\n".format(self.focusStyled["border-left-style"])
        if self.focusStyled["border-left-color"] != "":              focusStyle += "border-left-color: {};\n".format(self.focusStyled["border-left-color"])
        if self.focusStyled["border-right-width"]:                   focusStyle += "border-right-width: {}px;\n".format(self.focusStyled["border-right-width"])
        if self.focusStyled["border-right-style"] != "":             focusStyle += "border-right-style: {};\n".format(self.focusStyled["border-right-style"])
        if self.focusStyled["border-right-color"] != "":             focusStyle += "border-right-color: {};\n".format(self.focusStyled["border-right-color"])
        if self.focusStyled["border-top-width"]:                     focusStyle += "border-top-width: {}px;\n".format(self.focusStyled["border-top-width"])
        if self.focusStyled["border-top-style"] != "":               focusStyle += "border-top-style: {};\n".format(self.focusStyled["border-top-style"])
        if self.focusStyled["border-top-color"] != "":               focusStyle += "border-top-color: {};\n".format(self.focusStyled["border-top-color"])
        if self.focusStyled["border-bottom-width"]:                  focusStyle += "border-bottom-width: {}px;\n".format(self.focusStyled["border-bottom-width"])
        if self.focusStyled["border-bottom-style"] != "":            focusStyle += "border-bottom-style: {};\n".format(self.focusStyled["border-bottom-style"])
        if self.focusStyled["border-bottom-color"] != "":            focusStyle += "border-bottom-color: {};\n".format(self.focusStyled["border-bottom-color"])
        if self.focusStyled["border-top-left-radius"]:               focusStyle += "border-top-left-radius: {}px;\n".format(self.focusStyled["border-top-left-radius"])
        if self.focusStyled["border-top-right-radius"]:              focusStyle += "border-top-right-radius: {}px;\n".format(self.focusStyled["border-top-right-radius"])
        if self.focusStyled["border-bottom-right-radius"]:           focusStyle += "border-bottom-right-radius: {}px;\n".format(self.focusStyled["border-bottom-right-radius"])
        if self.focusStyled["border-bottom-left-radius"]:            focusStyle += "border-bottom-left-radius: {}px;\n".format(self.focusStyled["border-bottom-left-radius"])
        if self.focusStyled["padding-left"]:                         focusStyle += "padding-left: {}px;\n".format(self.focusStyled["padding-left"])
        if self.focusStyled["padding-right"]:                        focusStyle += "padding-right: {}px;\n".format(self.focusStyled["padding-right"])
        if self.focusStyled["padding-top"]:                          focusStyle += "padding-top: {}px;\n".format(self.focusStyled["padding-top"])
        if self.focusStyled["padding-bottom"]:                       focusStyle += "padding-bottom: {}px;\n".format(self.focusStyled["padding-bottom"])
        #
        focusStyle += "\n}\n"


###########################################################################################################################################
########    CONCATENED STYLES AND APPLY TO OUR OBJECT
###########################################################################################################################################
        resStyle = style_ + hoverStyle + pressStyle + focusStyle
        self.setStyleSheet(resStyle)
####
    def enterEvent(self, event: QEnterEvent) -> None:
        QWidget.enterEvent(self, event)
        self.repaint()
    def leaveEvent(self, event: QEvent) -> None:
        QWidget.leaveEvent(self, event)
        self.repaint()
    def paintEvent(self, event: QPaintEvent) -> None:
        QFrame.paintEvent(self, event)
