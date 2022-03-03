import json
import os
from ..msVariables import  styleJson
from assets.styles import *

def LoadJsonStyle():
    if not os.path.exists(styleJson):

        with open(styleJson, "w") as _file:
            js = json.dumps(defaultStyle, sort_keys=True, indent=4, separators=(',', ': '))
            _file.write(js)
            _file.close()
    else:
        with open(styleJson, "r") as _file:
            x = json.load(_file)
            _file.close()
            for i in x:
                style.update({i: x[i]})

def saveStyleToJson():
    with open(styleJson, "w") as _file:
            js = json.dumps(style, sort_keys=True, indent=4, separators=(',', ': '))
            _file.write(js)
            _file.close()
