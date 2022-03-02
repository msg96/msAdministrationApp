import uuid as __uuid
from modulos import cripter
from env import ENVVAR as ENV

def getHWND() -> str:
    return str(__uuid.uuid1()).split("-")[-1]

def getEncriptedHWND():
    result = cripter.encript(getHWND(), ENV["bdmasterkey"])
    return result

def decriptHWND(encHWND):
    result = cripter.decript(encHWND, ENV["bdmasterkey"])
    return result