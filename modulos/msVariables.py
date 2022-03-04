from .customFunctions.appGetUniversalPath import AppGetUniversalPath as __AppGetUniversalPath
from .customFunctions.appGetFile import AppGetFile as __AppGetFile

styleJson = __AppGetFile(__AppGetUniversalPath("assets"), "style.json")
admin = 'admin'