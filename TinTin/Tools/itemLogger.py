import os
import sys
import mysql.connector
from mysql.connector import errorcode
from baseDatabase import BaseDatabase
from tintin import TinTin

db3k = BaseDatabase()

itemName = sys.argv[1]
itemDescription = sys.argv[2]
roomID = sys.argv[3]
area = sys.argv[4]

insertQuery = ("INSERT INTO MapItems (ItemName, AreaName, RoomID, ItemDescription ) VALUES (%s, %s, %s, %s)")


itemID = db3k.insert(insertQuery, [itemName, area, roomID, itemDescription] )
TinTin.execute("#draw Yellow scroll line 1 1 1 80;");
TinTin.echo("{<128>%-25s<088> recorded at [<168>%.5s<088>] in [<168>%-15s<088>]} {"+itemName+"} {"+roomID+"} {"+area+"}")
TinTin.execute("#draw Yellow scroll line 1 1 1 80;");

db3k.dispose()

