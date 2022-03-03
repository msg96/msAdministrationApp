###########################################################################################################################
###########################################################################################################################
###########################################################################################################################
###########################################################################################################################
############################################## -> DESGINED BY MATHEUS SANTOS ##############################################
###########################################################################################################################
###########################################################################################################################
###########################################################################################################################
###########################################################################################################################
################################# RELAX BECAUSE SECURITY INFOS NOT UPDATE FROM HERE :)    #################################
###########################################################################################################################
###################### JUST FOR TESTS, THIS PART OF THE PROGRAM NEED TO MIGRATED TO YOUR BACKEND    #######################
########### THIS PROGRAM SIMULATE SOME TO PERSONAL USER APP, AND I USE STAND ALONE METHOD. BUT ITS NOT RECOMENDED   #######
###########################################################################################################################
########    IMPORTS
###########################################################################################################################
import string
from env import ENVVAR as ENV
from env import usersdb_conn
import psycopg2
from modulos import cripter
from modulos import hwnd
from modulos.cripter.encript import encript
import re
###########################################################################################################################
########    VARIAVEIS
###########################################################################################################################
#

###########################################################################################################################
########    DATA BASE INFOS VIDE .GITIGNORE FIRST -> IF U NOT SEE ENV.PY IN PROJECT GET ENV.PY.EXAMPLE
########    JUST CREATE SOME LIKE HIM
###########################################################################################################################
#
def tryconnect():
    try:
        connect = psycopg2.connect(usersdb_conn)
        return connect.cursor(), connect
    except:
       return 0
### FUNCTION TO CHECK IF EMAIL IS VALID EMAIL
def emailValidator(value):
    emailRgx = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return True if(re.fullmatch(emailRgx, value)) else False
###########################################################################################################################
def passwordStronger(value):
    if not any(c in string.punctuation for c in value): return False
    if not any(c in string.ascii_uppercase for c in value): return False
    if not any(c in string.ascii_lowercase for c in value): return False
    if not any(c in string.digits for c in value): return False
    if len(value) < 8: return False
    # IF NOT HAVE 1 SYMBOL 1 UPPERCASE 1 LOWERCASE 1 DIGIT AND VALUE LENGHT IS SMALL A 8 RETURN FALSE
    return True

###########################################################################################################################
########    EVENT TO CHECK LOGIN
###########################################################################################################################
def login (login, password) -> int:
####    ENCRIPT HWND LIKE LOGIN AUTH NEEDED ON MAIN FILE
    hwnd_ = cripter.digest(hwnd.getHWND())
######  LOCAL FOR TEST PURPOSE
######  IF YOU PUT SOME 0 OR "" IN LocalUser or LocalPass YOU DISABLE YOUR LOCAL TEST LOGIN. IT'S EASY :)
    if ENV["LocalUser"] and ENV["LocalPass"] and ENV["LocalEmail"]:
        if (login == ENV["LocalUser"] or login == ENV["LocalEmail"]) and password == ENV["LocalPass"]:
            return [0, ENV["LocalUser"] , ENV["LocalEmail"], ENV["LocalPass"], 1, None, hwnd_]
###############################################################################################################
#################################################################################################
    curCursor = tryconnect()
    if not curCursor:
        return 0
####    VERIFY IF USER TRY LOGIN WITH EMAIL OR USERNAME
    useroremail =  ENV["emailrow"]  if "@" in login else ENV["userrow"]
####    ENCRIPT DATA
    login = cripter.digest(login)
    password = cripter.digest(password)
####    USE THIS SINTAX TO PREVENT SQL INJECTION
    ##  EXECUTABLE QUERY
    QueryStr = f"SELECT * FROM {ENV['pgusertable']} WHERE {useroremail}=%(login)s AND {ENV['dbpasscolum']}=%(password)s"
    intoData = {'login': login, 'password': password}
    curCursor[0].execute(QueryStr, intoData)
    matched = curCursor[0].fetchall()

#####   VERIFY IF SOME MATCH AND SEND SOME RESPONSE TO CALLER
    if not matched:
        curCursor[0].close()
        return 0
    else:
        if matched[0][6] == None:
            hwnd_ = cripter.digest(hwnd.getHWND())
            listhwnd = []
            listhwnd.append(hwnd_)
            ##  EXECUTABLE QUERY
            QueryStr = f"UPDATE {ENV['pgusertable']} SET {ENV['hwndrow']}=%(hwnd_)s WHERE {ENV['dbidrow']}={int(matched[0][0])}"
            intoData = {"hwnd_": listhwnd}
            curCursor[0].execute(QueryStr, intoData)
            curCursor[1].commit()
            ##  CLOSE CONNECTION
            curCursor[0].close()
            ## RETORNA ALL VALUES WITH NEW HWND WITHOUT CHECK AGAIN IN THE TABLE
            result = (matched[0][0],matched[0][1],matched[0][2],matched[0][3],matched[0][4],matched[0][5],listhwnd)
            return result
        else:
            ##  CLOSE CONNECTION
            curCursor[0].close()
            return matched[0]
########    EVENT TO CHANGE PASSWORD
def ChangePW(login :str, oldpassword :str, newpassword :str):
    curCursor = tryconnect()
    if not curCursor: return
    ## VERIFY IF USER PUT EMAIL OR USERNAME
    useroremail =  ENV["emailrow"]  if "@" in login else ENV["userrow"]
    ## ECRIPT DATA
    login = cripter.digest(login)
    oldpassword = cripter.digest(oldpassword)
    newpassword = cripter.digest(newpassword)
    ## EXECUTABLE QUERY
#### USING THIS METHOD TO PASS OUR DATA TO QUERY TO PREVENT SOME SQLINJECTION IF ANY PEOPLE INTERCEPT OUR COMMUNICATION WITH DATABASE
    QueryStr = f"UPDATE {ENV['pgusertable']} SET {ENV['dbpasscolum']}=%(newpassword)s WHERE {useroremail}=%(login)s AND {ENV['dbpasscolum']}=%(oldpassword)s"
    intoData = {'newpassword': newpassword, 'login': login, 'oldpassword': oldpassword }
    curCursor[0].execute(QueryStr, intoData)
    curCursor[1].commit()
    ## CLOSE CONNECTION
    curCursor[0].close()
######  EVENT TO CREATE NEW USERS :)
def CreateUser(login :str, email :str, password :str, privilege :int) -> str:
    curCursor = tryconnect()
    if not curCursor: return
    ## Checkers
    if any(c in string.punctuation for c in login): return "username with not valid characters"
    if not emailValidator(email): return "Inserted email invalid!."
    if not passwordStronger(password): return "Weak password was inserted!."
    ## ENCRIPT DATA
    login = cripter.digest(login)
    email = cripter.digest(email)
    password = cripter.digest(password)
    privilege = int(privilege)
    hwnd_ = cripter.digest(hwnd.getHWND())
    listhwnd = []
    listhwnd.append(hwnd_)
    ## VERIFY IF USER EXIST IN TABLE
    QueryStr = f"SELECT {ENV['dbidrow']} FROM {ENV['pgusertable']} WHERE {ENV['userrow']}=%(login)s OR {ENV['emailrow']}=%(email)s"
    intoData = {'login': login, 'email': email}
    curCursor[0].execute(QueryStr, intoData)
    have = curCursor[0].fetchall()
    if have:
        curCursor[0].close() 
        return "user allaready registred before."
    ## EXECUTABLE QUERY
    QueryStr = f"INSERT INTO {ENV['pgusertable']} ({ENV['dbusercolum']},{ENV['emailrow']},{ENV['dbpasscolum']},{ENV['dbprivileges']},{ENV['hwndrow']}) VALUES (%(user)s,%(email)s,%(password)s,%(privilege)s,%(hwnd)s)"
    intoData = {"user": login, "email": email, "password": password, "privilege": privilege, "hwnd": listhwnd}
    curCursor[0].execute(QueryStr, intoData)
    curCursor[1].commit()
    ## CLOSE CONNECTION
    curCursor[0].close()
######  EVENT TO DELETE USERS
def DeleteUser(login :str, password :str):
    curCursor = tryconnect()
    if not curCursor: return

    login = cripter.digest(login)
    password = cripter.digest(password)

    QueryStr = f"DELETE FROM {ENV['pgusertable']} WHERE {ENV['dbusercolum']}=%(login)s AND {ENV['dbpasscolum']}=%(password)s"
    intoData = {'login': login, 'password': password}
    curCursor[0].execute(QueryStr, intoData)
    curCursor[1].commit()
    ## CLOSE CONNECTION
    curCursor[0].close()
