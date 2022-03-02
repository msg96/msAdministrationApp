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
from env import ENVVAR as ENV
from env import usersdb_conn
import psycopg2

from modulos import cripter
###########################################################################################################################
########    VARIAVEIS
###########################################################################################################################
#
###########################################################################################################################
########    DATA BASE INFOS VIDE .GITIGNORE FIRST 
###########################################################################################################################
#
def tryconnect():
    try:
        connect = psycopg2.connect(usersdb_conn)
        return connect.cursor(), connect
    except:
       return 0
###########################################################################################################################
########    EVENTO DE VERIFICAÇÃO DE LOGIN
###########################################################################################################################
def login (login, password) -> int:
    curCursor = tryconnect()
    if not curCursor:
        return 0
    useroremail =  ENV["emailrow"]  if "@" in login else ENV["userrow"]
####    ENCRIPT DATA
    login = cripter.encript(login, ENV['bdmasterkey'])
    login = str(bytes(login, "utf-8")).replace("'", "").replace("b(","")
    password = cripter.encript(password, ENV['bdmasterkey'])
    password = str(bytes(password, "utf-8")).replace("'", "").replace("b(","")
####    USE THIS SINTAX TO PREVENT SQL INJECTION
    curCursor[0].execute(f"SELECT * FROM {ENV['pgusertable']} WHERE {useroremail}=%(login)s AND {ENV['dbpasscolum']}=%(password)s",
     {'login': login, 'password': password})
    matched = curCursor[0].fetchall()
######  IF YOU PUT SOME 0 OR "" IN LocalUser or LocalPass YOU DISABLE YOUR LOCAL TEST LOGIN. IT'S EASY :)
    if ENV["LocalUser"] and ENV["LocalPass"]:
        if login == ENV["LocalUser"] and password == ENV["LocalPass"]:
            return [1, "admin"]
#####   VERIFY IF SOME MATCH AND SEND SOME RESPONSE TO CALLER
    curCursor[0].close()
    if not matched: 
        return 0
    else:
        return matched[0]


def ChangePW(login :str, oldpassword :str, newpassword :str):
    curCursor = tryconnect()
    if not curCursor:
        return
    ## VERIFY IF USER PUT EMAIL OR USERNAME
    useroremail =  ENV["emailrow"]  if "@" in login else ENV["userrow"]
    ## ECRIPT DATA
    login = cripter.encript(login, ENV['bdmasterkey'])
    login = str(bytes(login, "utf-8")).replace("'", "").replace("b(","")
    oldpassword = cripter.encript(oldpassword, ENV['bdmasterkey'])
    oldpassword = str(bytes(oldpassword, "utf-8")).replace("'", "").replace("b(","")
    newpassword = cripter.encript(newpassword, ENV['bdmasterkey'])
    newpassword = str(bytes(newpassword, "utf-8")).replace("'", "").replace("b(","")
    ##
    curCursor[0].execute(f"UPDATE {ENV['pgusertable']} SET {ENV['dbpasscolum']}=%(newpassword)s WHERE {useroremail}=%(login)s AND {ENV['dbpasscolum']}=%(oldpassword)s",
     {'newpassword': newpassword, 'login': login, 'oldpassword': oldpassword })
    curCursor[1].commit()
    curCursor[0].close()