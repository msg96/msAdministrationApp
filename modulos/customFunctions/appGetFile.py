import os

def AppGetFile(PathName, FileName) -> str:
    return os.path.normpath(os.path.join(PathName, FileName))