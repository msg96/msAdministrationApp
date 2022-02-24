###########################################################################################################################
########    IMPORTS
###########################################################################################################################
import re
from env import ENVVAR as ENV
from env import usersdb_conn
import psycopg2
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
        return connect.cursor()
    except:
       return 0
###########################################################################################################################
########    EVENTO DE VERIFICAÇÃO DE LOGIN
###########################################################################################################################
def login (login, password) -> int:
    curCursor = tryconnect()
    if not curCursor:
        return 0
    useroremail =  "app_email"  if "@" in login else "app_username"
        
    curCursor.execute(f"SELECT {ENV['dbprivileges']} from {ENV['pgusertable']} WHERE {useroremail}='{login}' AND {ENV['dbpasscolum']}='{password}'")
    matched = curCursor.fetchall()
    if login == ENV["LocalUser"] and password == ENV["LocalPass"]:
        return 1
    if not matched: 
        return 0
    else:
        return matched[0][0]