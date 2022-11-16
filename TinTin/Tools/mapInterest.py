import sys
import mysql.connector
import mysql.connector
from mysql.connector import errorcode
from tintin import TinTin
import os
from baseDatabase import BaseDatabase

db3k = BaseDatabase()

mapNote = sys.argv[1]
roomID = sys.argv[2]
areaName = sys.argv[3]
symbol = sys.argv[4]

interestID = db3k.insert("INSERT INTO MapInterests (Note, RoomID, AreaName, RoomSymbol) VALUES (%s, %s, %s, %s)",
    [mapNote, roomID, areaName, symbol])

TinTin.showme("<094>--- InterestID [" + interestID + "] added.")

db3k.dispose()
  

