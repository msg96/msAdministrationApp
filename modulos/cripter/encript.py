###########################################################################################################################
###########################################################################################################################
###########################################################################################################################
###########################################################################################################################
############################################## -> DESGINED BY MATHEUS SANTOS ##############################################
###########################################################################################################################
###########################################################################################################################
###########################################################################################################################
###########################################################################################################################
import base64 as __base64
import os.path as __path
__codetype = "utf-8"

def fileEncript(filein_, pass_="", fileout_=""):
    if fileout_ == "":
        fileout_ = filein_
    if pass_ == "" or len(pass_) < 3:
        return False
    if not __path.exists(filein_):
        return False

    file_ =  open(filein_, "rb") 
    fileContent = file_.read()
    fileBytes = bytearray(fileContent)
    file_.close()
    receivedBytes = __enriptBytes(fileBytes, pass_)
    if not receivedBytes[0]:
        print("erro 1")
    else:
        file_e = open(fileout_, "wb")
        file_e.write(receivedBytes[1])
        file_e.close()

def encript(data_ :str , pass_) -> str:
        dataBytes_ = bytearray(data_, __codetype)
        receivedBytes = __enriptBytes(dataBytes_, pass_)
        if not receivedBytes[0]:
            return ""
        else:
            receivedResult = receivedBytes[1].decode(__codetype)
            return receivedResult
    
def __enriptBytes(data_, pass_):
    try:
        data_ = data_[::-1]
        pass_ = pass_[::-1]
        dataTo64 = __base64.b64encode(data_)
        passTo64 = __base64.b64encode(bytes(pass_, __codetype))
        passTo64 = passTo64[:-2]
        info = [dataTo64[i:i+len(passTo64)] for i in range(0, len(dataTo64), len(passTo64))]
        pb = bytearray()
        verifyCode1 = 0
        for i in passTo64:
            verifyCode1 += i
        for an in info:
            for n in range(len(an)):
                pb.append((an[n] ^ passTo64[n]))
        verifyCode2 = 0
        for i in pb:
            verifyCode2 += i
        verifyCode1 = (verifyCode1 % len(passTo64)) ^ len(passTo64)
        verifyCode1 = verifyCode1.to_bytes(length=(8 + (verifyCode1 + (verifyCode1 < 0)).bit_length()) // 8 , byteorder='big', signed=True)
        verifyCode2 = (verifyCode2 % len(passTo64)) ^ len(passTo64)
        verifyCode2 = verifyCode2.to_bytes(length=(8 + (verifyCode2 + (verifyCode2 < 0)).bit_length()) // 8 , byteorder='big', signed=True)
        pb[0:0] = verifyCode1
        pb[-1:-1] = verifyCode2
        
        return True, pb
    except:
        return False, data_ 
