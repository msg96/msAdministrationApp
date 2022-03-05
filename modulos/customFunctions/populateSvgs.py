import os
from ..customFunctions.appGetUniversalPath import AppGetUniversalPath as __AppGetUniversalPath
from ..customFunctions.appGetFile import AppGetFile as __AppGetFile
#
def populateSvgs() -> dict:
        Svgs = {}
        SvgPath = __AppGetUniversalPath("assets/svg/")
        for file in os.listdir(SvgPath):
                if file.endswith(".svg"):
                        filename = file.split("/")[-1].replace(".svg", "")
                        fullfilename = __AppGetFile(SvgPath, file)
                        Svgs.update({filename: fullfilename})
        return Svgs