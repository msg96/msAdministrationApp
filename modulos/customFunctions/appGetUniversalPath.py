import os

def AppGetUniversalPath(PathName):
    AppFolder = os.path.abspath(os.getcwd())
    JoinFolder = os.path.join(AppFolder, PathName)
    return os.path.normpath(os.path.join(JoinFolder))